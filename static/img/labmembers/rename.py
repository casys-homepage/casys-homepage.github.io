#!/usr/bin/python
import os
ls = os.listdir('.')
cache_access_traces = [elem for elem in ls if "students" in elem or "labmember" in elem]
for elem in cache_access_traces:
    ori_name = elem
    new_name = elem.replace("__", "_")
    os.system("mv " + ori_name + " " + new_name)
