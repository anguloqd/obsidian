## 00 // notes sur VHDL

```vhdl
entity my_entity is
	-- les ports (entrées et sorties) de l'entité, de la composante
	port (
				-- ...
	);
end entity counter;

architecture behavorial of my_entity is
	-- définiton des signaux internes
	signal my_signal : -- ...
begin
	-- process pour les procedures séquentielles
	-- idéale pour les blocs if
	process(clock) -- s'execute chaque fois que clock change
	begin
	-- ...
	end process;
	
	-- instructions concurrentes ici
	-- ...
	
end archtecture behavorial
```

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity counter is
    port (
        clock    : in  std_logic;
        enable   : in  std_logic;
        reset    : in  std_logic;
        count    : out std_logic_vector(7 downto 0)
    );
end entity counter;

architecture behavioral of counter is
    -- Internal signals
    signal internal_count : unsigned(7 downto 0);
begin
    -- Sequential process for counting
    -- useful for doing if statements
    process(clock, reset) -- This process runs whenever 'clock' or 'reset' changes
    begin
        if reset = '1' then
            internal_count <= (others => '0');  -- Reset to zero
        elsif rising_edge(clock) then -- Check for rising clock edge
            if enable = '1' then
                internal_count <= internal_count + 1;
            end if;
        end if;
    end process;

    -- Concurrent statement (happens continously)
    count <= std_logic_vector(internal_count);  -- Convert to output type
end architecture behavioral;
```

### Entity declaration

ENTITY DECLARATION:

- An entity is like a "black box" that defines the interface of your circuit with the outside world - think of it as declaring what pins/connections your circuit will have
- A port is the list of all these input/output connections
- Inside a port, each line defines a signal with three parts:
    1. Signal name (like 'clk', 'data_in')
    2. Direction:
        - 'in' (input to your circuit)
        - 'out' (output from your circuit)
        - 'inout' (bidirectional)
        - 'buffer' (output that can be read internally)
    3. Data type:
        - std_logic: single bit ('0' or '1')
        - std_logic_vector: bus of bits
        - integer: numeric values
        - other custom types you can define

### Architecture block

ARCHITECTURE BLOCK:

1. Types of architectures:
    - 'behavioral': describes WHAT the circuit does (like software)
    - 'structural': describes HOW the circuit is built (connecting components)
    - 'dataflow': describes the flow of data using concurrent statements
2. Signals:
    - Internal wires in your circuit
    - Used for communication between processes
    - Declared before 'begin'

The 'begin' block:

- Contains the actual logic of your circuit
- Can contain both concurrent statements (happen continuously) and processes

The 'process' block:

- Used for sequential logic (like if-then statements)
- Has a sensitivity list in parentheses that determines when it runs
- Common for clocked logic (like registers, state machines)
