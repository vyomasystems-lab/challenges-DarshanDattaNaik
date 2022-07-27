# SEQ_1011 Detector Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/initial%20tool.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed for the given Sequence detector design. The environment contains test cases which exposes the bugs in the design.The test drives inputs to the Design Under Test (seq module here) which takes in 5-bit input 'sel', 31 2-bit inputs 'inp0' to 'inp30' and gives 1-bit output 'out' based on the 'sel' input.

# Test Scenario 1

The following values are assigned to the input port 

```
    s = 0b01100
    i = 0b10
    dut.sel.value = s
    dut.inp12.value = i
```

The following error is seen:

```
                         assert dut.out.value == i, "Randomised test failed with: inp{A}={B}, sel={S} with obtained output={M} not equal expected output={E}".format(
                     AssertionError: Randomised test failed with: inp12=10, sel=01100 with obtained output=00 not equal expected output=10
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








