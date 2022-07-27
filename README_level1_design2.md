# SEQ_1011 Detector Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/level1_design2/id%20verifcation.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed for the given Sequence detector design. The environment contains test cases which exposes the bugs in the design.The test drives input sequence to the Design Under Test (seq_detect_1011 module here) which takes a one bit input 'input_bit' in each clock cycle and moves to different states based on the inputs detected. The test detects whether the 'output_seen' and the 'current_state' values match expected values for a given input sequence

The following required libraries are imported for developing the environment
```
import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
```

The clock is generated and the sequence detector is reset initially while testing each test case by using following code 
```
 clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

```

# Test Scenario 1

The sequence 11011 is fed as input to the detector using the below code

```
     #sequence-11011 
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
```

The following error is seen:

```
assert dut.seq_seen.value == 1,"The sequnce was not detected with current state={A} and seq_seen={B} expected current_state={C} and seq_seen={D}".format(A=int(dut.current_state.value),B=dut.seq_seen.value,C=4,D=0b1)
                     AssertionError: The sequnce was not detected with current state=0 and seq_seen=0 expected current_state=4 and seq_seen=1
```

- Test Inputs: 'input sequence=11011'  
- Expected Output: 'current_state = 4' 'seq_seen=1'
- Observed Output in the DUT : 'current state=0' 'seq_seen=0'

The sequence is not detected indicating bug in the design

# Test Scenario 2

The sequence 1011011 is fed as input to the detector using the below code

```
#sequence-1011011
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
```

The following error is seen:

```
 assert dut.seq_seen.value == 1,"The sequnce was not detected with current state={A} and seq_seen={B} expected current_state={C} and seq_seen={D}".format(A=int(dut.current_state.value),B=dut.seq_seen.value,C=4,D=0b1)
                     AssertionError: The sequnce was not detected with current state=0 and seq_seen=0 expected current_state=4 and seq_seen=1
```
- Test Inputs: 'input sequence=1011011'  
- Expected Output: 'current_state = 4' 'seq_seen=1'
- Observed Output in the DUT : 'current state=0' 'seq_seen=0'

The sequence is not detected indicating bug in the design

# Test Scenario 3

The sequence 101011 is fed as input to the detector using the below code

```
#sequence-101011
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
```

The following error is seen:

```
assert dut.seq_seen.value == 1,"The sequnce was not detected with current state={A} and seq_seen={B} expected current_state={C} and seq_seen={D}".format(A=int(dut.current_state.value),B=dut.seq_seen.value,C=4,D=0b1)
                     AssertionError: The sequnce was not detected with current state=0 and seq_seen=0 expected current_state=4 and seq_seen=1
```
- Test Inputs: 'input sequence=101011'  
- Expected Output: 'current_state = 4' 'seq_seen=1'
- Observed Output in the DUT : 'current state=0' 'seq_seen=0'

The sequence is not detected indicating bug in the design

# Design Bug

Based on the above test input and analysing the design, we see the following

```
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;                   =====> BUG1
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;                  ========> BUG2   
      end
      SEQ_1011:
      begin
        next_state = IDLE;                    =========> BUG3
      end
    endcase
  end
endmodule
```

BUG1: The 'next_state' should be assigned as 'SEQ_1' and not 'IDLE' if present state is 'SEQ_1' and 1 is detected  

BUG2: The 'next_state' should be assigned as 'SEQ_10' and not 'IDLE' if present state is 'SEQ_101' and 0 is detected

BUG3: The 'next_state' should be assigned as 'SEQ_1 if 1 is detected' or 'SEQ_10 if 0 is detected'  not 'IDLE' if present state is 'SEQ_1011' 

# Design Fix
Updating the design and re-running the test makes the test pass.
![fixed design output](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/level1_design2/level1_design2_testpassed.png)

The updated design is checked in as seq_detect_1011_fixed.v

# Verification strategy

# Is the verification complete?








