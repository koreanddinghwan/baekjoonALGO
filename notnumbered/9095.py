import collections
from itertools import count
import sys
count = 0
def NOde(n,m):
    global count
    count += 1
    next_node = NOde(m)