#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
def name_of_email(addr):
    m=re.match(r'^(.+)(@)(\w[a-z]+)(.\w{2,3})$',addr)
    # print(m.group(1))
    if '<' in m.group(1):
        L=re.split('[>\<]',m.group(1))
        print(L[1])
    else:
        print(m.group(1))

if __name__ == '__main__':
    name_of_email('tom@gmail.com')
    name_of_email('<Tom Paris> tom@voyager.org')