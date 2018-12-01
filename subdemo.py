#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing as mp
from multiprocessing import Process,Pipe,Queue
import os,time,random
def f(q):
    q.put('你好')
    time.sleep(random.random())

if __name__ == '__main__':
    ctx=mp.get_context('spawn')
    p=ctx.Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()


