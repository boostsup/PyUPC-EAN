'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2014 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2014 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2014 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: __init__.py - Last Update: 10/31/2014 Ver. 2.7.2 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sys, re, imp;

__author__ = "Kazuki Przyborowski";
__copyright__ = "Copyright 2011-2014, Game Maker 2k";
__credits__ = ["Kazuki Przyborowski", "Game Maker 2k"];
__license__ = "Revised BSD License";
__maintainer__ = "Kazuki Przyborowski";
__email__ = "kazuki.przyborowski@gmail.com";
__status__ = "Production";
__project__ = "PyUPC-EAN";
__project_url__ = "https://pypi.python.org/pypi/PyUPC-EAN";
__version_info__ = (2, 7, 2, "RC 1");
__revision__ = __version_info__[3];
if(__version_info__[3]!=None):
 __version__ = "{major}.{minor}.{build} {release}".format(major=__version_info__[0], minor=__version_info__[1], build=__version_info__[2], release=__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = "{major}.{minor}.{build}".format(major=__version_info__[0], minor=__version_info__[1], build=__version_info__[2]);
__version_alt__ = "{major}.{minor}.{build}".format(major=__version_info__[0], minor=__version_info__[1], build=__version_info__[2]);
def version_info():
 global __version_info__;
 if(__version_info__[3]!=None):
  return {"major": __version_info__[0], "minor": __version_info__[1], "build": __version_info__[2], "release": __version_info__[3]};
 if(__version_info__[3]==None):
  return {"major": __version_info__[0], "minor": __version_info__[1], "build": __version_info__[2], "release": None};
__version_date_info__ = (2014, 10, 21, "RC 1");
def version_date():
 global __version_info__;
 if(__version_date_info__[3]!=None):
  return {"year":__version_date_info__[0], "month": __version_date_info__[1], "day": __version_date_info__[2], "release": __version_date_info__[3]};
 if(__version_date_info__[3]==None):
  return {"year":__version_date_info__[0], "month": __version_date_info__[1], "day": __version_date_info__[2], "release": None};
__version_date__ = "{year}.{month}.{day}".format(year=__version_date_info__[0], month=__version_date_info__[1], day=__version_date_info__[2]);
__version_date_alt__ = "{year}.{month}.{day} {release}".format(year=__version_date_info__[0], month=__version_date_info__[1], day=__version_date_info__[2], release=__version_date_info__[2]);

# PIL Support Check
pilsupport = True;
try:
 imp.find_module('PIL');
 pilsupport = True;
except ImportError:
 try:
  imp.find_module('Image');
  pilsupport = True;
 except ImportError:
  pilsupport = False;

'''
// UPC Resources and Info
// Source: http://en.wikipedia.org/wiki/Universal_Product_Code
// Source: http://en.wikipedia.org/wiki/Global_Trade_Item_Number
// Source: http://en.wikipedia.org/wiki/Barcode
// Source: http://www.ucancode.net/CPP_Library_Control_Tool/Draw-Print-encode-UPCA-barcode-UPCE-barcode-EAN13-barcode-VC-Code.htm
// Source: http://en.wikipedia.org/wiki/International_Article_Number
// Source: http://www.upcdatabase.com/docs/
// Source: http://www.accipiter.org/projects/cat.php
// Source: http://www.accipiter.org/download/kittycode.js
// Source: http://uscan.sourceforge.net/upc.txt
// Source: http://www.adams1.com/upccode.html
// Source: http://www.documentmedia.com/Media/PublicationsArticles/QuietZone.pdf
// Source: http://zxing.org/w/decode.jspx
// Source: http://code.google.com/p/zxing/
// Source: http://www.terryburton.co.uk/barcodewriter/generator/
// Source: http://en.wikipedia.org/wiki/Interleaved_2_of_5
// Source: http://www.gs1au.org/assets/documents/info/user_manuals/barcode_technical_details/ITF_14_Barcode_Structure.pdf
// Source: http://www.barcodeisland.com/
'''

import upcean.validate, upcean.convert, upcean.shortcuts, upcean.getprefix;
if(pilsupport==True):
 import upcean.fonts, upcean.xml, upcean.barcodes, upcean.getsfname, upcean.oopfuncs;
