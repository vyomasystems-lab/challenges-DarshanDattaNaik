# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    #sequence-11011 
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'current state={int(dut.current_state.value)} seq_seen={dut.seq_seen.value} model current state={4} model seq_seen={1}')
    assert dut.seq_seen.value == 1,"The sequnce was not detected with current state={A} and seq_seen={B} expected current_state={C} and seq_seen={D}".format(A=int(dut.current_state.value),B=dut.seq_seen.value,C=4,D=0b1)

@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    #sequence-101011 
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value= 1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'current state={int(dut.current_state.value)} seq_seen={dut.seq_seen.value} model current state={4} model seq_seen={1}')
    assert dut.seq_seen.value == 1,"The sequnce was not detected with current state={A} and seq_seen={B} expected current_state={C} and seq_seen={D}".format(A=int(dut.current_state.value),B=dut.seq_seen.value,C=4,D=0b1)
