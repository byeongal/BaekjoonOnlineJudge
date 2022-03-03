'''
문제: 이친수(https://www.acmicpc.net/problem/2193)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n)
'''
from typing import List


def solution(n) -> int:
    dp: List[List[int]] = [[0 for row in range(2)] for col in range(n + 1)]
    dp[1][1] = 1
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    return dp[n][0] + dp[n][1]


def main():
    n: int = int(input())
    print(solution(n))


if __name__ == '__main__':
    main()
