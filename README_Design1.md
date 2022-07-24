# Mux_31to1 Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/initial%20tool.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed for the given mux design. The environment contains test cases which exposes the bugs in the design.The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit input 'sel', 31 2-bit inputs 'inp0' to 'inp30' and gives 1-bit output 'out' based on the 'sel' input.

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





