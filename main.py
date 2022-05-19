import pathlib
import xml.dom.minidom

def traverse_and_fix(node):

    children = node.childNodes
    if len(children) == 0:
        if node.localName is not None and "signavio" in node.localName:
            node.parentNode.removeChild(node)
    else:
        for child in children:
            traverse_and_fix(node=child)

in_xml = "data/basic_with_gateway.bpmn"
suffix = pathlib.Path(in_xml).suffix
out_xml = f"{in_xml[:len(in_xml)-len(suffix)]}_C8{suffix}"

domtree = xml.dom.minidom.parse(in_xml)
root = domtree.documentElement


root.childNodes[1].attributes['isExecutable'].nodeValue = "true"

traverse_and_fix(node=root)

domtree.writexml(open(out_xml, "w"), encoding="UTF-8")
