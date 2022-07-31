# 8x8 Vedic Multiplier Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/initial%20tool.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed for the given mux design. The environment contains test cases which exposes the bugs in the design.The test drives inputs to the Design Under Test (vedic8x8 module here) which takes in 8-bit inputs 'a' and 'b' and gives 16-bit output 'p'.The test cases are developed to verify the product.Test cases are developed to verify smaller modules present in the DUT to identify the exact location of the bug in the design.

The following required libraries are imported in the environment
```
import cocotb
from cocotb.triggers import Timer
import random
```

The required binary_to_decimal and decimal_to_binary functions are defined as follows
```
def btd(val):
    return int(val,2)
def dtb(val):
    return bin(val)
```
# Test Scenario 1

The following values are assigned to 'a' and 'b' 

```
       A = random.randint(0,255)
       B = random.randint(0,255)
       dut.a.value = A
       dut.b.value = B
```

The following error is seen:

```
 assert dut.p.value == A*B, "Randomised test failed with: a={A} and b={B} and product p!={P} DUT={Q}".format(
                     AssertionError: Randomised test failed with: a=67 and b=132 and product p!=8844 DUT=8588
```

- Test Inputs:  'a=67' 'b=132'
- Expected Output: p=8844
- Observed Output in the DUT: DUT=8588

The test fails indicating bug in the design

# Test Scenario 2

Test for Vedic4x4_A module present DUT

```
 #Test for Vedic_4x4_A module
    """Test for a[3:0]*b[3:0} """
    
    A = 0xaa
    B = 0xff
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(A)[-4:])*btd(dtb(B)[-4:])
    assert dut.m.value == c , "Randomised test failed with: a={A} and b={B} and  m={P} not equal to expected value m={Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.m.value))
```

The following error is seen:

```
assert dut.m.value == c , "Randomised test failed with: a={A} and b={B} and  m={P} not equal to expected value m={Q}".format(
                     AssertionError: Randomised test failed with: a=10101010 and b=11111111 and  m=175 not equal to expected value m=150
```

- Test Inputs: 'a=10101010' 'b=11111111'
- Expected Output: m=150
- Observed Output in the DUT: DUT=175

Failed test indicates presence of bug in Vedic4x4_A module

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
![fixed design output](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/level1_design1/Design1_passed_test.png)

The updated design is checked in as mux_fix.v

# Verification strategy
The verification startegy used here is based on
i) only one input should be selected for one unique combination of 'sel'
ii) verifying the output for all different possible combinations of 'sel'


# Is the verification complete?
Yes, the verification is complete and the design is fixed
Note: When sel=5'b11111 the ouput would be set to default zero (This value of sel can be used to reset the mux output)







