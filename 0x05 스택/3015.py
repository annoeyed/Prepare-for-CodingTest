# 오아시스 재결합
'''
오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.
이 역사적인 순간을 맞이하기 위해 줄에서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해졌다.
두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.
줄에 서 있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 줄에서 기다리고 있는 사람의 수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 2^31 나노미터보다 작다.
사람들이 서 있는 순서대로 입력이 주어진다.

서로 볼 수 있는 쌍의 수를 출력한다.
'''
import sys
input = sys.stdin.readline
n = int(input())
heights = [int(input()) for _ in range(n)]
stack = []
result = 0
for i in range(n):
    count = 1
    while stack and stack[-1][0] <= heights[i]:
        result += stack[-1][1]
        if stack[-1][0] == heights[i]:
            count += stack[-1][1]
        stack.pop()
    if stack:
        result += 1
    stack.append((heights[i], count))
print(result)