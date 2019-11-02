from update import *
import csv
import json
def Invest(name, vol):
    with open('data.json') as json_data:
        loaded_json = json.loads(json_data.read())
        for x in loaded_json:
            if x == "NAME":
                company = loaded_json[x]
                break
        for x in loaded_json:
            if x == "PRESENT_VALUE":
                price = loaded_json[x]
                break
        update(name, vol, price, company)
    
