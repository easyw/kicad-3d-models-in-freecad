

import FreeCAD, Draft, FreeCADGui, ImportGui

Gui.activateWorkbench("CadQueryWorkbench")

import FreeCADGui as Gui

from cq_cad_tools import close_CQ_Example

close_CQ_Example(App, Gui)

import cadquery as cq
from fc_tools import *

from Helpers import show

doc = FreeCAD.newDocument("test")
App.setActiveDocument("test")
Gui.ActiveDocument = Gui.getDocument("test")

from collections import namedtuple

Params = namedtuple("Params", [
    
    'p', # pitch (separaration between pins)
    'c', # chamfering of plastic base
    'h', # height of plastic base above board
    'pw', #pin width
    'pt', #tip width
    'pa', #pin height above board
    'ph', #pin height total
])

headers = {
    '254': Params(
        p = 2.54,
        c = 0.254,
        h = 2.54,
        pw = 0.64,
        pt = 0.3,
        pa = 8.5,
        ph = 11.5
    )
}

def MakeBaseRow(n, params):
    
    f = 0.99999
    
    base = cq.Workplane("XY").rarray(params.p,1,n,1,center=False).rect(params.p*f,params.p*f).extrude(params.h)
    base = base.edges("Z").chamfer(params.c)
    base = base.faces("<Z").rarray(params.p,1,n,1,center=False).rect(params.pw+0.01,params.pw+0.01).cutThruAll()
    
    return base

#make a pin header
def MakeBase(n, params, rows=1):

    base = MakeBaseRow(n,params)
    
    for i in range(1,rows):
        base = base.union(MakeBaseRow(n,params).translate((0,params.p,0)))
    
    return base
    
def MakePinRow(n, params):
    #make some pins
    pins = cq.Workplane("XY").workplane(offset=params.pa-params.ph).rarray(params.p,1,n,1,center=False).rect(params.pw,params.pw)
    pins = pins.extrude(params.ph)
    
    return pins
    
def MakePins(n, params, rows=1):
    pins = MakePinRow(n,params)
    
    for i in range(1,rows):
        pins = pins.union(MakePinRow(n,params).translate((0,params.p,0)))
        
    return pins
    
pins = MakePins(8, headers['254'],rows=3)
base = MakeBase(8, headers['254'],rows=3)

show(pins)
show(base)