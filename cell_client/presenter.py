
'''
/*  Copyright (C) 2007  Adenilson Cavalcanti <savagobr@yahoo.com>
 *
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; by version 2 of the License.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 */
'''

sys.path.append('E:\\python\\libs\\')
import socket
import appuifw
import e32
from keyboard import *
from bt_client import *


def quit():
    global running
    running=0
    appuifw.app.set_exit()



bt = bt_client()
keyboard = Keyboard()

running = 1
canvas = appuifw.Canvas(event_callback = keyboard.handle_event, redraw_callback=None)
mouse_x = 400
mouse_y = 400
delta = 10

appuifw.app.body = canvas
appuifw.app.exit_key_handler = quit

bt.connect()
while running:
    if keyboard.is_down(EScancode6):
        print u'RIGHT'
        bt.write_line(u'RIGHT')
    elif keyboard.is_down(EScancode4):
        print u'LEFT'
        bt.write_line(u'LEFT')
    elif keyboard.is_down(EScancode2):
        print u'UP'
        bt.write_line(u'UP')
    elif keyboard.is_down(EScancode8):
        print u'DOWN'
        bt.write_line(u'DOWN')
    elif keyboard.is_down(EScancodeUpArrow):
        print u'MOUSE_UP'
        mouse_y = mouse_y - delta
        bt.write_line(u'MOUSE_MOVE')
        bt.write_line(str(mouse_x))
        bt.write_line(str(mouse_y))
    elif keyboard.is_down(EScancodeDownArrow):
        print u'MOUSE_DOWN'
        mouse_y = mouse_y + delta
        bt.write_line(u'MOUSE_MOVE')
        bt.write_line(str(mouse_x))
        bt.write_line(str(mouse_y))
    elif keyboard.is_down(EScancodeLeftArrow):
        print u'MOUSE_LEFT'
        mouse_x = mouse_x - delta
        bt.write_line(u'MOUSE_MOVE')
        bt.write_line(str(mouse_x))
        bt.write_line(str(mouse_y))
    elif keyboard.is_down(EScancodeRightArrow):
        print u'MOUSE_RIGHT'
        mouse_x = mouse_x + delta
        bt.write_line(u'MOUSE_MOVE')
        bt.write_line(str(mouse_x))
        bt.write_line(str(mouse_y))
    e32.ao_yield()



bt.close()