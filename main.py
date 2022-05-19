import xml.etree.ElementTree as ET

xmlfile = "data/basic_with_gateway.bpmn"
# create element tree object
tree = ET.parse(xmlfile)

# get root element
root = tree.getroot()

root[0].attrib['isExecutable'] = "true"
tree.write(xmlfile)
a=3