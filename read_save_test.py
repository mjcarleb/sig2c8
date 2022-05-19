import xml.etree.ElementTree as ET
import pathlib

def traverse_and_fix(node, parent_of_node):

    children = node.getchildren()
    if len(children) == 0:
        if "signavio" in node.tag:
            parent_of_node.remove(node)
    else:
        for child in children:
            traverse_and_fix(node=child, parent_of_node=node)


in_xml = "data/basic_with_gateway.bpmn"
suffix = pathlib.Path(in_xml).suffix
out_xml = f"{in_xml[:len(in_xml)-len(suffix)]}_C8{suffix}"

# create element tree object
tree = ET.parse(in_xml)

# get root element
root = tree.getroot()
root[0].attrib['isExecutable'] = "true"

traverse_and_fix(node=root, parent_of_node=None)

tree.write(out_xml)
