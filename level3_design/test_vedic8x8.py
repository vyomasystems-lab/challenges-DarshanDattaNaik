import cocotb
from cocotb.triggers import Timer
import random

def btd(val):
    return int(val,2)
def dtb(val):
    return bin(val)

@cocotb.test()
async def test_multiplier(dut):
    """Test for multiplication"""
    for i in range(10):
       A = random.randint(0,255)
       B = random.randint(0,255)
       dut.a.value = A
       dut.b.value = B
       await Timer(2, units='ns')
    
       dut.log.info(f'a={A} b={B} model={A*B} DUT={int(dut.p.value)}')
       assert dut.p.value == A*B, "Randomised test failed with: a={A} and a={B} and product p!={P}"#.format(
       #A=s, B=dut.inp12.value, S=dut.sel.value,M=dut.out.value,E=dut.inp12.value)      

@cocotb.test()
async def test_multiplier1(dut):
    """Test for a[3:0]*b[3:0} """
    
    A = 0x0f
    B = 0x0f
    dut.a.value = A
    dut.b.value = B
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={A*B} DUT={int(dut.m.value)}')
    assert dut.m.value == A*B , "Randomised test failed with: a={A} and b={B} and  m={P} not equal to expected value m={Q}".format(
    A=dut.a.value, B=dut.b.value, Q=A*B,P=dut.m.value)      

@cocotb.test()
async def test_multiplier2(dut):
    """Test for a[7:4]*b[3:0} """
    
    A = 0xf0
    B = 0x0f
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(A)[2:6])*btd(dtb(B)[-4:])
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={c} DUT={int(dut.n.value)}')
    assert dut.n.value == c , "Randomised test failed with: a={A} and b={B} and  n={P} not equal to expected value n={Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=dut.n.value)

@cocotb.test()
async def test_multiplier3(dut):
    """Test for a[3:0]*b[7:4] """
    
    A = 0x0f
    B = 0xf0
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[2:6])*btd(dtb(A)[-4:])
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={c} DUT={int(dut.o.value)}')
    assert dut.o.value == c , "Randomised test failed with: a={A} and b={B} and  o={P} not equal to expected value o={Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=dut.o.value)

@cocotb.test()
async def test_multiplier4(dut):
    """Test for a[7:4]*b[7:4] """
    
    A = 0xf0
    B = 0xf0
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[2:6])*btd(dtb(A)[2:6])
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={c} DUT={int(dut.q.value)}')
    assert dut.q.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=dut.q.value)

# TEST FOR ALL VEDIC4x4 MODULES

@cocotb.test()
async def test_multiplier1_1(dut):
    """Test for a[1:0]*b[1:0] """
    
    A = 0b00000011
    B = 0b00000011
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(B)[-2:])*btd(dtb(A)[-2:])
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={c} DUT={int(dut.A.m.value)}')
    assert dut.A.m.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=dut.A.m.value)


@cocotb.test()
async def test_multiplier1_2(dut):
    """Test for a[1:0]*b[1:0] """
    
    A = 0b00001100
    B = 0b00000011
    dut.a.value = A
    dut.b.value = B
    c=btd(dtb(A)[6:8])*btd(dtb(B)[-2:])
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={c} DUT={int(dut.A.m.value)}')
    assert dut.A.m.value == c , "Randomised test failed with: a={A} and b={B} and  DUT={P} not equal to expected output {Q}".format(
    A=dut.a.value, B=dut.b.value, Q=c,P=dut.A.m.value)