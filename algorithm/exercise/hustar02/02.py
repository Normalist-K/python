# 큐 구현하기

from collections import deque

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    queue = deque([])

    for _ in range(N):
        num = int(input())
        if num > 0:
            queue.append(num)
        else:
            print(queue.popleft())
