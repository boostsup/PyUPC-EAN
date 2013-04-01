#!/usr/bin/python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2012 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2012 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2012 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: convert.py - Last Update: 04/01/2013 Ver. 2.3.0 RC 1  - Author: cooldude2k $
'''

import sys, re, upcean.validate;
from upcean.validate import *;

def convert_upce_to_upca(upc):
 upc = str(upc);
 if(len(upc)==7):
  upc = upc+str(validate_upce(upc,True));
 if(len(upc)>8 or len(upc)<8):
  return False;
 if(not re.findall("^(0|1)", upc)):
  return False;
 if(validate_upce(upc)==False):
  return False;
 if(re.findall("(0|1)(\d{5})([0-3])(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
  upc_matches = upc_matches[0];
  if(int(upc_matches[6])==0):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[6]+"0000"+upc_matches[3]+upc_matches[4]+upc_matches[5]+upc_matches[7];
  if(int(upc_matches[6])==1):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[6]+"0000"+upc_matches[3]+upc_matches[4]+upc_matches[5]+upc_matches[7];
  if(int(upc_matches[6])==2):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[6]+"0000"+upc_matches[3]+upc_matches[4]+upc_matches[5]+upc_matches[7];
  if(int(upc_matches[6])==3):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+"00000"+upc_matches[4]+upc_matches[5]+upc_matches[7]; 
 if(re.findall("(0|1)(\d{5})([4-9])(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
  upc_matches = upc_matches[0];
  if(int(upc_matches[6])==4):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+upc_matches[4]+"00000"+upc_matches[5]+upc_matches[7];
  if(int(upc_matches[6])==5):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+upc_matches[4]+upc_matches[5]+"0000"+upc_matches[6]+upc_matches[7];
  if(int(upc_matches[6])==6):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+upc_matches[4]+upc_matches[5]+"0000"+upc_matches[6]+upc_matches[7];
  if(int(upc_matches[6])==7):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+upc_matches[4]+upc_matches[5]+"0000"+upc_matches[6]+upc_matches[7];
  if(int(upc_matches[6])==8):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+upc_matches[4]+upc_matches[5]+"0000"+upc_matches[6]+upc_matches[7];
  if(int(upc_matches[6])==9):
   upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+upc_matches[3]+upc_matches[4]+upc_matches[5]+"0000"+upc_matches[6]+upc_matches[7];
 return upce;
def convert_upca_to_ean13(upc):
 upc = str(upc);
 if(len(upc)==11):
  upc = upc+str(validate_upca(upc,True));
 if(len(upc)>13 or len(upc)<12):
  return False;
 if(validate_upca(upc)==False):
  return False;
 if(len(upc)==12):
  ean13 = "0"+upc;
 if(len(upc)==13):
  ean13 = upc;
 return ean13;
def convert_ean13_to_itf14(upc):
 upc = str(upc);
 if(len(upc)==11):
  upc = upc+str(validate_upca(upc,True));
 if(len(upc)==12):
  upc = "0"+upc;
 if(len(upc)>14 or len(upc)<13):
  return False;
 if(validate_ean13(upc)==False):
  return False;
 if(len(upc)==13):
  itf14 = "0"+upc;
 if(len(upc)==14):
  itf14 = upc;
 return itf14;
def convert_upce_to_ean13(upc):
 upc = str(upc);
 return convert_upca_to_ean13(convert_upce_to_upca(upc));
def convert_upce_to_itf14(upc):
 upc = str(upc);
 return convert_ean13_to_itf14(convert_upce_to_ean13(upc));
def convert_upca_to_itf14(upc):
 upc = str(upc);
 return convert_ean13_to_itf14(convert_upca_to_ean13(upc));
def convert_ean13_to_upca(upc):
 upc = str(upc);
 if(len(upc)==12):
  upc = "0"+upc;
 if(len(upc)>13 or len(upc)<13):
  return False;
 if(validate_ean13(upc)==False):
  return False;
 if(not re.findall("^0(\d{12})", upc)):
  return False;
 if(re.findall("^0(\d{12})", upc)):
  upc_matches = re.findall("^0(\d{12})", upc);
  upca = upc_matches[0];
 return upca;
def convert_itf14_to_ean13(upc):
 upc = str(upc);
 if(len(upc)==13):
  upc = "0"+upc;
 if(len(upc)>14 or len(upc)<14): 
  return False;
 if(validate_itf14(upc)==False):
  return False;
 if(not re.findall("^(\d{1})(\d{12})(\d{1})", upc)):
  return False;
 if(re.findall("^(\d{1})(\d{12})(\d{1})", upc)):
  upc_matches = re.findall("^(\d{1})(\d{12})(\d{1})", upc);
  upc_matches = upc_matches[0];
  ean13 = upc_matches[1]+str(validate_ean13(upc_matches[1], True));
 return ean13;
def convert_upca_to_upce(upc):
 upc = str(upc);
 if(len(upc)==11):
  upc = upc+str(validate_upca(upc,True));
 if(len(upc)>12 or len(upc)<12):
  return False;
 if(validate_upca(upc)==False):
  return False;
 if(not re.findall("(0|1)(\d{11})", upc)):
  return False;
 upce = None;
 if(re.findall("(0|1)(\d{2})00000(\d{3})(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{2})00000(\d{3})(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+"0";
  upce = upce+upc_matches[3]; 
  return upce;
 if(re.findall("(0|1)(\d{2})10000(\d{3})(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{2})10000(\d{3})(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+"1";
  upce = upce+upc_matches[3]; 
  return upce;
 if(re.findall("(0|1)(\d{2})20000(\d{3})(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{2})20000(\d{3})(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+"2";
  upce = upce+upc_matches[3]; 
  return upce;
 if(re.findall("(0|1)(\d{3})00000(\d{2})(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{3})00000(\d{2})(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+"3";
  upce = upce+upc_matches[3]; 
  return upce;
 if(re.findall("(0|1)(\d{4})00000(\d{1})(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{4})00000(\d{1})(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+upc_matches[2]+"4";
  upce = upce+upc_matches[3]; 
  return upce;
 if(re.findall("(0|1)(\d{5})00005(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{5})00005(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+"5";
  upce = upce+upc_matches[2]; 
  return upce;
 if(re.findall("(0|1)(\d{5})00006(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{5})00006(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+"6";
  upce = upce+upc_matches[2]; 
  return upce;
 if(re.findall("(0|1)(\d{5})00007(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{5})00007(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+"7";
  upce = upce+upc_matches[2]; 
  return upce;
 if(re.findall("(0|1)(\d{5})00008(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{5})00008(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+"8";
  upce = upce+upc_matches[2]; 
  return upce;
 if(re.findall("(0|1)(\d{5})00009(\d{1})", upc)):
  upc_matches = re.findall("(0|1)(\d{5})00009(\d{1})", upc);
  upc_matches = upc_matches[0];
  upce = upc_matches[0]+upc_matches[1]+"9";
  upce = upce+upc_matches[2]; 
  return upce;
 if(upce==None):
  return False;
 return upce;
def convert_ean13_to_upce(upc):
 upc = str(upc);
 return convert_upca_to_upce(convert_ean13_to_upca(upc));
def convert_itf14_to_upca(upc):
 upc = str(upc);
 return convert_ean13_to_upca(convert_itf14_to_ean13(upc));
def convert_itf14_to_upce(upc):
 upc = str(upc);
 return convert_upca_to_upce(convert_itf14_to_upca(upc));
def convert_any_to_upca(upc):
 upc = str(upc);
 if(len(upc)==8):
  return convert_upce_to_upca(upc);
 if(len(upc)==13):
  return convert_ean13_to_upca(upc);
 if(len(upc)==14):
  return convert_itf14_to_upca(upc);
 return False;
def convert_any_to_upce(upc):
 upc = str(upc);
 if(len(upc)==12):
  return convert_upca_to_upce(upc);
 if(len(upc)==13):
  return convert_ean13_to_upce(upc);
 if(len(upc)==14):
  return convert_itf14_to_upce(upc);
 return False;
def convert_any_to_ean13(upc):
 upc = str(upc);
 if(len(upc)==8):
  return convert_upce_to_ean13(upc);
 if(len(upc)==12):
  return convert_upca_to_ean13(upc);
 if(len(upc)==14):
  return convert_itf14_to_ean13(upc);
 return False;
def convert_any_to_itf14(upc):
 upc = str(upc);
 if(len(upc)==8):
  return convert_upce_to_itf14(upc);
 if(len(upc)==12):
  return convert_upca_to_itf14(upc);
 if(len(upc)==13):
  return convert_ean13_to_itf14(upc);
 return False;
def convert_any_to_ean8(upc):
 upc = str(upc);
 if(len(upc)==12):
  return convert_upca_to_ean8(upc);
 if(len(upc)==13):
  return convert_ean13_to_ean8(upc);
 if(len(upc)==14):
  return convert_itf14_to_ean8(upc);
 return False;

'''
Changing a EAN-8 code to UPC-A and EAN-13 based on whats used at: 
http://www.upcdatabase.com/
'''
def convert_ean8_to_upca(upc):
 upc = str(upc);
 if(len(upc)==7):
  upc = upc+str(validate_ean8(upc,True));
 if(len(upc)>8 or len(upc)<8):
  return False;
 if(validate_ean8(upc)==False):
  return False;
 upca = "0000"+upc; 
 return upca;
def convert_ean8_to_ean13(upc):
 upc = str(upc);
 return convert_upca_to_ean13(convert_ean8_to_upca(upc));
def convert_ean8_to_itf14(upc):
 upc = str(upc);
 return convert_ean13_to_itf14(convert_ean8_to_ean13(upc));
def convert_upca_to_ean8(upc):
 upc = str(upc);
 if(len(upc)==11):
  upc = upc+str(validate_upca(upc,True));
 if(len(upc)>12 or len(upc)<12):
  return False;
 if(validate_upca(upc)==False):
  return False;
 if(not re.findall("^0000(\d{8})", upc)):
  return False;
 if(re.findall("^0000(\d{8})", upc)):
  upc_matches = re.findall("^0000(\d{8})", upc);
  ean8 = upc_matches[0];
 return ean8;
def convert_ean13_to_ean8(upc):
 upc = str(upc);
 return convert_upca_to_ean8(convert_ean13_to_upca(upc));
def convert_itf14_to_ean8(upc):
 upc = str(upc);
 return convert_ean13_to_ean8(convert_itf14_to_ean13(upc));

'''
ISSN (International Standard Serial Number)
http://en.wikipedia.org/wiki/International_Standard_Serial_Number
'''
def convert_issn8_to_issn13(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 upc = upc.replace("X", "");
 if(validate_issn8(upc)==False): 
  return False;
 if(len(upc)>7): 
  fix_matches = re.findall("^(\d{7})", upc); 
  upc = fix_matches[0];
 issn13 = "977"+upc+"00"+str(validate_ean13("977"+upc+"00",True)); 
 return issn13;
def convert_issn13_to_issn8(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 upc = upc.replace("X", "");
 if(validate_ean13(upc)==False): 
  return False;
 if(not re.findall("/^977(\d{7})/", upc)):
  return False;
 if(re.findall("^977(\d{7})", upc)):
  upc_matches = re.findall("^977(\d{7})", upc);
  issn8 = upc_matches[1]+validate_issn8(upc_matches[1],True);
 return issn8;
def print_issn8(upc):
 upc = str(upc);
 if(len(upc)>8): 
  fix_matches = re.findall("^(\d{8})", upc); 
  upc = fix_matches[1];
 if(len(upc)>8 or len(upc)<8): 
  return False;
 if(not re.findall("^(\d{4})(\d{4})", upc)):
  return False;
 issn_matches = re.findall("^(\d{4})(\d{4})", upc);
 issn_matches = issn_matches[0];
 issn8 = issn_matches[0]+"-"+issn_matches[1];
 return issn8;
def print_issn13(upc):
 upc = str(upc);
 if(len(upc)>13): 
  re.findall("^(\d{13})", upc, fix_matches); 
  upc = fix_matches[1];
 if(len(upc)>13 or len(upc)<13): 
  return False;
 if(not re.findall("^(\d{3})(\d{4})(\d{4})(\d{2})", upc, issn_matches)):
  return False;
 issn_matches = re.findall("^(\d{3})(\d{4})(\d{4})(\d{2})", upc);
 issn_matches = issn_matches[0];
 issn13 = issn_matches[0]+"-"+issn_matches[1]+"-"+issn_matches[2]+"-"+issn_matches[3];
 return issn13;
def print_convert_issn8_to_issn13(upc):
 upc = str(upc);
 issn13 = print_issn13(convert_issn8_to_issn13(upc));
 return issn13;
def print_convert_issn13_to_issn8(upc):
 upc = str(upc);
 issn8 = print_issn8(convert_issn13_to_issn8(upc));
 return issn8;

'''
ISBN (International Standard Book Number)
http://en.wikipedia.org/wiki/ISBN
'''
def convert_isbn10_to_isbn13(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(validate_isbn10(upc)==False):
  return False;
 if(len(upc)>9):
  fix_matches = re.findall("^(\d{9})", upc);
  upc = fix_matches[0];
  isbn13 = "978"+upc+str(validate_ean13("978"+upc,True)); 
 return isbn13;
def convert_isbn13_to_isbn10(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(validate_ean13(upc)==False):
  return False;
 if(not re.findall("^978(\d{9})", upc)):
  return False;
 if(re.findall("^978(\d{9})", upc)):
  upc_matches = re.findall("^978(\d{9})", upc);
  isbn10 = upc_matches[0]+str(validate_isbn10(upc_matches[0],True));
 return isbn10;
def convert_isbn10_to_ean13(upc):
 upc = str(upc);
 return convert_isbn10_to_isbn13(upc);
def convert_ean13_to_isbn10(upc):
 upc = str(upc);
 return convert_isbn13_to_isbn10(upc);
def convert_isbn10_to_itf14(upc):
 upc = str(upc);
 return convert_ean13_to_itf14(convert_isbn10_to_isbn13(upc));
def convert_itf14_to_isbn10(upc):
 upc = str(upc);
 return convert_itf14_to_ean13(convert_isbn13_to_isbn10(upc));
def print_isbn10(upc):
 upc = str(upc);
 if(len(upc)>10):
  fix_matches = re.findall("^(\d{9})(\d{1}|X{1})", upc); 
  fix_matches = fix_matches[0]
  upc = fix_matches[0]+fix_matches[1];
 if(len(upc)>10 or len(upc)<10):
  return False;
 if(not re.findall("^(\d{1})(\d{3})(\d{5})(\d{1}|X{1})", upc)):
  return False;
 isbn_matches = re.findall("^(\d{1})(\d{3})(\d{5})(\d{1}|X{1})", upc);
 isbn_matches = isbn_matches[0];
 isbn10 = isbn_matches[0]+"-"+isbn_matches[1]+"-"+isbn_matches[2]+"-"+isbn_matches[3];
 return isbn10;
def print_isbn13(upc):
 upc = str(upc);
 if(len(upc)>13):
  fix_matches = re.findall("^(\d{13})", upc); 
  upc = fix_matches[1];
 if(len(upc)>13 or len(upc)<13):
  return False;
 if(not re.findall("^(\d{3})(\d{1})(\d{3})(\d{5})(\d{1})", upc)):
  return False;
 isbn_matches = re.findall("^(\d{3})(\d{1})(\d{3})(\d{5})(\d{1})", upc);
 isbn_matches = isbn_matches[0];
 isbn13 = isbn_matches[0]+"-"+isbn_matches[1]+"-"+isbn_matches[2]+"-"+isbn_matches[3]+"-"+isbn_matches[4];
 return isbn13;
def print_convert_isbn10_to_isbn13(upc):
 upc = str(upc);
 isbn13 = print_isbn13(convert_isbn10_to_isbn13(upc));
 return isbn13;
def print_convert_isbn13_to_isbn10(upc):
 upc = str(upc);
 isbn10 = print_isbn10(convert_isbn13_to_isbn10(upc));
 return isbn10;

'''
ISMN (International Standard Music Number)
http://en.wikipedia.org/wiki/International_Standard_Music_Number
http://www.ismn-international.org/whatis.html
http://www.ismn-international.org/manual_1998/chapter2.html
'''
def convert_ismn10_to_ismn13(upc):
 upc = str(upc);
 upc = upc.replace("M", "");
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(validate_ismn10(upc)==False):
  return False;
 if(len(upc)>8):
  fix_matches = re.findall("^(\d{8})", upc); 
  upc = fix_matches[0];
 ismn13 = "9790"+upc+str(validate_ean13("9790"+upc,True)); 
 return ismn13;
def convert_ismn13_to_ismn10(upc):
 upc = str(upc);
 upc = upc.replace("M", "");
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(validate_ean13(upc)==False):
  return False;
 if(not re.findall("^9790(\d{8})", upc)):
  return False;
 if(re.findall("^9790(\d{8})", upc)):
  upc_matches = re.findall("^9790(\d{8})", upc);
  ismn10 = upc_matches[0]+str(validate_ismn10(upc_matches[0],True));
 return ismn10;
def convert_ismn10_to_ean13(upc):
 upc = str(upc);
 return convert_ismn10_to_ismn13(upc);
def convert_ean13_to_ismn10(upc):
 upc = str(upc);
 return convert_ismn13_to_ismn10(upc);
def convert_ismn10_to_itf14(upc):
 upc = str(upc);
 return convert_ean13_to_itf14(convert_ismn10_to_ismn13(upc));
def convert_itf14_to_ismn10(upc):
 upc = str(upc);
 return convert_itf14_to_ean13(convert_ismn13_to_ismn10(upc));
def print_ismn10(upc):
 upc = str(upc);
 upc = upc.replace("M", "");
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>9):
  re.findall("^(\d{9})", upc, fix_matches); 
  upc = fix_matches[0];
 if(len(upc)>9 or len(upc)<9):
  return False;
 if(not re.findall("^(\d{4})(\d{4})(\d{1})", upc)):
  return False;
 ismn_matches = re.findall("^(\d{4})(\d{4})(\d{1})", upc);
 ismn_matches = ismn_matches[0];
 ismn10 = "M-"+ismn_matches[0]+"-"+ismn_matches[1]+"-"+ismn_matches[2];
 return ismn10;
def print_ismn13(upc):
 upc = str(upc);
 if(len(upc)>13):
  fix_matches = re.findall("^(\d{13})", upc); 
  upc = fix_matches[0];
 if(len(upc)>13 or len(upc)<13):
  return False;
 if(not re.findall("^(\d{3})(\d{1})(\d{4})(\d{4})(\d{1})", upc)):
  return False;
 ismn_matches = re.findall("^(\d{3})(\d{1})(\d{4})(\d{4})(\d{1})", upc);
 ismn_matches = ismn_matches[0];
 ismn13 = ismn_matches[0]+"-"+ismn_matches[1]+"-"+ismn_matches[2]+"-"+ismn_matches[3]+"-"+ismn_matches[4];
 return ismn13;
def print_convert_ismn10_to_ismn13(upc):
 upc = str(upc);
 ismn13 = print_ismn13(convert_ismn10_to_ismn13(upc));
 return ismn13;
def print_convert_ismn13_to_ismn10(upc):
 upc = str(upc);
 ismn10 = print_ismn10(convert_ismn13_to_ismn10(upc));
 return ismn10;

'''
// Get variable weight price checksum
// Source: http://wiki.answers.com/Q/How_does_a_price_embedded_bar_code_work
// Source: http://en.wikipedia.org/wiki/Universal_Product_Code#Prefixes
// Source: http://barcodes.gs1us.org/GS1%20US%20BarCodes%20and%20eCom%20-%20The%20Global%20Language%20of%20Business.htm
'''
def make_vw_upca(code, price):
 code = str(code);
 price = str(price);
 if(len(code)>5):
  if(re.findall("^(\d{5})", code)):
   code_matches = re.findall("^(\d{5})", code);
   code = code_matches[0];
 if(len(price)>4):
  if(re.findall("^(\d{4})", price)):
   price_matches = re.findall("^(\d{4})", price);
   price = price_matches[0];
 pricecs = str(get_vw_price_checksum(price));
 vwupc = "2"+code+pricecs+price;
 vwupc = vwupc+str(validate_upca(vwupc, True));
 return vwupc;
def make_vw_to_ean13(code, price):
 code = str(code);
 price = str(price);
 vwean13 = convert_upca_to_ean13(make_vw_upca(code, price));
 return vwean13;
def make_vw_to_itf14(code, price):
 code = str(code);
 price = str(price);
 vwitf14 = convert_upca_to_itf14(make_vw_upca(code, price));
 return vwitf14;
def make_coupon_upca(numbersystem, manufacturer, family, value):
 numbersystem = str(numbersystem);
 manufacturer = str(manufacturer);
 family = str(family);
 value = str(value);
 if(int(numbersystem)!=5 and int(numbersystem)!=9):
  numbersystem = "5";
 if(len(manufacturer)>5):
  fix_matches = re.findall("^(\d{5})", manufacturer); 
  upc = fix_matches[0];
 if(len(family)>3):
  fix_matches = re.findall("^(\d{3})", family); 
  upc = fix_matches[0];
 if(len(value)>2):
  fix_matches = re.findall("^(\d{2})", value); 
  upc = fix_matches[0];
 couponupca = numbersystem+manufacturer+family+value;
 couponupca = couponupca+str(validate_upca(couponupca, True));
 return couponupca;
def make_coupon_to_ean13(numbersystem, manufacturer, family, value):
 numbersystem = str(numbersystem);
 manufacturer = str(manufacturer);
 family = str(family);
 value = str(value);
 couponean13 = convert_upca_to_ean13(make_coupon_upca(numbersystem, manufacturer, family, value));
 return couponean13;
def make_coupon_to_itf14(numbersystem, manufacturer, family, value):
 numbersystem = str(numbersystem);
 manufacturer = str(manufacturer);
 family = str(family);
 value = str(value);
 couponitf14 = convert_upca_to_itf14(make_coupon_upca(numbersystem, manufacturer, family, value));
 return couponitf14;
