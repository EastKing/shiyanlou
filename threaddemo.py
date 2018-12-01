#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
def is_valid_email(addr):
    if re.match(r'^[a-zA-Z0-9_\.-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',addr):
        print('邮箱地址正确')
    else:
        print('邮箱地址错误')
def name_of_email(addr):
    m=re.match(r'^(.+)(@)(\w[a-z]+)(.\w{2,3})$',addr)
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.group(4))
    if m:
        if '<' in m.group(1):
            L=re.split(r'[>\<]',m.group(1))
            return L[1]
        else:
            return m.group(1)
    else:
        print('%s 是错误的邮箱地址'% addr)

if __name__ == '__main__':
    is_valid_email('someone@gmail.com')
    is_valid_email('bill.gates@microsoft.com')
    is_valid_email('bob#example.com')
    is_valid_email('mr-bob@gamil.com')
    print('ok')
    # assert name_of_email('tom@voyager.org')=='tom'
    assert name_of_email('<Tom Paris> tom@voyager.org')=='Tom Paris'


