''' 예를들어 n=4 일때,
1 -> 1부터 4까지 모두 약수로 들어가고,
2 -> 2와 4
3 -> 3
4 -> 4
이므로, 1은 4번, 2는 2번, 3과4는 각각 한번 들어가는 것을 알 수 있다.
이와 같이 i가 n//i한 갯수만큼 가지고 있게 되는 것이다.

그 결과로 sum += (n//i) * i 라는 결과가 나오게 된다. '''

# import sys
# input = sys.stdin.readline

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += (n//i) * i
print(sum)
