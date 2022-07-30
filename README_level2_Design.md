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

Test for AND+ operation 

```
    for j in range(1000):
       mav_putvalue_src1 = 0x10
       mav_putvalue_src2 = j
       mav_putvalue_src3 = 0x0
       mav_putvalue_instr = 0x00007033                #instruction for AND+ opeartion 

       # expected output from the model
       expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

       # driving the input transaction
       dut.mav_putvalue_src1.value = mav_putvalue_src1
       dut.mav_putvalue_src2.value = mav_putvalue_src2
       dut.mav_putvalue_src3.value = mav_putvalue_src3
       dut.EN_mav_putvalue.value = 1
       dut.mav_putvalue_instr.value = mav_putvalue_instr
  
       yield Timer(1) 

       # obtaining the output
       dut_output = dut.mav_putvalue.value
```

The following error is seen:

```
 assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x20 does not match MODEL = 0x0 with src1= 0x10  src2= 0x1  src3= 0x0
```

- Test Inputs: 'src1= 0x10'  'src2= 0x1'  'src3= 0x0' 'mav_putvalue_instr = 0x00007033'
- Expected Output: 'MODEL = 0x0'
- Observed Output in the DUT : 'DUT = 0x20'

The error indicates a bug in the AND+ logic of the DUT

# Test Scenario 2
Test for OR+ operation 

```
    for j in range(1000):
       mav_putvalue_src1 = 0xabcdabcd
       mav_putvalue_src2 = j
       mav_putvalue_src3 = 0x0
       mav_putvalue_instr = 0x00006033                #instruction for OR+ opeartion 

       # expected output from the model
       expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

       # driving the input transaction
       dut.mav_putvalue_src1.value = mav_putvalue_src1
       dut.mav_putvalue_src2.value = mav_putvalue_src2
       dut.mav_putvalue_src3.value = mav_putvalue_src3
       dut.EN_mav_putvalue.value = 1
       dut.mav_putvalue_instr.value = mav_putvalue_instr
  
       yield Timer(1) 

       # obtaining the output
       dut_output = dut.mav_putvalue.value

```

The following error is seen:

```
 assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x1579b579a does not match MODEL = 0x0 with src1= 0xabcdabcd  src2= 0x1  src3= 0x0
```

- Test Inputs: 'src1= 0xabcdabcd'  'src2= 0x1'  'src3= 0x0' 'mav_putvalue_instr = 0x00006033'
- Expected Output: 'MODEL = 0x0'
- Observed Output in the DUT :  'DUT = 0x1579b579a'

The error indicates a bug in the OR+ logic of the DUT

# Test Scenario 3
Test for XOR+ operation 

```
for j in range(1000):
       mav_putvalue_src1 = 0xffff
       mav_putvalue_src2 = j
       mav_putvalue_src3 = 0x10
       mav_putvalue_instr = 0x00004033                #instruction for XOR+ opeartion 

       # expected output from the model
       expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

       # driving the input transaction
       dut.mav_putvalue_src1.value = mav_putvalue_src1
       dut.mav_putvalue_src2.value = mav_putvalue_src2
       dut.mav_putvalue_src3.value = mav_putvalue_src3
       dut.EN_mav_putvalue.value = 1
       dut.mav_putvalue_instr.value = mav_putvalue_instr
  
       yield Timer(1) 

       # obtaining the output
       dut_output = dut.mav_putvalue.value

```

The following error is seen:

```
 assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x20 does not match MODEL = 0x0 with src1= 0xffff  src2= 0x0  src3= 0x10
```

- Test Inputs: 'src1= 0xffff'  'src2= 0x0'  'src3= 0x10' 'mav_putvalue_instr = 0x00004033'
- Expected Output: 'MODEL = 0x0'
- Observed Output in the DUT :  ' DUT = 0x20 '

The error indicates a bug in the XOR+ logic of the DUT

# Test Scenario 4
Test for ANDN operation 

```
for j in range(1,1000):
       mav_putvalue_src1 = 0xaaaa
       mav_putvalue_src2 = j
       mav_putvalue_src3 = 0x101
       mav_putvalue_instr = 0x40007033                #instruction for ANDN opeartion 

       # expected output from the model
       expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

       # driving the input transaction
       dut.mav_putvalue_src1.value = mav_putvalue_src1
       dut.mav_putvalue_src2.value = mav_putvalue_src2
       dut.mav_putvalue_src3.value = mav_putvalue_src3
       dut.EN_mav_putvalue.value = 1
       dut.mav_putvalue_instr.value = mav_putvalue_instr
  
       yield Timer(1) 

       # obtaining the output
       dut_output = dut.mav_putvalue.value

```

The following error is seen:

```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x1 does not match MODEL = 0x15555 with src1= 0xaaaa  src2= 0x1  src3= 0x101
```

- Test Inputs: 'src1= 0xaaaa'  'src2= 0x1'  'src3= 0x101' 'mav_putvalue_instr = 0x40007033'
- Expected Output: 'MODEL = 0x15555'
- Observed Output in the DUT :  ' DUT = 0x1 '

The error indicates a bug in the ANDN logic of the DUT

# Test Scenario 5
Test for SLL+ operation 

```
for j in range(0,1000):
       mav_putvalue_src1 = j
       mav_putvalue_src2 = 0x10101010
       mav_putvalue_src3 = 0x01010101
       mav_putvalue_instr = 0x00001033                #instruction for SLL+ opeartion 

       # expected output from the model
       expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

       # driving the input transaction
       dut.mav_putvalue_src1.value = mav_putvalue_src1
       dut.mav_putvalue_src2.value = mav_putvalue_src2
       dut.mav_putvalue_src3.value = mav_putvalue_src3
       dut.EN_mav_putvalue.value = 1
       dut.mav_putvalue_instr.value = mav_putvalue_instr
  
       yield Timer(1) 

       # obtaining the output
       dut_output = dut.mav_putvalue.value
```

The following error is seen:

```
 assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x2 does not match MODEL = 0x0 with src1= 0x1  src2= 0x10101010  src3= 0x1010101
```

- Test Inputs: 'src1= 0x1'  'src2= 0x10101010'  'src3= 0x1010101' 'mav_putvalue_instr = 0x00001033'
- Expected Output: 'MODEL = 0x0'
- Observed Output in the DUT :  ' DUT = 0x2 '

The error indicates a bug in the SLL+ logic of the DUT

# Verification strategy
The strategy used is generating all possible values for required inputs using 'for loops' for a particular instruction set and checking the functionality to obtain combination of inputs which fail the design.

# Is the verification complete?
No the verification is not complete as the number of testcases that can be generated is very high there is a possibilty of presence of unnoticed bugs in the design








