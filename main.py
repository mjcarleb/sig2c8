import xml.etree.ElementTree as ET

xmlfile = "data/basic_with_gateway_SIG.bpmn"
# create element tree object
tree = ET.parse(xmlfile)

# get root element
root = tree.getroot()
root[0].attrib['isExecutable'] = "true"

n_elements = len(root[0])

tree.write(xmlfile)


def traverse(node, parent_of_node):

    children = node.getchildren()
    if len(children) == 0:
        if "signavio" in node.tag:
            print(node)
            parent_of_node.remove(node)
    else:
        for child in children:
            traverse(node=child, parent_of_node=node)

a=3

traverse(node=root, parent_of_node=None)

a=3

tree.write("data/removed_signavio.bpmn")
