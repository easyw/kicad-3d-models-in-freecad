# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script to generate connector models

## requirements
## freecad (v1.5 and v1.6 have been tested)
## cadquery FreeCAD plugin (v0.3.0 and v0.2.0 have been tested)
##   https://github.com/jmwright/cadquery-freecad-module

## This script can be run from within the cadquery module of freecad.
## To generate VRML/ STEP files for, use launch-cq-molex
## script of the parent directory.

#* This is a cadquery script for the generation of MCAD Models.             *
#*                                                                          *
#*   Copyright (c) 2016                                                     *
#* Rene Poeschl https://github.com/poeschlr                                 *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU General Public License (GPL)             *
#*   as published by the Free Software Foundation; either version 2 of      *
#*   the License, or (at your option) any later version.                    *
#*   for detail see the LICENCE text file.                                  *
#*                                                                          *
#*   This program is distributed in the hope that it will be useful,        *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
#*   GNU Library General Public License for more details.                   *
#*                                                                          *
#*   You should have received a copy of the GNU Library General Public      *
#*   License along with this program; if not, write to the Free Software    *
#*   Foundation, Inc.,                                                      *
#*   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           *
#*                                                                          *
#* The models generated with this script add the following exception:       *
#*   As a special exception, if you create a design which uses this symbol, *
#*   and embed this symbol or unaltered portions of this symbol into the    *
#*   design, this symbol does not by itself cause the resulting design to   *
#*   be covered by the GNU General Public License. This exception does not  *
#*   however invalidate any other reasons why the design itself might be    *
#*   covered by the GNU General Public License. If you modify this symbol,  *
#*   you may extend this exception to your version of the symbol, but you   *
#*   are not obligated to do so. If you do not wish to do so, delete this   *
#*   exception statement from your version.                                 *
#****************************************************************************

__title__ = "model description for Molex SlimStack 54722 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for Molex SlimStack 54722 series connectors using cadquery'

___ver___ = "0.2 04/12/2017"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Ray Benitez"
    STR_licEmail = "hackscribble@outlook.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################

import sys

if "module" in __name__ :
    for path in sys.path:
        if 'molex/cq_models':
            p1 = path.replace('molex/cq_models','_tools')
    if not p1 in sys.path:
        sys.path.append(p1)
else:
    sys.path.append('../_tools')

from ribbon import Ribbon


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD


class series_params():
    series = "SlimStack"
    series_long = 'SlimStack Fine-Pitch SMT Board-to-Board Connectors'
    manufacturer = 'Molex'
    orientation = 'V'
    number_of_rows = 2
    datasheet = 'http://www.molex.com/pdm_docs/sd/547220804_sd.pdf'
    mpn_format_string = "54722-0{pincount:02}4"
    mount_pin = ''


    #pins_per_row per row
    pinrange = [16,20,22,24,30,34,40,50,60,80]

    body_color_key = "white body"
    pins_color_key = "metal grey pins"
    color_keys = [
        body_color_key,
        pins_color_key
    ]
    obj_suffixes = [
        '__body',
        '__pins'
    ]


    pin_inside_distance = 1.05 + 0.5                # Distance between centre of end pin and end of body
    pocket_inside_distance = (10.1 - (8.95 + 0.5)) / 2.0     # Distance between end of pocket and end of body
    island_inside_distance = (10.1 - 8.0) / 2.0             # Distance between end of island and end of body

    pitch = 0.5

    body_width = 5.0
    body_height = 1.15
    body_fillet_radius = 0.15
    body_chamfer = 0.1
    pin_recess_height = 0.4

    pocket_width = 2.8
    pocket_base_thickness = 0.2
    pocket_fillet_radius = 0.05

    island_width = 1.65

    hole_width = 0.3
    hole_length = 0.3
    hole_offset = (body_width + pocket_width) / 4.0

    rib_width = 0.25
    rib_depth = 2.0 * body_chamfer

    slot_height = body_height - 0.05
    slot_depth = 0.3

    notch_width = 1.2
    notch_depth = 0.1

    pin_width = 0.15
    pin_thickness = 0.075
    pin_minimum_radius = 0.005 + pin_thickness / 2.0
    pin_y_offset = 0.5

    recess_breakpoint = 29                    # Above this number of pins, the body has housings on the side
    recess_width = 2.0
    recess_height = 0.575
    recess_depth = 0.05
    recess_pitch = 2.5


calcDim = namedtuple( 'calcDim', ['pin_group_width', 'length', 'pocket_length', 'island_length', 'rib_group_outer_width', 'slot_width', 'num_recesses', 'recess_offset'])


def dimensions(num_pins):
    pin_group_width = ((num_pins / 2) - 1) * series_params.pitch
    length =  pin_group_width + 2 * series_params.pin_inside_distance
    pocket_length = length - 2.0 * series_params.pocket_inside_distance
    island_length = length - 2.0 * series_params.island_inside_distance
    rib_group_outer_width = pin_group_width + series_params.pitch + series_params.rib_width
    slot_width = series_params.pitch - series_params.rib_width
    if num_pins > series_params.recess_breakpoint:
        num_recesses = num_pins // 10
        recess_offset = (num_pins % 10) * series_params.pitch / 4.0
    else:
        num_recesses = recess_offset = 0
    return calcDim(pin_group_width=pin_group_width, length = length, pocket_length=pocket_length,
                   island_length = island_length, rib_group_outer_width=rib_group_outer_width,
                   slot_width=slot_width, num_recesses=num_recesses, recess_offset=recess_offset)

def generate_contact(calc_dim):
    pin_group_width = calc_dim.pin_group_width
    pin_width = series_params.pin_width
    pin_thickness = series_params.pin_thickness
    pin_minimum_radius = series_params.pin_minimum_radius
    pitch = series_params.pitch
    pin_y_offset = series_params.pin_y_offset
    body_width = series_params.body_width
    hole_length = series_params.hole_length-0.02
    hole_offset = series_params.hole_offset
    slot_height = series_params.slot_height
    c1_list = [
        ('start', {'position': ((-body_width/2 - pin_y_offset, pin_thickness/2.0)), 'direction': 0.0, 'width':pin_thickness}),
        ('line', {'length': pin_y_offset}),
        ('arc', {'radius': pin_minimum_radius, 'angle': 60.0}),
        ('line', {'length': 0.05}),
        ('arc', {'radius': pin_minimum_radius, 'angle': -60.0}),
        ('line', {'length': 0.8}),
        ('arc', {'radius': pin_minimum_radius, 'angle': -45.0}),
        ('arc', {'radius': pin_minimum_radius, 'angle': 45.0}),
        ('line', {'length': 0.63}),
        ('arc', {'radius': 0.15, 'angle': 95.0}),
        ('line', {'length': 0.5}),
        ('arc', {'radius': 0.1, 'angle': 85.0})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0 - pin_group_width/2.0), c1_list)
    contact1 = ribbon.drawRibbon().extrude(pin_width)
    c2_list = [
        ('start', {'position': ((-hole_offset-hole_length/2.0+pin_thickness/2.0, slot_height-pin_minimum_radius-pin_thickness/2.0)), 'direction': 90.0, 'width':pin_thickness}),
        ('arc', {'radius': pin_minimum_radius, 'angle': -90.0}),
        ('line', {'length': hole_length-2.0*pin_minimum_radius-pin_thickness}),
        ('arc', {'radius': pin_minimum_radius, 'angle': -90.0}),
        ('line', {'length': slot_height - 0.32}),
        ('arc', {'radius': pin_minimum_radius, 'angle': 90.0}),
        ('line', {'length': 0.29}),
        ('arc', {'radius': 0.1, 'angle': 90.0}),
        ('line', {'length': 0.45}),
        ('arc', {'radius': 0.1, 'angle': -90.0})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0 - pin_group_width/2.0), c2_list)
    contact2 = ribbon.drawRibbon().extrude(pin_width)
    contact1 = contact1.union(contact2)
    return contact1


def generate_contacts(num_pins, calc_dim):
    pitch=series_params.pitch
    contact1 = generate_contact(calc_dim)
    contact2=contact1.mirror("XZ")
    contact_pair = contact1.union(contact2)
    contacts = contact_pair
    for i in range(0, num_pins / 2):
        contacts = contacts.union(contact_pair.translate((i*pitch,0,0)))
    return contacts



def my_rarray(self, xSpacing, ySpacing, xCount, yCount, center=True):
        """
        Local version of rarray() function to fix bug in handling of pitch values below 1.0

        Creates an array of points and pushes them onto the stack.
        If you want to position the array at another point, create another workplane
        that is shifted to the position you would like to use as a reference

        :param xSpacing: spacing between points in the x direction ( must be > 0)
        :param ySpacing: spacing between points in the y direction ( must be > 0)
        :param xCount: number of points ( > 0 )
        :param yCount: number of points ( > 0 )
        :param center: if true, the array will be centered at the center of the workplane. if
            false, the lower left corner will be at the center of the work plane
        """

        if xSpacing <= 0 or ySpacing <= 0 or xCount < 1 or yCount < 1:
            raise ValueError("Spacing and count must be > 0 ")

        lpoints = []  # coordinates relative to bottom left point
        for x in range(xCount):
            for y in range(yCount):
                lpoints.append((xSpacing * x, ySpacing * y))

        #shift points down and left relative to origin if requested
        if center:
            xc = xSpacing*(xCount-1) * 0.5
            yc = ySpacing*(yCount-1) * 0.5
            cpoints = []
            for p in lpoints:
                cpoints.append((p[0] - xc, p[1] - yc))
            lpoints = list(cpoints)

        return self.pushPoints(lpoints)


def generate_body(num_pins, calc_dim):

    body_length = calc_dim.length
    body_width = series_params.body_width
    body_height = series_params.body_height
    body_fillet_radius = series_params.body_fillet_radius
    body_chamfer = series_params.body_chamfer
    pin_recess_height = series_params.pin_recess_height

    pin_inside_distance = series_params.pin_inside_distance
    pitch = series_params.pitch

    pocket_inside_distance = series_params.pocket_inside_distance
    pocket_width = series_params.pocket_width
    pocket_base_thickness = series_params.pocket_base_thickness
    pocket_fillet_radius = series_params.pocket_fillet_radius

    island_inside_distance = series_params.island_inside_distance
    island_width = series_params.island_width

    hole_width = series_params.hole_width
    hole_length = series_params.hole_length
    hole_offset = series_params.hole_offset

    rib_group_outer_width = calc_dim.rib_group_outer_width
    rib_depth = series_params.rib_depth
    rib_width = series_params.rib_width

    slot_width = calc_dim.slot_width
    slot_height = series_params.slot_height
    slot_depth = series_params.slot_depth

    notch_width = series_params.notch_width
    notch_depth = series_params.notch_depth

    recess_height = series_params.recess_height
    recess_width = series_params.recess_width
    recess_depth = series_params.recess_depth
    num_recesses = calc_dim.num_recesses
    recess_offset = calc_dim.recess_offset
    recess_pitch = series_params.recess_pitch

    # body
    body = cq.Workplane("XY")\
        .rect(body_length, body_width).extrude(body_height)\
        .faces(">Z").edges("|Y").chamfer(body_chamfer)\
        .edges("|Z").fillet(body_fillet_radius)

    if num_recesses > 0:
        body = body.faces("<Y").workplane().center(-recess_offset, (body_height - recess_height)/2.0).rarray(recess_pitch, 1, num_recesses, 1).rect(recess_width, recess_height).cutBlind(-recess_depth)
        body = body.faces(">Y").workplane().center(recess_offset, (body_height - recess_height)/2.0).rarray(recess_pitch, 1, num_recesses, 1).rect(recess_width, recess_height).cutBlind(-recess_depth)

    cutter_A = cq.Workplane("XZ").workplane(offset=body_width/2.0).center(0, pin_recess_height/2.0).rect(body_length,pin_recess_height).extrude(-body_fillet_radius)
    cutter_B = cutter_A.mirror("XZ")
    body = body.cut(cutter_A).cut(cutter_B)

    pocket = cq.Workplane("XY").workplane(offset=body_height)\
        .rect(body_length - 2.0 * pocket_inside_distance, pocket_width)\
        .extrude(-(body_height - pocket_base_thickness)).edges("|Z").fillet(pocket_fillet_radius)

    body = body.cut(pocket)

    pocket_chamfer = cq.Workplane("XY").workplane(offset=body_height)\
        .rect(body_length - 2.0 * pocket_inside_distance + body_chamfer / 2.0, pocket_width + body_chamfer)\
        .workplane(offset=-body_chamfer).rect(body_length - 2.0 * pocket_inside_distance, pocket_width)\
        .loft(combine=True)

    body = body.cut(pocket_chamfer)

    island = cq.Workplane("XY").workplane(offset=body_height)\
        .rect(body_length - 2.0 * island_inside_distance, island_width)\
        .extrude(-(body_height - pocket_base_thickness)).edges("|Z").fillet(pocket_fillet_radius)

    body = body.union(island)

    # contact holes
    body = body.faces(">Z").workplane().center(0, hole_offset)

    body = my_rarray(body, pitch, 1, (num_pins/2), 1).rect(hole_width, hole_length)\
        .center(0, -2*hole_offset)

    body = my_rarray(body, pitch, 1, (num_pins/2), 1).rect(hole_width, hole_length)\
       .cutBlind(-2)

    # ribs recess
    body = body.faces(">Z").workplane().center(0, pocket_width / 2.0)\
        .rect(rib_group_outer_width, rib_depth/2)\
        .center(0, -pocket_width)\
        .rect(rib_group_outer_width, rib_depth/2)\
        .cutBlind(-(body_height))

    # ribs
    ribs = cq.Workplane("XY")

    ribs = my_rarray(ribs, pitch, pocket_width + body_chamfer, (num_pins/2)+1, 2).rect(rib_width,rib_depth).extrude(body_height)\
        .faces(">Z").edges("|X").fillet((rib_depth-0.001)/2.0)

    body = body.union(ribs)

    # slots for contacts
    slot_cutter = cq.Workplane("XY").center(-slot_width/2.0, (island_width / 2.0) - slot_depth)

    slot_cutter = my_rarray(slot_cutter, pitch, 1, num_pins/2, 1).rect(slot_width, slot_depth+(pocket_width-island_width)/2.0, centered=False).extrude(slot_height)\
       .center(0, -island_width-slot_depth)

    slot_cutter = my_rarray(slot_cutter, pitch, 1, num_pins/2, 1).rect(slot_width, slot_depth+(pocket_width-island_width)/2.0, centered=False).extrude(slot_height)

    body = body.cut(slot_cutter)

    # notches
    notch1 = cq.Workplane("XY").workplane(offset=body_height).moveTo(body_length/2.0, 0)\
        .rect(1, notch_width).extrude(-notch_depth).faces("<Z").edges("<Z").chamfer(notch_depth-0.001)

    notch2 = notch1.mirror("YZ")

    notches = notch1.union(notch2)

    body = body.cut(notches)

    return body


def generate_part(num_pins):
    calc_dim = dimensions(num_pins)
    body = generate_body(num_pins, calc_dim)
    contacts = generate_contacts(num_pins, calc_dim)
    return (body, contacts)


# opened from within freecad
if "module" in __name__:
    num_pins = 16
    # part_to_build = 'molex_54722_2x15'
    # part_to_build = 'molex_54722_2x17'
    # part_to_build = 'molex_54722_2x40'

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 str(num_pins) + "pins variant\n")
    (body, contacts) = generate_part(num_pins)

    show(body)
    show(contacts)
