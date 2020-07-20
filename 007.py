#! /usr/bin/env python

for i in range(2,10,1):
    for j in range(1,10,1):
        if i % 2 == 0:
            print(f"{i} X {j} = {i*j}")
