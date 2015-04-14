
# coding: utf-8

# In[4]:

#!/usr/bin/env python

import xml.etree.ElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:          # find where uid is tag attribute 
             users.add(element.attrib['uid'])
        pass

    return users

def test():

    users = process_map(r'c:\Vijay\DS\DW\omaha_nebraska.osm')
    pprint.pprint(users)
    #assert len(users) == 6



if __name__ == "__main__":
    test()


##### 

# In[ ]:



