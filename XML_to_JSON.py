import xml.etree.ElementTree as ET
import json

def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    json_data = {}
    json_data[root.tag] = parse_element(root)
    return json.dumps(json_data, indent=4)

def parse_element(element):
    if len(element) == 0:
        return element.text
    else:
        data = {}
        for child in element:
            child_data = parse_element(child)
            if child.tag in data:
                if isinstance(data[child.tag], list):
                    data[child.tag].append(child_data)
                else:
                    data[child.tag] = [data[child.tag], child_data]
            else:
                data[child.tag] = child_data
        return data

if __name__ == "__main__":
    with open("XML file here", "r") as xml_file:
        xml_string = xml_file.read()
    json_output = xml_to_json(xml_string)
    print(json_output)
