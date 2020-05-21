import sys
sys.setrecursionlimit(21000)

def pi(accuracy,total=0):
    if accuracy == 0: return total
    else: return pi(accuracy-1,(-1/(accuracy*2-1) if accuracy%2==0 else 1/(accuracy*2-1))+total)

print(4*pi(1000))
