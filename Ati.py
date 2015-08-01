#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ati.py
#  
#  Copyright 2014 Achilles <achmo@ach>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#import os.pat
import subprocess


def current():
	fanspeed=subprocess.call("aticonfig --pplib-cmd \"get fanspeed 0 \" | grep   Result | awk  '{print \"Your current fanspeed is \"  $4}'",shell=True)
	
   
def ati():
	current()
	x=input('Choose fanspeed: ')
	if(validate(x)==True):
		subprocess.call('aticonfig --pplib-cmd \"set fanspeed 0 %d \"'%(float(x)),shell=True)
		
	
	
def validate(x):
	if float(x) > 100:
		print('Fan speed can\'t exceed 100%')
		return False
	elif float(x) < 0:
		print('Fan speed can\'t be lower than 0!')
		return False
	elif float(x) < 20:
		print('Warning.You chose a lower than default fan speed.')
		return False
	else:
		return True
		


ati()
