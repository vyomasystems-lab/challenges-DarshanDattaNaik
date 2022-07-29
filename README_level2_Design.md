# mkbitmanip co-processor Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/level1_design2/id%20verifcation.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed for the given mkbitmanip design. The environment contains test cases which exposes the bugs in the design.The test drives input to the Design Under Test (mkbitmanip.v module here) which takes 3 32-bit inputs 'mav_putvalue_src1','mav_putvalue_src2','mav_putvalue_src3'and one 32-bit instruction set input 'mav_putvalue_instr'. A python model file containing functionality of the design is imported in test envirnonment which is used to obtain expected values for diffrent instructions, The output obtained from given design is compared with the model output and verified accordingly.

The following required libraries are imported for developing the environment
```
import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

```

The clock is generated and the design is reset initially while testing each test case by using following code 
```
# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

```

# Test Scenario 1

The 

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

# Verification strategy
The strategy used is generating all possible values for required inputs using 'for loops' for a particular instruction set and checking the functionality to obtain combination of inputs which fail the design.

# Is the verification complete?
No the verification is not complete as the number of testcases that can be generated is very high there is a possibilty of presence of unnoticed bugs in the design








