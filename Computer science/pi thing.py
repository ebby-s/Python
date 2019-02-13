import sys
sys.setrecursionlimit(20500)

def pi(accuracy,total=0):
    if accuracy == 0: return total
    else: return pi(accuracy-1,do_thing(accuracy)+total)

def do_thing(accuracy):
    if accuracy%2 == 0: return -1/(accuracy*2-1)
    else: return 1/(accuracy*2-1)

print(4*pi(20490))
