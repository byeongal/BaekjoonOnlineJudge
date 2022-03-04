'''
문제: 가장 긴 증가하는 부분 수열 4(https://www.acmicpc.net/problem/14002)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n^2)
'''
from typing import List


def solution(number: List[int]) -> int:
    answer: int = 1
    answer_idx: int = 0
    dp: List[int] = [1] * len(number)
    from_idxs: List[int] = [-1] * len(number)

    for i in range(len(number)):
        for j in range(i):
            if number[i] > number[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    from_idxs[i] = j
        if answer < dp[i]:
            answer = dp[i]
            answer_idx = i
    stack = []
    cur_idx = answer_idx
    while cur_idx != -1:
        stack.append(str(number[cur_idx]))
        cur_idx = from_idxs[cur_idx]
    return answer, stack[::-1]


def main():
    n: int = int(input())
    numbers: List[int] = list(map(int, input().split()))
    answer, answer_sequence = solution(numbers)
    print(answer)
    print(' '.join(answer_sequence))


if __name__ == '__main__':
    main()
