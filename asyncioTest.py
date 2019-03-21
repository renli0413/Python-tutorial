#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:51:54 2019

@author: leon
"""
import asyncio
import time
async def add(x=1, y=2):
    print("Add {} + {} ...".format(x,y))
    await asyncio.sleep(2)
    return x + y

s=time.time()
loop = asyncio.get_event_loop()
tasks=[loop.create_task(add(1,2)),
       loop.create_task(add(11,12)),
       loop.create_task(add(111,112))]
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print(task.result())
print('cost:',time.time()-s)


