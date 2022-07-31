# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

#AND+ 1 TEST
@cocotb.test()
def run_test_AND(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message


#OR+ 2 Test
@cocotb.test()
def run_test_OR(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message


#XOR+ 3 Test
@cocotb.test()
def run_test_XOR(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message


#ANDN-4 Test
@cocotb.test()
def run_test_ANDN(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message

#ORN-5 Test
@cocotb.test()
def run_test_ORN(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
    for j in range(1,1000):
       mav_putvalue_src1 = 0x10101010
       mav_putvalue_src2 = j
       mav_putvalue_src3 = 0xaaaaaaaa
       mav_putvalue_instr = 0x40006033                #instruction for ORN opeartion 

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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message


#XNOR-6 Test
@cocotb.test()
def run_test_XNOR(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
    for j in range(0,1000):
       mav_putvalue_src1 = j
       mav_putvalue_src2 = 0x10101010
       mav_putvalue_src3 = 0x01010101
       mav_putvalue_instr = 0x40004033                #instruction for XNOR opeartion 

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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message

#SLL+ 7 Test
@cocotb.test()
def run_test_SLL(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message

#SRL+ 8 Test
@cocotb.test()
def run_test_SRL(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    #for i in range((2**32)-1):
    
    for j in range(0,1000):
       mav_putvalue_src1 = j
       mav_putvalue_src2 = 0x10101010
       mav_putvalue_src3 = 0x01010101
       mav_putvalue_instr = 0x00005033                #instruction for SRL+ opeartion 

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

       cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
       cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
       # comparison
       error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} with src1= {hex(dut.mav_putvalue_src1.value)}  src2= {hex(dut.mav_putvalue_src2.value)}  src3= {hex(dut.mav_putvalue_src3.value)}'
       assert dut_output == expected_mav_putvalue, error_message
 
