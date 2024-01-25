
module nios_setup_v2 (
	button_external_connection_export,
	clk_clk,
	hex0_external_connection_export,
	hex_1_external_connection_export,
	hex_2_external_connection_export,
	hex_3_external_connection_export,
	hex_4_external_connection_export,
	hex_5_external_connection_export,
	led_external_connection_export,
	reset_reset_n,
	switch_external_connection_export);	

	input	[3:0]	button_external_connection_export;
	input		clk_clk;
	output	[6:0]	hex0_external_connection_export;
	output	[6:0]	hex_1_external_connection_export;
	output	[6:0]	hex_2_external_connection_export;
	output	[6:0]	hex_3_external_connection_export;
	output	[6:0]	hex_4_external_connection_export;
	output	[6:0]	hex_5_external_connection_export;
	output	[9:0]	led_external_connection_export;
	input		reset_reset_n;
	input	[9:0]	switch_external_connection_export;
endmodule
