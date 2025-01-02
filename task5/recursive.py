import xml.etree.ElementTree as ET # import the xml module
import sys # import the sys module 
sys.setrecursionlimit(2000) # set the recursion limit to 2000 

xmlfile = 'task5/ proper_file.xml' # path to the xml file, This is a proper file

try:
    tree = ET.parse(xmlfile) # parse the xml file 
    root = tree.getroot() # get the root of the xml file 
except (ET.ParseError):
    print(' The file is empty or invalid')
    exit()

# Dysfunction finds duplicate elements in the XML file
seen_elements = set()
def find_duplicate(value, attribute_name=None, track_specific=None):
    global seen_elements
    # if the attribute name is not in the track_specific list, return
    if track_specific is not None and attribute_name not in track_specific:
        return
    # if the value is in the seen_elements set, print the duplicate value
    if value in seen_elements:
        print(f"Duplicate value detected: {value}")
    # add the value to the seen_element list
    else:
        seen_elements.add(value)

# a function to find broken elements in the xml file 
broken_elements = []
def find_broken_element(element, path=''):
    current_path = f"{path}/{element.tag}" if path else element.tag

    #iterating through the attributes of the element 
    for attribute_name, attribute_value in element.attrib.items():
        # defining what broken element is 
        if attribute_value in ('null', 'None', '', 'unknown'):
            broken_elements.append(f'Broken element: {attribute_name}="{attribute_value}" at {current_path}')
        
        find_duplicate(attribute_value, attribute_name, track_specific={'id'}) # Specify what you don't want any duplicates of 

    #iterating throuhg the children of the element      
    for child in element:
        #recursively calling the function to find the brokec element
        find_broken_element(child, current_path)

#calling the function to find the broken element
find_broken_element(root)

#leting the user know if there is a broken element in the xml file 
if broken_elements:
    print('found broken element')
    for elem in broken_elements:
        print(elem)
else:
    print('No broken element found')