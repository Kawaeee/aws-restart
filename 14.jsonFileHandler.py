import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
    
    
# fileName = "14.insulin.json"
# data = readJsonFile(fileName)