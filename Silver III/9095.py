'''
문제: 1, 2, 3 더하기()
분류: 다이나믹 프로그래밍
시간 복잡도: O(n)
'''
from typing import List


def solution(n: int, memo: List[int]) -> int:
    if n < 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = solution(n-1, memo) + solution(n-2, memo) + solution(n-3, memo)
    return memo[n]


def main():
    t: int = int(input())
    memo: List[int] = [-1] * 12
    memo[0] = 1
    memo[1] = 1
    for _ in range(t):
        n: int = int(input())
        print(solution(n, memo))


if __name__ == '__main__':
    main()
