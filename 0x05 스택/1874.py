# 스택 수열 
'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었따가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순이어야 한다고 하자. 임의의 수열이 주어졌을 때, 스택을 이용하여 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아내는 프로그램을 작성하라.

첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1 이상 n 이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.
입력되는 수열이 스택으로 만들 수 없는 경우에는 NO를 출력하고, 만들 수 있는 경우에는 push 연산은 +로, pop 연산은 -로 한 줄에 한 문자씩 출력한다. 이때, 가능한 답이 여러 가지인 경우에는 아무거나 출력한다.
'''

import sys
input = sys.stdin.readline
n = int(input())
stack = []
result = []
current = 1
possible = True
for _ in range(n):
    target = int (input())
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break
if possible == False:
    print("NO")
else:
    print('\n'.join(result))
