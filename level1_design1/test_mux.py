# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    s = 0b01010
    i10 = 0b1
    i13 = 0b0

    dut.sel.value = s
    dut.inp10.value = i10
    dut.inp13.value = i13

    await Timer(2, units='ns')
    assert dut.out.value == i13, f"mux result is incorrect: {dut.out.value} !=inp13"

     
    cocotb.log.info('##### CTB: Develop your test here ########')
