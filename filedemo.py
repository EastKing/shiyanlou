#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
obj = dict(name='小明', age=20)
s=json.dumps(obj,ensure_ascii=True)
print(s)
print(type(s))





