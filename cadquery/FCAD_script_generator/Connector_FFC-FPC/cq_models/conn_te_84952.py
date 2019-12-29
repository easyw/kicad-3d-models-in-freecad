# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning TE 84952 Connectors
# Based on molex/cq_models/conn_molex_502250.py by Joel Holdsworth

#* This is a cadquery script for the generation of MCAD Models.             *
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

__title__ = "model description for TE 84952 series connectors"
__author__ = "antonlysak"
__Comment__ = 'model description for TE 84952 series connectors using cadquery'

___ver___ = "0.1 29/12/2019"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Anton Lysak"
    STR_licEmail = "antonlysak@gmail.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD

class series_params():
    series = "84952"
    manufacturer = 'TE'
    mpn_format_string = '{pnp:s}84952-{pns:s}'
    orientation = 'H'
    datasheet = 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=84952&DocType=Customer+Drawing&DocLang=English&DocFormat=pdf'
    pinrange = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    number_of_rows = 1

    fp_name_format_string = '{man:s}_{mpn:s}_1x{pins:02d}-1MP_P{pitch:.1f}mm_{orientation:s}'
    mount_pin = ''

    pins_color_key = "metal grey pins"
    body_color_key = "white body"
    latch_color_key = "black body"
    color_keys = [
        body_color_key,
        pins_color_key,
        latch_color_key
    ]
    obj_suffixes = [
        '__pins',
        '__body',
        '__latch'
    ]

    half_pitch = 0.5
    pitch = half_pitch * 2

    pin_y = -1.94
    pin_full_y = -1.31
    pin_width = 0.20
    pin_length = 1.14
    pin_height = 0.69
    pin_full_height = 2.05

    mpad_y = 1
    mpad_offset_x = 2.99
    mpad_width = 2.5
    mpad_length = 3.5
    mpad_height = 0.18

    body_width = 3.53
    body_height = 2.56
    body_length_padding = 6.87
    body_y_offset = -0.8
    body_latch_border = 3.5
    latch_closed = 5.4
    latch_ear_width = 1.025

def generate_pins(num_pins):
    electrical_pins = [
        cq.Workplane("XY")
            .moveTo(i * series_params.pitch - series_params.pitch * (num_pins - 1)/2,
                series_params.pin_y)
            .box(series_params.pin_width, series_params.pin_length, series_params.pin_full_height, centered=(True, False, False))
        for i in range(0, num_pins, 1)]
    mounting_pins = [
        cq.Workplane("XY")
            .moveTo(d * ((num_pins-1) * series_params.pitch / 2 + series_params.mpad_offset_x),
                    series_params.mpad_y)
            .box(series_params.mpad_width, series_params.mpad_length, series_params.mpad_height, centered=(True, True, False))
        .cut(cq.Workplane("XY", origin=(0, 0, 0)) \
            .moveTo(d * ((num_pins-1) * series_params.pitch / 2 + series_params.mpad_offset_x + series_params.mpad_width/2), series_params.mpad_y) \
        .rect(1, 0.5, centered=True) \
            .moveTo(d * ((num_pins-1) * series_params.pitch / 2 + series_params.mpad_offset_x + series_params.mpad_width/2), series_params.mpad_y + 1) \
        .rect(1, 0.5, centered=True) \
            .moveTo(d * ((num_pins-1) * series_params.pitch / 2 + series_params.mpad_offset_x + series_params.mpad_width/2), series_params.mpad_y - 1) \
        .rect(1, 0.5, centered=True) \
        .extrude(series_params.mpad_height))
        for d in [-1, 1]]

    pins = mounting_pins[0]
    for p in [mounting_pins[1]] + electrical_pins:
        pins = pins.union(p)
    return pins \
    .cut(cq.Workplane("XY", origin=(0, 0, series_params.pin_full_height)) \
    .moveTo(0, series_params.pin_full_y + (series_params.pin_y - series_params.pin_full_y)/2) \
    .rect(num_pins * series_params.pitch, series_params.pin_y - series_params.pin_full_y, centered=True) \
    .extrude(series_params.pin_height - series_params.pin_full_height)) \
    .rotate((0, 0, 0), (0, 0, 1), 180)


def generate_body(num_pins, body_length):

    body_outline = cq.Workplane("XY") \
        .moveTo(0, series_params.body_y_offset) \
        .polyline([
            (body_length/2, series_params.body_y_offset),
            (body_length/2, series_params.body_y_offset + series_params.body_latch_border),
            (0, series_params.body_y_offset + series_params.body_latch_border)
        ]) \
        .mirrorY().extrude(series_params.body_height)

    ffc_pins = [
        cq.Workplane("XY")
            .moveTo(i * series_params.pitch - series_params.pitch * (num_pins - 1)/2 - series_params.half_pitch,
                series_params.body_y_offset + (series_params.latch_closed - series_params.body_latch_border)/2 + series_params.body_latch_border)
            .box(series_params.pitch - series_params.pin_width, series_params.latch_closed - series_params.body_latch_border,  series_params.body_height, centered=(True, True, False))
        for i in range(0, num_pins + 1, 1)]

    for d in [-1, 1]:
        body_outline = body_outline \
        .cut(cq.Workplane("XY", origin=(0, 0, 0)) \
        .moveTo(d * ((num_pins-1) * series_params.pitch / 2 + series_params.mpad_offset_x), series_params.mpad_y) \
        .rect(series_params.mpad_width, series_params.mpad_length, centered=True) \
        .extrude(series_params.mpad_height))

    for p in ffc_pins:
        body_outline = body_outline.union(p)

    return body_outline \
    .cut(cq.Workplane("XY", origin=(0, 0, series_params.body_height)) \
    .moveTo(0, series_params.body_y_offset + (series_params.latch_closed - series_params.body_latch_border)/2 + series_params.body_latch_border) \
    .rect(body_length, series_params.latch_closed - series_params.body_latch_border, centered=True) \
    .extrude(-1.86)) \
    .cut(cq.Workplane("XY", origin=(0, 0, 0)) \
    .moveTo(0, series_params.body_y_offset + (series_params.latch_closed - series_params.body_latch_border)/2 + series_params.body_latch_border) \
    .rect(body_length, series_params.latch_closed - series_params.body_latch_border, centered=True) \
    .extrude(0.1)) \
    .union(cq.Workplane("XY", origin=(0, 0, series_params.body_height)) \
    .moveTo(0, series_params.body_y_offset + series_params.body_latch_border) \
    .rect(body_length - 4.69, series_params.latch_closed - series_params.body_latch_border, centered=True) \
    .extrude(-1)) \
    .rotate((0, 0, 0), (0, 0, 1), 180)

def generate_latch(body_length):
    slot_length = body_length - 4.69

    latch_outline = cq.Workplane("XY") \
        .moveTo(0, series_params.body_y_offset + series_params.body_latch_border + (series_params.latch_closed - series_params.body_latch_border)/2) \
        .polyline([
            (slot_length/2, series_params.body_y_offset + series_params.body_latch_border + (series_params.latch_closed - series_params.body_latch_border)/2),
            (slot_length/2, series_params.body_y_offset + series_params.body_latch_border),
            (body_length/2, series_params.body_y_offset + series_params.body_latch_border),
            (body_length/2, series_params.body_y_offset + series_params.body_latch_border + (series_params.latch_closed - series_params.body_latch_border)/2),
            (body_length/2 + series_params.latch_ear_width, series_params.body_y_offset + series_params.body_latch_border + (series_params.latch_closed - series_params.body_latch_border)/2),
            (body_length/2 + series_params.latch_ear_width, series_params.body_y_offset + series_params.latch_closed),
            (0, series_params.body_y_offset + series_params.latch_closed)
        ]) \
        .mirrorY()

    return latch_outline.extrude(series_params.body_height) \
    .cut(cq.Workplane("XY", origin=(0, 0, 0)) \
    .moveTo(0, series_params.body_y_offset + (series_params.latch_closed - series_params.body_latch_border)/2 + series_params.body_latch_border) \
    .rect(slot_length, series_params.latch_closed - series_params.body_latch_border, centered=True) \
    .extrude(1.56)) \
    .cut(cq.Workplane("XY", origin=(0, 0, 0)) \
    .moveTo(0, series_params.body_y_offset + (series_params.latch_closed - series_params.body_latch_border)/2 + series_params.body_latch_border) \
    .rect(body_length + series_params.latch_ear_width * 2, series_params.latch_closed - series_params.body_latch_border, centered=True) \
    .extrude(series_params.mpad_height)) \
    .rotate((0, 0, 0), (0, 0, 1), 180)

def generate_part(num_pins):
    body_length = series_params.body_length_padding + (num_pins - 1) * series_params.pitch
    return (
        generate_pins(num_pins),
        generate_body(num_pins, body_length),
        generate_latch(body_length))

# opened from within freecad
if "module" in __name__:
    part_to_build = 17

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 str(part_to_build) + "pin variant\n")
    (pins, body, latch) = generate_part(part_to_build)

    show(pins)
    show(body)
    show(latch)
