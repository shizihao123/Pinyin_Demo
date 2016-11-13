# !/bin/bash
import json

def json_load(file_name= "base_start.json"):
    f = open("/home/jun/workspace/Pinyin_Demo/json2sqlite/" + file_name, "r")
    s = json.load(f)
    # for i in s.keys():
    #     print i, s[i]
    return s


# print s["name"]
# print s["type"]["name"]