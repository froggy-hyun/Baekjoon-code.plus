# import sys
# input = sys.stdin.readline

count = int(input())
arr = list(map(int, input().split()))
print(min(arr) * max(arr))
