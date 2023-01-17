# importing element tree
import xml.etree.ElementTree as ET

path = r'\\10.88.22.128\dbs\bson\Для Саши Б\test.xls'
tree = ET.parse(path)

root = tree.getroot()

# print the root (parent) tag along with its memory location
print(root)
print(tree)
