	component nios_setup_v2 is
		port (
			button_external_connection_export : in  std_logic_vector(3 downto 0) := (others => 'X'); -- export
			clk_clk                           : in  std_logic                    := 'X';             -- clk
			hex0_external_connection_export   : out std_logic_vector(6 downto 0);                    -- export
			hex_1_external_connection_export  : out std_logic_vector(6 downto 0);                    -- export
			hex_2_external_connection_export  : out std_logic_vector(6 downto 0);                    -- export
			hex_3_external_connection_export  : out std_logic_vector(6 downto 0);                    -- export
			hex_4_external_connection_export  : out std_logic_vector(6 downto 0);                    -- export
			hex_5_external_connection_export  : out std_logic_vector(6 downto 0);                    -- export
			led_external_connection_export    : out std_logic_vector(9 downto 0);                    -- export
			reset_reset_n                     : in  std_logic                    := 'X';             -- reset_n
			switch_external_connection_export : in  std_logic_vector(9 downto 0) := (others => 'X')  -- export
		);
	end component nios_setup_v2;

	u0 : component nios_setup_v2
		port map (
			button_external_connection_export => CONNECTED_TO_button_external_connection_export, -- button_external_connection.export
			clk_clk                           => CONNECTED_TO_clk_clk,                           --                        clk.clk
			hex0_external_connection_export   => CONNECTED_TO_hex0_external_connection_export,   --   hex0_external_connection.export
			hex_1_external_connection_export  => CONNECTED_TO_hex_1_external_connection_export,  --  hex_1_external_connection.export
			hex_2_external_connection_export  => CONNECTED_TO_hex_2_external_connection_export,  --  hex_2_external_connection.export
			hex_3_external_connection_export  => CONNECTED_TO_hex_3_external_connection_export,  --  hex_3_external_connection.export
			hex_4_external_connection_export  => CONNECTED_TO_hex_4_external_connection_export,  --  hex_4_external_connection.export
			hex_5_external_connection_export  => CONNECTED_TO_hex_5_external_connection_export,  --  hex_5_external_connection.export
			led_external_connection_export    => CONNECTED_TO_led_external_connection_export,    --    led_external_connection.export
			reset_reset_n                     => CONNECTED_TO_reset_reset_n,                     --                      reset.reset_n
			switch_external_connection_export => CONNECTED_TO_switch_external_connection_export  -- switch_external_connection.export
		);

