
# coding: utf-8

# In[1]:

#!/usr/bin/env python

import xml.etree.ElementTree as ET
import pprint
import re



lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        k = element.attrib['k']
        #print k
        if len(lower_colon.findall(k)) > 0:
            keys['lower_colon'] += 1
        elif len(lower.findall(k)) > 0:
            keys['lower'] += 1
        elif len(problemchars.findall(k)) > 0:
            keys['problemchars'] += 1
        else:
            keys['other'] +=1
    return keys
        # YOUR CODE HERE
    #    pass
        
   # return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertions will be incorrect then.
    keys = process_map('c:\Vijay\DS\DW\omaha_nebraska.osm')
    pprint.pprint(keys)
    #assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()


# In[ ]:



