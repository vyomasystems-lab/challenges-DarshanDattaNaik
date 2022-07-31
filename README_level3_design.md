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

Test for Vedic4x4_A module present in DUT

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

Test for Vedic4x4_B module present in DUT

```
#Test for Vedic_4x4_B module
    """Test for a[7:4]*b[3:0} """
    
    A = 0xaa
    B = 0xbb
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(A)[2:6])*btd(dtb(B)[-4:])
    assert dut.n.value == c , "Randomised test failed with: a={A} and b={B} and  n={P} not equal to expected value n={Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.n.value))

```

The following error is seen:

```
assert dut.n.value == c , "Randomised test failed with: a={A} and b={B} and  n={P} not equal to expected value n={Q}".format(
                     AssertionError: Randomised test failed with: a=10101010 and b=10111011 and  n=115 not equal to expected value n=110
```

- Test Inputs: 'a=10101010' 'b=10111011'
- Expected Output: n=110
- Observed Output in the DUT: DUT=115

Failed test indicates presence of bug in Vedic4x4_B module

# Test Scenario 4

Test for Vedic4x4_C module present in DUT

```
 #Test for Vedic_4x4_C module
    """Test for a[3:0]*b[7:4] """
    
    A = 0x99
    B = 0x99
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[2:6])*btd(dtb(A)[-4:])
    assert dut.o.value == c , "Randomised test failed with: a={A} and b={B} and  o={P} not equal to expected value o={Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.o.value))

```

The following error is seen:

```
assert dut.o.value == c , "Randomised test failed with: a={A} and b={B} and  o={P} not equal to expected value o={Q}".format(
                     AssertionError: Randomised test failed with: a=10011001 and b=10011001 and  o=84 not equal to expected value o=81
```

- Test Inputs: 'a=10011001' 'b=10011001'
- Expected Output: o=81
- Observed Output in the DUT: DUT=84

Failed test indicates presence of bug in Vedic4x4_C module

# Test Scenario 5

Test for Vedic4x4_D module present in DUT

```
  #Test for Vedic_4x4_D module
    """Test for a[7:4]*b[7:4] """
    
    A = 0xaf
    B = 0xcf
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[2:6])*btd(dtb(A)[2:6])
    assert dut.q.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.q.value))
```

The following error is seen:

```
 assert dut.q.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
                     AssertionError: Randomised test failed with: a=10101111 and b=11001111 and  DUT=140 not equal to expected output 120
```

- Test Inputs: 'a=10101111' 'b=11001111'
- Expected Output: q=120
- Observed Output in the DUT: DUT=140

Failed test indicates presence of bug in Vedic4x4_D module

All four vedic4x4 modules present in vedic8x8 failed the tests indicating bugs in lower level modules of vedic4x4.

# Test Scenario 6

Test for Vedic2x2_A module present in Vedic4x4_A module

```
#Test for Vedic_2x2_A module
    """Test for a[1:0]*b[1:0] """
    
    A = 0xc9
    B = 0xc9
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[-2:])*btd(dtb(A)[-2:])
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={c} DUT={int(dut.A.m.value)}')
    assert dut.A.m.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.A.m.value))


```

The following error is seen:

```
assert dut.A.m.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
                     AssertionError: Randomised test failed with: a=11001001 and b=11001001 and  DUT=0 not equal to expected output 1
```

- Test Inputs: 'a=11001001' 'b=11001001'
- Expected Output: m=1
- Observed Output in the DUT: DUT=0

Failed test indicates presence of bug in Vedic2x2_A module

# Test Scenario 7

Test for Vedic2x2_B module present in Vedic4x4_A module

```
 #Test for Vedic_2x2_B module
    """Test for a[3:2]*b[1:0] """
    
    A = 0xa5
    B = 0xd3
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(A)[-4:-2])*btd(dtb(B)[-2:])
    assert dut.A.n.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.A.n.value))

```

The following error is seen:

```
 assert dut.A.n.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
                     AssertionError: Randomised test failed with: a=10100101 and b=11010011 and  DUT=2 not equal to expected output 3
```

- Test Inputs: 'a=10100101' 'b=11010011'
- Expected Output: n=3
- Observed Output in the DUT: DUT=2

Failed test indicates presence of bug in Vedic2x2_B module


# Test Scenario 8

Test for Vedic2x2_C module present in Vedic4x4_A module

```
 #Test for Vedic_2x2_C module
    """Test for a[1:0]*b[3:2] """
    
    A = 0xc1
    B = 0xac
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[-4:-2])*btd(dtb(A)[-2:])
    assert dut.A.o.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.A.o.value))

```

The following error is seen:

```
assert dut.A.o.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
                     AssertionError: Randomised test failed with: a=11000001 and b=10101100 and  DUT=2 not equal to expected output 3
```

- Test Inputs: 'a=11000001' 'b=10101100'
- Expected Output: o=3
- Observed Output in the DUT: DUT=2

Failed test indicates presence of bug in Vedic2x2_C module

# Test Scenario 9

Test for Vedic2x2_D module present in Vedic4x4_A module

```
 #Test for Vedic_2x2_D module
    """Test for a[3:2]*b[3:2] """
    
    A = 0xaa
    B = 0xbf
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[-4:-2])*btd(dtb(A)[-4:-2])
    assert dut.A.q.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=int(dut.A.q.value))

```

The following error is seen:

```
 assert dut.A.q.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
                     AssertionError: Randomised test failed with: a=10101010 and b=10111111 and  DUT=7 not equal to expected output 6
```

- Test Inputs: 'a=10101010' 'b=10111111'
- Expected Output: q=6
- Observed Output in the DUT: DUT=7

Failed test indicates presence of bug in Vedic2x2_D module

# Test Scenario 10

Test for Vedic2x2_basic module 

```
    A = 2
    B = 3
    dut.A.A.a.value = A
    dut.A.A.b.value = B
    assert dut.A.A.p.value == A*B , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.A.A.a.value, B=dut.A.A.b.value, Q=A*B,P=int(dut.A.A.p.value))
```

The following error is seen:

```
  assert dut.A.A.p.value == A*B , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
                     AssertionError: Randomised test failed with: a=10 and b=11 and  DUT=7 not equal to expected output 6
```

- Test Inputs: 'a=0b10' 'b=0b11'
- Expected Output: p=6
- Observed Output in the DUT: DUT=7

Failed test indicates presence of bug in lower Vedic2x2 module 

# Design Bug

Based on the above test input and analysing the design, we see the following

```
module vedic2x2(a,b,p);
input [1:0] a,b;
output [3:0] p;
wire [3:0] w;
assign p[0]= a[1]&b[0];             ===> BUG
assign w[0]=a[1]&b[0];
assign w[1]=a[0]&b[1];
assign w[2]=a[1]&b[1];
half_adder A(w[0],w[1],p[1],w[3]);
half_adder B(w[2],w[3],p[2],p[3]);
endmodule
```

BUG1: The product of a[1]&b[0] is assigned to p[0], it should be modified to p[0]=a[0]&b[0]

# Design Fix
Updating the design and re-running the test makes the test pass.
![fixed design output](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/level1_design1/Design1_passed_test.png)

The updated design is checked in as vedic8x8_fix.v

# Verification strategy
The verification startegy used here is 
-1. checking the outputs of all vedic4x4 modules present in the vedic8x8 one by one.
-2. based on the errors obtained in step(1) all the individual vedic2x2 modules within one vedic4x4 module are checked
-3. based on the errors obtained in step(2) the functionality vedic2x2 module is verfied
-4. The vedic2x2 module gives error indicating presence of bug in it.


# Is the verification complete?
Yes, the verification is complete and the design is fixed
The outputs are verfied for all possible inputs of 'a' and 'b'






