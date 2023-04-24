#
# Copyright 2004 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

def i_code (code3):
    return code3[0]

def o_code(code3):
    return code3[1] if len (code3) >= 2 else code3[0]

def tap_code(code3):
    return code3[2] if len (code3) >= 3 else code3[0]

def i_type (code3):
    return char_to_type[i_code (code3)]

def o_type (code3):
    return char_to_type[o_code (code3)]

def tap_type (code3):
    return char_to_type[tap_code (code3)]


char_to_type = {
    's': 'short',
    'i': 'int',
    'f': 'float',
    'c': 'gr_complex',
    'b': 'unsigned char',
}
