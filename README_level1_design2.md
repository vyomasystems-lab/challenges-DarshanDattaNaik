# SEQ_1011 Detector Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/initial%20tool.png)

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

```

- Test Inputs: 'sel=01100'  'inp12=10'  
- Expected Output: out=10
- Observed Output in the DUT dut.out=00

'Zero' is obtained as output instead of 'inp12' as output indicating bug in the design

# Test Scenario 2

The values are assigned to the input ports using

```
      s = 0b01101
      i12 = 0b10
      i13 = 0b11
      dut.sel.value = s
      dut.inp12.value = i12
      dut.inp13.value = i13
```

The following error is seen:

```
 assert dut.out.value == i13, "Randomised test failed with: inp{A}={B}, sel={S} with obtained output={M} not equal expected output={E}".format(
                     AssertionError: Randomised test failed with: inp13=11, sel=01101 with obtained output=10 not equal expected output=11
```

- Test Inputs: 'sel=01101'  'inp12=10'  'inp13=11'
- Expected Output: out=11
- Observed Output in the DUT dut.out=10

'inp12' is obtained as output instead of obtaining 'inp13' as output indicating a bug in the design

# Test Scenario 3

The following values are assigned to the input port 

```
    s = 30
    i= 0b11
    dut.sel.value = s
    dut.inp30.value = i
    await Timer(2, units='ns')
```

The following error is seen:

```
assert dut.out.value == i, "Randomised test failed with: inp{A}={B}, sel={S} with obtained output={M} not equal expected output={E}".format(
                     AssertionError: Randomised test failed with: inp30=11, sel=11110 with obtained output=00 not equal expected output=11
```

- Test Inputs: 'sel=11110'  'inp30=11'  
- Expected Output: out=11
- Observed Output in the DUT dut.out=00

'Zero' is obtained as output instead of 'inp30' as output indicating bug in the design

# Design Bug

Based on the above test input and analysing the design, we see the following

```
begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;             ========> BUG1
      5'b01101: out = inp13;             ========> BUG2
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;             ======> BUG3
      default: out = 0;
```

BUG1: output for testcase sel=5'b01100 is not defined 

BUG2: two different inputs are selected as output for same sel=5'b01101

BUG3: output for testcase sel=5'b11110 is not defined

# Design Fix
Updating the design and re-running the test makes the test pass.
![fixed design output](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/Design1_passed_test.png)

The updated design is checked in as mux_fix.v

# Verification strategy

# Is the verification complete?








