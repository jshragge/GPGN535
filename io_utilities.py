#!/usr/bin/env python
import numpy as np
import os

class Tinfile:
    """Set up TIN file class for LIDAR data
       Members:
           nx: # samples in x
           ny: # samples in y
           ox: origin in x
           oy: origin in y
           dx: sample interval in x
           dy: sample interval in y
           data: elevation data
           """
    nx=None
    ny=None
    dx=None
    dy=None
    ox=None
    oy=None
    data=None
    
    def __init__(self):
        self.data = []
        
def Read_In_TIN(myfile,verb=False):
    """Read in a TIN file and return a class
       Input: 
           file (string): the input path and file name 
           verb (logical;optional): be verbose
       Output:
           tin (class)"""
    
    tin = Tinfile()        

    with open(myfile, "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    
    tin.nx=int(array[0][5:])
    tin.ny=int(array[1][5:])
    tin.ox=float(array[2][10:])
    tin.oy=float(array[3][10:])    
    tin.dx=float(array[4][9:])
    tin.dy=float(array[4][9:])
    
    if(verb):
        print('Reading in TIN file %s'%(myfile))
        print('NX: %d'%(tin.nx))
        print('NY: %d'%(tin.ny))
        print('OX: %f'%(tin.ox))
        print('OY: %f'%(tin.oy))
        print('DX: %g'%(tin.dx))
        print('DY: %g'%(tin.dy))

    alldata = np.zeros((tin.nx,tin.ny));
    for ii in range(0,tin.ny):
        alldata[:,ii]=array[ii+6].split();

    tin.data = np.reshape(alldata,(tin.nx,tin.ny));
    return tin;