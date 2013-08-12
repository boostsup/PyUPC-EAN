'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2013 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2013 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2013 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: prepil.py - Last Update: 11/27/2013 Ver. 2.5.4 RC 1  - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import re, os, sys;
from PIL import Image, ImageDraw, ImageFont;

'''
http://stevehanov.ca/blog/index.php?id=28
'''
def snapCoords( ctx, x, y ):
 (xd, yd) = ctx.user_to_device(x, y);
 return ( round(x) + 0.5, round(y) + 0.5 );

def drawColorLine( ctx, x1, y1, x2, y2, color ):
 ctx.line((x1, y1, x2, y2), fill=color);

def drawColorRectangle( ctx, x1, y1, x2, y2, color ):
 ctx.rectangle([(x1, y1), (x2, y2)], fill=color);

def drawColorText( ctx, size, x, y, text, color ):
 font = ImageFont.truetype(os.path.dirname(__file__)+os.sep+"OCRB.otf", size);
 text = str(text);
 ctx.text((x, y), text, font=font, fill=color);
 del(font);

def drawColorRectangleAlt( ctx, x1, y1, x2, y2, color ):
 ctx.rectangle([(x1, y1), (x2, y2)], outline=color);
    