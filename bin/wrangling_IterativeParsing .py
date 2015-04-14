
# coding: utf-8

# In[1]:

import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
        tags = {}
        for (event, node) in ET.iterparse(filename, ['start']):
            tag = node.tag
            if tag and not tag in tags.keys():
                tags[tag] = 0
            tags[tag] = tags[tag] + 1
        return tags
                
            


def test():
    tags = count_tags(r'c:\Vijay\DS\DW\omaha_nebraska.osm')
    pprint.pprint(tags)
    #assert tags == {'bounds': 1, 'member': 3,'nd': 4,'node': 20,'osm': 1,'relation': 1,'tag': 7,              'way': 1}

    

if __name__ == "__main__":
    test()


# In[25]:




# In[25]:




# In[ ]:



