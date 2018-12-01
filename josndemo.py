#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
python_obj=[[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)},True,False,None]
json_str=json.dumps(python_obj,sort_keys=True,indent=2)
print(json_str)
print(type(json_str))