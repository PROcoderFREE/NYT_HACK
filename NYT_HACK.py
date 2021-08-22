#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:12:13 2021

@author: naza
"""

import subprocess
import os

class FoundException(Exception):pass


def input_data():
    list_links = []
    while True:
         sep_link = input('Paste URL links here and press ENTER after every link --> ')
         if sep_link == '':
             break
         list_links.append(sep_link) 
    
    executive_list = ['curl', '-O']
    for link in list_links:
        if '.html' not in link or 'https://' not in link:
            raise FoundException()
        executive_list.append(link)
        executive_list.append('-O')
    executive_list.pop(len(executive_list)-1)
    return executive_list


try:
   exec_data = input_data()
except FoundException:
   print('Every inputed string should be a link and has .http extension!!!')
   exec_data = input_data()

current_directory = os.getcwd()
cmd = 'cd '+current_directory

os.system(cmd)
subprocess.run(exec_data)

print('File(s) was(were) succesfully saved in this directory:'+current_directory)

rights = input('<<<created_by_naza_nazirov>>>')