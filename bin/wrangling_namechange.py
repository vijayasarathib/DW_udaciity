
# coding: utf-8

# In[29]:

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "c:\Vijay\DS\DW\omaha_nebraska.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
# expected variable from the file to be handled by the code
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons",'Broadway','Circle','Plaza']

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            'Ave': 'Avenue',
            'Blvd': 'Blvd',
            'Dr': 'Drive',
            'Rd': 'Road',
            'STREET': 'Street',
            
            }


# In[30]:
#function to handle different street types
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

# function to select only the street tags
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

#function to parse the audit the data
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    #pprint.pprint(dict(street_types)) 
    return street_types



#function to update the names
def update_name(name, mapping):
    m = street_type_re.search(name)
    better_name = name
    if m:
        better_street_type = mapping[m.group()]
        better_name = street_type_re.sub(better_street_type, name)

    return better_name

#driver function for the code
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




if __name__ == '__main__':
    test()






