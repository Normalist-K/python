# 피보나치 수열

import sys
sys.stdin = open("project03-1.txt", "r")

def fibo(n):
    if n in (1, 2):
        return 1

    return fibo(n-1) + fibo(n-2)

def fibo_dp(n):
    fibo = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i in (1, 2):
            fibo[i] = 1
        else:
            fibo[i] = fibo[i-1] + fibo[i-2]
    
    return fibo[-1]

def fibo_dp2(n):
    
    for i in range(1, n + 1):
        if i in (1, 2):
            fibo_last = 1
            fibo_i = 1
            fibo_ii = 1
        else:
            fibo_last = fibo_i + fibo_ii
            fibo_i = fibo_ii
            fibo_ii = fibo_last

    return fibo_last    

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(fibo_dp2(N))
