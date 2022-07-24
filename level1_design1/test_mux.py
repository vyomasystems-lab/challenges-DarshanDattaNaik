# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test1_mux(dut):
    """Test for mux2"""
    s = 12
    i = 0b10
    dut.sel.value = s
    dut.inp12.value = i
    await Timer(2, units='ns')
    
    dut.log.info(f'sel={dut.sel.value} inp{s}={dut.inp12.value} model={dut.inp12.value} DUT={dut.out.value}')
    assert dut.out.value == i, "Randomised test failed with: inp{A}={B}, sel={S} with obtained output={M} not equal expected output={E}".format(
    A=s, B=dut.inp12.value, S=dut.sel.value,M=dut.out.value,E=dut.inp12.value)

@cocotb.test()
async def test2_mux(dut):
    """Test for mux2"""
    s = 13
    i12 = 0b10
    i13 = 0b11
    dut.sel.value = s
    dut.inp12.value = i12
    dut.inp13.value = i13
    await Timer(2, units='ns')
    
    dut.log.info(f'sel={dut.sel.value} inp{s}={dut.inp13.value} model={dut.inp13.value} DUT={dut.out.value}')
    assert dut.out.value == i13, "Randomised test failed with: inp{A}={B}, sel={S} with obtained output={M} not equal expected output={E}".format(
    A=s, B=dut.inp13.value, S=dut.sel.value,M=dut.out.value,E=dut.inp13.value)

@cocotb.test()
async def test3_mux(dut):
    """Test for mux2"""
    s = 30
    i= 0b11
    dut.sel.value = s
    dut.inp30.value = i
    await Timer(2, units='ns')
    
    dut.log.info(f'sel={dut.sel.value} inp{s}={dut.inp30.value} model={dut.inp30.value} DUT={dut.out.value}')
    assert dut.out.value == i, "Randomised test failed with: inp{A}={B}, sel={S} with obtained output={M} not equal expected output={E}".format(
    A=s, B=dut.inp30.value, S=dut.sel.value,M=dut.out.value,E=dut.inp30.value)