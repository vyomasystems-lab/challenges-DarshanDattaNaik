# Mux_31to1 Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![Gitpod Id verification](https://github.com/vyomasystems-lab/challenges-DarshanDattaNaik/blob/master/initial%20tool.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed for the given mux design. The environment contains test cases which exposes the bugs in the design.The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit input 'sel', 31 2-bit inputs 'inp0' to 'inp30' and gives 1-bit output 'out' based on the 'sel' input.

# Test Scenario 1
The values are assigned to the input port using

```
      s = 13
      i12 = 0b10
      i13 = 0b11
      dut.sel.value = s
      dut.inp12.value = i12
      dut.inp13.value = i13
```




