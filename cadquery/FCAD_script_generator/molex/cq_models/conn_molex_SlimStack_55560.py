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

__title__ = "model description for Molex SlimStack 55560 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for Molex SlimStack 55560 series connectors using cadquery'

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

lock_positions = {
    16: ['all'],
    20: ['all'],
    22: ['all'],
    24: ['all'],
    30: ['all'],
    34: [2,3,4,5,7,8,9,10,11,13,14,15,16],
    40: [2,3,5,6,8,9,12,13,15,16,18,19],
    46: [2,4,8,10,14,16,20,22],
    50: [2,4,8,10,16,18,22,24],
    60: [10,21],
    80: ['none']
}

class series_params():
    series = "SlimStack"
    series_long = 'SlimStack Fine-Pitch SMT Board-to-Board Connectors'
    manufacturer = 'Molex'
    orientation = 'V'
    number_of_rows = 2
    datasheet = 'http://www.molex.com/pdm_docs/sd/555600207_sd.pdf'
    mpn_format_string = "55560-0{pincount:02}1"
    mount_pin = ''

    body_color_key = "dark grey body"
    pins_color_key = "gold pins"
    contacts_color_key = "gold pins"

    color_keys = [
        body_color_key,
        pins_color_key,
        contacts_color_key
    ]
    obj_suffixes = [
        '__body',
        '__pins',
        '__contacts'
    ]

    pitch = 0.5

    pinrange = lock_positions.keys()

    pin_inside_distance = 0.45 + 0.525				# Distance between centre of end pin and end of body
    pocket_inside_distance = 0.45			 	# Distance between end of pocket and end of body

    body_width = 2.83
    body_height = 1.15
    body_fillet_radius = 0.15
    body_chamfer = 0.1
    pin_recess_height = 0.4

    pocket_width = 1.65
    pocket_base_thickness = 0.2
    pocket_fillet_radius = 0.15

    pin_width = 0.15
    pin_thickness = 0.075
    pin_minimum_radius = 0.005 + pin_thickness / 2.0
    pin_y_offset = 0.735

    contact_width = 0.2
    contact_thickness = 0.15
    contact_minimum_radius = 0.005 + contact_thickness / 2.0
    contact_slot_width = 0.3
    top_slot_offset = (body_width + pocket_width) / 4.0


calcDim = namedtuple( 'calcDim', ['pin_group_width', 'length', 'pocket_length'])


def dimensions(num_pins):
    pin_group_width = ((num_pins / 2) - 1) * series_params.pitch
    length =  pin_group_width + 2 * series_params.pin_inside_distance
    pocket_length = length - 2.0 * series_params.pocket_inside_distance
    return calcDim(pin_group_width=pin_group_width, length = length, pocket_length=pocket_length)

def generate_pin(num_pins, calc_dim):
    pin_group_width = calc_dim.pin_group_width
    pin_width = series_params.pin_width
    pin_thickness = series_params.pin_thickness
    pin_pitch = series_params.pitch
    body_width = series_params.body_width
    pin_minimum_radius = series_params.pin_minimum_radius
    pin_y_offset = series_params.pin_y_offset
    p_list = [
        ('start', {'position': ((-body_width/2 - pin_y_offset, pin_thickness/2.0)), 'direction': 0.0, 'width':pin_thickness}),
        ('line', {'length': pin_y_offset}),
        ('arc', {'radius': pin_minimum_radius, 'angle': 60.0}),
        ('line', {'length': 0.05}),
        ('arc', {'radius': pin_minimum_radius, 'angle': -60.0}),
        ('line', {'length': 0.4})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0 - pin_group_width/2.0), p_list)
    pin = ribbon.drawRibbon().extrude(pin_width)
    return pin


def generate_pins(num_pins, calc_dim):
    pin_pitch=series_params.pitch
    pin_A = generate_pin(num_pins, calc_dim)
    pin_B = pin_A.mirror("XZ")
    pin_pair = pin_A.union(pin_B)
    pins = pin_pair
    for i in range(0, num_pins / 2):
        pins = pins.union(pin_pair.translate((i*pin_pitch,0,0)))
    return pins


def generate_contact(calc_dim):
    pin_group_width = calc_dim.pin_group_width
    contact_width = series_params.contact_width
    contact_thickness = series_params.contact_thickness
    contact_minimum_radius = series_params.contact_minimum_radius
    pin_pitch = series_params.pitch
    pocket_width = series_params.pocket_width
    body_height = series_params.body_height
    pocket_base_thickness = series_params.pocket_base_thickness
    c_list = [
        ('start', {'position': ((-pocket_width/2 - contact_thickness / 2.0, pocket_base_thickness)), 'direction': 90.0, 'width':contact_thickness}),
        ('line', {'length': body_height  - pocket_base_thickness - contact_minimum_radius - contact_thickness / 2.0}),
        ('arc', {'radius': contact_minimum_radius, 'angle': 90.0}),
        ('line', {'length': 0.25})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-contact_width/2.0 - pin_group_width/2.0), c_list)
    contact = ribbon.drawRibbon().extrude(contact_width)
    contact = contact.faces("<Y").edges("|Z").chamfer((contact_width / 2.0)- 0.01)
    return contact


def generate_contacts(num_pins, calc_dim):
    pin_pitch=series_params.pitch
    contact1 = generate_contact(calc_dim)
    contact2=contact1.mirror("XZ")
    contact_pair = contact1.union(contact2)
    contacts = contact_pair
    for i in range(0, num_pins / 2):
        contacts = contacts.union(contact_pair.translate((i*pin_pitch,0,0)))
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
    pin_pitch = series_params.pitch

    pocket_inside_distance = series_params.pocket_inside_distance
    pocket_width = series_params.pocket_width
    pocket_base_thickness = series_params.pocket_base_thickness
    pocket_fillet_radius = series_params.pocket_fillet_radius

    contact_thickness = series_params.contact_thickness
    contact_slot_width = series_params.contact_slot_width
    top_slot_offset = series_params.top_slot_offset

    pin_group_width = calc_dim.pin_group_width


    # body
    body_A = cq.Workplane("XY")\
        .rect(body_length, body_width).extrude(body_height)\
        .edges("|Z").fillet(body_fillet_radius)
    body_A = body_A.faces("<Y").workplane().center(0, -body_height/2.0).rect(body_length-2*pocket_inside_distance,pin_recess_height*2.0).cutBlind(-body_fillet_radius)
    body_A = body_A.faces(">Y").workplane().center(0, -body_height/2.0).rect(body_length-2*pocket_inside_distance,pin_recess_height*2.0).cutBlind(-body_fillet_radius)
    body_A = body_A.faces(">Z").chamfer(body_chamfer)

    body_B = cq.Workplane("XY")\
        .rect(body_length-0.4, body_width-0.4).extrude(body_height)
    body_A = body_A.cut(body_B)

    pocket = cq.Workplane("XY").workplane(offset=body_height)\
        .rect(body_length - 2.0 * pocket_inside_distance, pocket_width)\
        .extrude(-(body_height - pocket_base_thickness)).edges("|Z").fillet(pocket_fillet_radius)
    body_B = body_B.cut(pocket)

    #body_B = body_B.faces(">Z").edges("not(<X or >X or <Y or >Y)").fillet(body_chamfer)
    body = body_A.union(body_B)

    # cut slots for contacts
    body = body.faces(">Z").workplane().center(0, top_slot_offset)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 1)\
        .center(0, -2 * top_slot_offset)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 1)\
       .cutBlind(-contact_thickness)

    body = body.faces(">Z").workplane().center(0, pocket_width / 2.0)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 2 * contact_thickness)\
        .center(0, -pocket_width)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 2 * contact_thickness)\
       .cutBlind(-body_height + pocket_base_thickness)

   # cut overall side profile
    cutter_A = cq.Workplane("YZ").workplane(offset=(body_length - 2.0 * pocket_inside_distance) / 2.0).center(body_width / 2.0 - 0.2, body_height)\
        .line(0.05, -0.1).line(0,-0.1).line(0.05, -0.1).line(0,-0.3).line(0.06,-0.06)\
        .line(1,0).line(0, body_height).close().extrude(-(body_length - 2.0 * pocket_inside_distance))
    cutter_B = cutter_A.mirror("XZ")
    body = body.cut(cutter_A.union(cutter_B))

    # cut lock pockets in all positions
    cutter = cq.Workplane("XY").workplane(offset=0.49).center(0, body_width / 2.0)
    cutter = my_rarray(cutter, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 0.25)\
        .center(0, -body_width)
    cutter = my_rarray(cutter, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 0.25)\
       .extrude(0.25)
    body = body.cut(cutter)

    # overcut to remove selected lock pockets
    overcut = []
    if 'all' in lock_positions:
        # no need to overcut any lock pockets
        pass
    else:
        if 'none' in lock_positions:
            # need to overcut all lock pockets
            overcut = range(1, 1 + num_pins / 2)
        else:
            # need to overcut those pockets not in lock_positions list
            overcut = [i for i in range(1, 1 + num_pins / 2) if i not in lock_positions]
        cut = cq.Workplane("XY").workplane(offset=0.49).center(-pin_group_width / 2.0, body_width / 2.0)\
            .rect(contact_slot_width, 0.25)\
            .center(0, -body_width)\
            .rect(contact_slot_width, 0.25)\
            .extrude(3)
        for i in overcut:
            cutter = cutter.union(cut.translate(((i-1)*pin_pitch,0,0)))
        body = body.cut(cutter)

    return body


def generate_part(num_pins):
    calc_dim = dimensions(num_pins)
    body = generate_body(num_pins, calc_dim)
    pins = generate_pins(num_pins, calc_dim)
    contacts = generate_contacts(num_pins, calc_dim)
    return (body, pins, contacts)


# opened from within freecad
if "module" in __name__:
    num_pins = 2*8
    # part_to_build = 'molex_55560_2x10'
    # part_to_build = 'molex_55560_2x11'
    # part_to_build = 'molex_55560_2x12'
    # part_to_build = 'molex_55560_2x15'
    # part_to_build = 'molex_55560_2x17'
    # part_to_build = 'molex_55560_2x20'
    # part_to_build = 'molex_55560_2x23'
    # part_to_build = 'molex_55560_2x25'
    # part_to_build = 'molex_55560_2x30'
    # part_to_build = 'molex_55560_2x40'

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 str(num_pins) + "pins variant\n")
    (body, pins, contacts) = generate_part(num_pins)

    show(body)
    show(pins)
    show(contacts)
