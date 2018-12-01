#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
class SearchFile(object):
    def __init__(self,path,str):
        self.path=path
        self.str=str

    def search(self):
        dirs=os.path.abspath(self.path)
        for subpath in os.listdir(self.path):
            full_path=os.path.join(dirs,subpath)
            if os.path.isdir(full_path):
                SearchFile(self.path,self.str)
            else:
                if self.str in subpath:
                    print(full_path)
if __name__ == '__main__':
    SearchFile('.','.py').search()

