from collections import deque
import sys
sys.stdin = open("input.txt", "r")

backward = deque([])
frontward = deque([])
access = []

n, q, c = map(int, input().split())
cap = [0]
cap += list(map(int, input().split()))

do = []



