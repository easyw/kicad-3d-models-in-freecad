# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning Molex 502250 Connectors

## This script can be run from within the cadquery module of freecad.
## To generate VRML/ STEP files for, use launch-cq-molex
## script of the parent directory.

#* This is a cadquery script for the generation of MCAD Models.             *
#*                                                                          *
#*   Copyright (c) 2018                                                     *
#* Joel Holdsworth https://github.com/jhol                                  *
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

__title__ = "model description for Molex 502250 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for Molex 502250 series connectors using cadquery'

___ver___ = "0.1 29/01/2018"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Joel Holdsworth"
    STR_licEmail = "joel@airwebreathe.org.uk"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD

class series_params():
    series = "502250"
    manufacturer = 'Molex'
    mpn_format_string = '502250-{pincount:02d}91'
    orientation = 'H'
    datasheet = 'http://www.molex.com/pdm_docs/sd/5022501791_sd.pdf'
    pinrange = [17, 21, 23, 27, 33, 35, 39, 41, 51]
    number_of_rows = 2
    fp_name_format_string = '{man:s}_{mpn:s}_{num_rows:d}Rows-{pins:02d}Pins-1MP_P{pitch:.2f}mm_{orientation:s}'
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

    half_pitch = 0.3
    pitch = half_pitch * 2

    pin_row_spacing = 2.875
    body_width = 3.53
    body_height = 0.88
    body_length_padding = 1.8
    body_y_offset = 0.28 + pin_row_spacing/2
    body_cut_width = body_width - 1.99


def generate_pins(num_pins):
    odd_pins = [
        cq.Workplane("XY")
            .moveTo(i * series_params.half_pitch - series_params.half_pitch * (num_pins - 1)/2,
                -series_params.pin_row_spacing/2)
            .box(0.12, 0.56, 0.21, centered=(True, True, False))
        for i in range(0, num_pins, 2)]
    even_pins = [
        cq.Workplane("XY")
            .moveTo(i * series_params.half_pitch - series_params.half_pitch * (num_pins - 1)/2,
                series_params.pin_row_spacing/2)
            .box(0.15, 0.40, 0.30, centered=(True, True, False))
        for i in range(1, num_pins-1, 2)]
    anchor_pins = [
        cq.Workplane("XY")
            .moveTo(d * ((num_pins-1) * series_params.half_pitch / 2 + 0.7),
                    -series_params.pin_row_spacing/2 + 0.325)
            .box(0.12, 0.55, 0.3, centered=(True, True, False))
        for d in [-1, 1]]

    pins = anchor_pins[0]
    for p in [anchor_pins[1]] + odd_pins + even_pins:
        pins = pins.union(p)
    return pins.rotate((0, 0, 0), (0, 0, 1), -90)


def generate_body(body_length):
    slot_length = body_length - 0.6*2

    body_outline = cq.Workplane("XY") \
        .moveTo(0, 0.1) \
        .polyline([
            (body_length/2-0.745, 0.1),
            (body_length/2-0.745, 0),
            (body_length/2, 0),
            (body_length/2, 0.45),
            (body_length/2-0.28, 0.45),
            (body_length/2-0.28, 0.815),
            (body_length/2, 0.815),
            (body_length/2, 3.53),
            (body_length/2-0.30, 3.53),
            (body_length/2-0.30, 3.28),
            (0, 3.28)
        ]) \
        .mirrorY()

    return body_outline.extrude(series_params.body_height) \
        .cut(cq.Workplane("XY", origin=(0, 0, series_params.body_height))
            .moveTo(-slot_length/2, series_params.body_width - series_params.body_cut_width)
            .rect(slot_length, series_params.body_cut_width, centered=False)
            .extrude(0.26-series_params.body_height)
        ).cut(cq.Workplane("XZ")
            .moveTo(-slot_length/2, 0.26)
            .rect(slot_length, 0.28, centered=False)
            .extrude(-series_params.body_width)
        ).translate((0, -series_params.body_y_offset, 0.02)).rotate((0, 0, 0), (0, 0, 1), -90)


def generate_latch(body_length):
    bar_length = body_length - 1.58
    bar = cq.Workplane("YZ").moveTo(1.41, 0.89).polyline([
            (0, 0.89), (0, 0.4), (1.4-0.65, 0.4), (0.75, 0.15),
            (1.01, 0.15), (1.41, 0.585)]) \
        .close() \
        .extrude(bar_length) \
        .translate((-bar_length/2, series_params.body_width -
            series_params.body_y_offset - 0.75, 0))

    pin_length = body_length - 0.1696
    pin = cq.Workplane("YZ").moveTo(0, 0.4).circle(0.15) \
        .extrude(pin_length) \
        .translate((-pin_length/2, series_params.body_width -
            series_params.body_y_offset - 0.75, 0))

    return bar.union(pin).rotate((0, 0, 0), (0, 0, 1), -90)


def generate_part(num_pins):
    body_length = series_params.body_length_padding + num_pins * series_params.half_pitch
    return (
        generate_pins(num_pins),
        generate_body(body_length),
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
