import xml.etree.ElementTree as ET # import the xml module
import sys # import the sys module 
sys.setrecursionlimit(2000) # set the recursion limit to 2000 

# xmlfile = '/Users/renadcute/Desktop/Advanced workbook/task5/empty.xml' # path to the xml file #!this is an ampty file
# xmlfile = '/Users/renadcute/Desktop/Advanced workbook/task5/malformed.xml' # path to the xml file, this is a malformed file
# xmlfile = '/Users/renadcute/Desktop/Advanced workbook/task5/sample2.xml' # path to the xml file, this is a valid file
xmlfile = '/Users/renadcute/Desktop/Advanced workbook/task5/sample.xml' # path to the xml file, this is a broken file

try:
    tree = ET.parse(xmlfile) # parse the xml file 
    root = tree.getroot() # get the root of the xml file 
except (ET.ParseError):
    print(' The file is empty or invalid')
    exit()

# a function to find broken elements in the xml file 
broken_elements = []
def find_broken_element(element, path=''):
    current_path = f"{path}/{element.tag}" if path else element.tag

    #iterating through the attributes of the element 
    for attribute_name, attribute_value in element.attrib.items():
        # defining what broken element is 
        if attribute_value in ('null', 'None', '', 'unknown'):
            broken_elements.append(f'Broken element: {attribute_name}="{attribute_value}" at {current_path}')

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