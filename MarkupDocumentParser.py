# imports
import xml.etree.ElementTree as ET
import json

# xml file, "tree" = parsed XML, add to root
tree = ET.parse('WebService.xml')
root = tree.getroot() # ignore root.tag
# element.attrib, element.tag

# hold result, needs to be dictonary, get root name, and methods into [] list <-
result = {}
result["name"] = root.get("name")
result["methods"] = []

# we can hardcode just to abstract method since its only that basically
for methods in root.findall("abstract_method"): # just go to all methods in abstract method
    method = {} # CREATE DICTIONARY OF METHOD
    method["name"] = methods.get("name") # get method names
    method["modifier"] = methods.findtext("modifier") # get modifier texts



    parameters = methods.findall("parameters/parameter") # get all parameters

    if len(parameters) > 0: # if len is bigger than 0, we go to list
        parameter_list = []
        for i in parameters:
            parameter_list.append({"type": i.get("type"), "text": i.text}) # append all of it

        if len(parameter_list) == 1:
            parameter_list = parameter_list[0] # go to first element

        method["parameters"] = {"parameter": parameter_list} # parameter list added to method

    exceptions = methods.findall("exceptions/exception") # same as PARAMETERS code just appending

    if len(exceptions) > 0:
        exception_list = []
        for j in exceptions:
            exception_list.append(j.text)

        if len(exception_list) == 1:
            exception_list = exception_list[0]

        method["exceptions"] = {"exception": exception_list}

    method["return"] = methods.findtext("return") # add return
 
    result["methods"].append(method) # add to methods all of the code


# creating JSON file 
json_text = json.dumps(result, indent=2) # some tutorial json import code
print(json_text) # shows the json

with open("WebService.json", "w") as f:
    f.write(json_text) # makes the json