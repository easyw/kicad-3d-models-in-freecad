"""
    ribbon
    ======

    A helper module for CadQuery and FreeCAD

    This software is licensed by Ray Benitez under the MIT License.

    git@hackscribble.com | http://www.hackscribble.com

"""


import cadquery as cq
from Helpers import show
import numpy as np


class Ribbon:
    """Constructs a CadQuery closed wire that is a constant-width
       expansion of line represented by a list of "turtle graphics" style
       plotting commands.  From the starting position, the left hand side of
       of the ribbon is drawn by parsing the commmands from start to finish.
       The right hand side of the ribbon is then drawn by parsing the commands
       in reverse order.

       Arguments:
       cq -- CadQuery object
       commands -- list of plotting commands

       Returns:
       cq -- CadQuery object with closed wire added
       """

    def __init__(self, cq, commands):
        self.cq = cq
        self.commands = commands
        self.current_x = 0
        self.current_y = 0
        self.direction = 0


    def _rotate(self, sx, sy, cx, cy, theta_degrees):
        """Rotate a point about a centre through an angle.

           Arguments:
           sx, sy -- x,y coordinates of point
           cx, cy -- x,y coordinates of centre of rotation
           theta_degrees -- angle of rotation in degrees (+ve for CCW, -ve for CW)

           Return values:
           ex, ey -- x,y coordinates of the rotated point
           """
        vsx = sx - cx
        vsy = sy - cy
        theta = np.deg2rad(theta_degrees)
        vex = np.cos(theta) * vsx - np.sin(theta) * vsy
        vey = np.sin(theta) * vsx + np.cos(theta) * vsy
        ex = cx + vex
        ey = cy + vey
        return ex, ey


    def _turn(self, vx, vy, direction_degrees, r, turn_degrees):
        """Calculate an arc from the current position and direction
           that turns through an angle with a given radius.

           Arguments:
           vx, vy -- x,y coordinates of current position
           direction_degrees -- current direction in degrees
           r -- radius of the turning arc
           turn_degrees -- angle of turning in degrees (+ve for CCW, -ve for CW)

           Returns:
           qmx, qmy -- x,y coordinates of a mid point of the three point arc
           qex, qey -- x,y coordinates of the end point of the three point arc
           rx, ry -- x,y coordinates of the centre of rotation of the arc
           """
        direction = np.deg2rad(direction_degrees)
        turn = np.deg2rad(turn_degrees)
        if turn > 0:
            # turning left
            rx = vx - r * np.sin(direction)
            ry = vy + r * np.cos(direction)
        else:
            # turning right
            rx = vx + r * np.sin(direction)
            ry = vy - r * np.cos(direction)
        qex, qey = self._rotate(vx, vy, rx, ry, turn_degrees)
        qmx, qmy = self._rotate(vx, vy, rx, ry, turn_degrees / 2)
        return qmx, qmy, qex, qey, rx, ry


    def _parseCommands(self, commands, offset, direction_multiplier, debug=False):
        """Adds edges to a CadQuery object based on a list of "turtle graphics" style
           plotting commands.

           Arguments:
           cq -- CadQuery object
           commands -- list of plotting commands
           offset -- distance between generated edge and centreline of command
           direction_multiplier -- +1 for left hand side of ribbon, -1 for right hand side

           Returns:
           cq -- CadQuery object with edges added
           """
        for c in commands:
            if c[0] == 'start':
                pass
            elif c[0] == 'line':
                if 'angle' in c[1]:
                    angle = c[1]['angle'] * direction_multiplier
                    self.direction += angle
                vx = c[1]['length'] * np.cos(np.deg2rad(self.direction))
                vy = c[1]['length'] * np.sin(np.deg2rad(self.direction))
                self.current_x += vx
                self.current_y += vy
                self.cq = self.cq.lineTo(self.current_x, self.current_y)
                if debug:
                    print("line to {0} {1} {2}".format(self.current_x, self.current_y, self.direction))
            elif c[0] == 'arc':
                angle = c[1]['angle'] * direction_multiplier
                radius = c[1]['radius']
                if angle > 0:
                    radius -= offset
                else:
                    radius += offset
                mid_x, mid_y, turn_x, turn_y, centre_x, centre_y =\
                    self._turn(self.current_x, self.current_y, self.direction, radius, angle)
                self.cq = self.cq.threePointArc((mid_x, mid_y), (turn_x, turn_y))
                self.direction += angle
                self.current_x, self.current_y = turn_x, turn_y
                if debug:
                    print("arc to {0} {1} {2} {3} {4}".format(self.current_x, self.current_y, self.direction, radius, angle))
            else:
                print('RIBBON ERROR: unrecognised command: {0}'.format(c))
        return self.cq


    def drawRibbon(self, debug=False):
        if self.commands[0][0] == 'start':
            self.direction = self.commands[0][1]['direction']
            half_width = self.commands[0][1]['width'] / 2.0
            self.current_x = self.commands[0][1]['position'][0] + half_width * np.cos(np.deg2rad(self.direction + 90))
            self.current_y = self.commands[0][1]['position'][1] + half_width * np.sin(np.deg2rad(self.direction + 90))
            self.cq = self.cq.moveTo(self.current_x, self.current_y)
            if debug:
                print("start at {0} {1}".format(self.current_x, self.current_y))
        else:
            print('RIBBON ERROR: start command not found')
            return
        self.cq = self._parseCommands(self.commands[1:], half_width, 1, debug)
        self.direction += 180
        self.current_x += 2 * half_width * np.cos(np.deg2rad(self.direction + 90))
        self.current_y += 2 * half_width * np.sin(np.deg2rad(self.direction + 90))
        self.cq = self.cq.lineTo(self.current_x, self.current_y)
        if debug:
            print("line to {0} {1} {2}".format(self.current_x, self.current_y, self.direction))
        self.cq = self._parseCommands(self.commands[:0:-1], half_width, -1, debug)
        self.cq = self.cq.close()
        return self.cq
