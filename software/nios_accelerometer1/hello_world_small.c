#include "system.h"
#include "altera_up_avalon_accelerometer_spi.h"
#include "altera_avalon_timer_regs.h"
#include "altera_avalon_timer.h"
#include "altera_avalon_pio_regs.h"
#include "sys/alt_irq.h"
#include <stdlib.h>

#define OFFSET -32
#define PWM_PERIOD 16
#define FILTER_TAP_NUM 4
//#define COEFFICIENT 0.5f

alt_8 pwm = 0;
alt_u8 led;
int level;

void led_write(alt_u8 led_pattern) {
    IOWR(LED_BASE, 0, led_pattern);
}

float applyFilter(float new_reading){
      static float filter[FILTER_TAP_NUM] = {0};
      static float coeff[] = {-0.1204, 0.2879, 0.6369, 0.2879};
      float filtered_reading = 0;

      for(int i = FILTER_TAP_NUM - 1; i > 0; i--){
            filter[i] = filter[i-1];
      }

      filter[0] = new_reading;

      for(int i = 0; i < FILTER_TAP_NUM; i++){
            filtered_reading += filter[i] * coeff[i];
      }
      return filtered_reading;
}


void convert_read(alt_32 acc_read, int * level, alt_u8 * led) {
    acc_read += OFFSET;
    alt_u8 val = (acc_read >> 6) & 0x07;
    alt_printf("val: %x\n", val);
    * led = (8 >> val) | (8 << (8 - val));
    alt_printf("led: %x\n", (8 >> val) | (8 << (8 - val)));
    * level = (acc_read >> 1) & 0x1f;
}

void sys_timer_isr() {
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER_BASE, 0);

    if (pwm < abs(level)) {

        if (level < 0) {
            led_write(led << 1);
        } else {
            led_write(led >> 1);
        }

    } else {
        led_write(led);
    }

    if (pwm > PWM_PERIOD) {
        pwm = 0;
    } else {
        pwm++;
    }

}

void timer_init(void * isr) {

    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER_BASE, 0x0003);
    IOWR_ALTERA_AVALON_TIMER_STATUS(TIMER_BASE, 0);
    IOWR_ALTERA_AVALON_TIMER_PERIODL(TIMER_BASE, 0x0900);
    IOWR_ALTERA_AVALON_TIMER_PERIODH(TIMER_BASE, 0x0000);
    alt_irq_register(TIMER_IRQ, 0, isr);
    IOWR_ALTERA_AVALON_TIMER_CONTROL(TIMER_BASE, 0x0007);

}

int main() {

    alt_32 x_read;
    alt_up_accelerometer_spi_dev * acc_dev;
    acc_dev = alt_up_accelerometer_spi_open_dev("/dev/accelerometer_spi");
    if (acc_dev == NULL) { // if return 1, check if the spi ip name is "accelerometer_spi"
        return 1;
    }

    timer_init(sys_timer_isr);
    while (1) {

        alt_up_accelerometer_spi_read_x_axis(acc_dev, & x_read);

//        float x = (float)x_read;

        alt_32 filtered_reading = (alt_32)applyFilter((float)x_read);

//        int level;
//        alt_u8 led;
        alt_printf("raw data: %x\n", x_read);
        alt_printf("filtered data: %x\n", filtered_reading);
        convert_read(filtered_reading, &level, &led);

    }

    return 0;
}
