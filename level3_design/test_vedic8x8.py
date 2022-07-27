import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test1_mux(dut):
    """Test for mux2"""
    A = 20
    B = 255
    dut.a.value = A
    dut.b.value = B
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={A*B} DUT={int(dut.p.value)}')
    assert dut.p.value == A*B, "Randomised test failed with: a={A} and a={B} and product p!={P}"#.format(
    #A=s, B=dut.inp12.value, S=dut.sel.value,M=dut.out.value,E=dut.inp12.value)