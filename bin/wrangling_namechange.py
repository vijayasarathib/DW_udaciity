
# coding: utf-8

# In[29]:

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "c:\Vijay\DS\DW\omaha_nebraska.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            '106': '106',
            '330': '330',
            '370': '370',
            'A': 'A',
            'Ave': 'Avenue',
            'Blvd': 'Blvd',
            'Broadway': 'BroadWay',
            'Circle': 'circle',
            'Dr': 'Drive',
            'Hascall': 'Hascall',
            'Highway': 'Highway',
            'Maple': 'Maple',
            'North': 'North',
            'Plaza': 'Plaza',             
            'Q': 'Q',
            'Rd': 'Road',
            'STREET': 'Street',
            'South': 'South',
            'St': 'Street',
            'St.': 'Street',
            'Way': 'Way',
            'bing': 'bing'
           
            }


# In[30]:

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    #pprint.pprint(dict(street_types)) 
    return street_types


# In[39]:

def update_name(name, mapping):
    m = street_type_re.search(name)
    better_name = name
    if m:
        better_street_type = mapping[m.group()]
        better_name = street_type_re.sub(better_street_type, name)

    return better_name
    # YOUR CODE HERE

    #return name


def test():
    st_types = audit(OSMFILE)
    #assert len(st_types) == 3
    #pprint.pprint(len(st_types))
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
           #pprint.pprint(name)
           #pprint.pprint(mapping) 
           better_name = update_name(name, mapping)
           print name, "=>", better_name
            #if name == "West Lexington St.":
            #    assert better_name == "West Lexington Street"
            #if name == "Baldwin Rd.":
            #    assert better_name == "Baldwin Road"


# In[40]:

if __name__ == '__main__':
    test()


# In[ ]:



