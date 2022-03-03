'''
문제: 쉬운 계단 수(https://www.acmicpc.net/problem/10844)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n)
'''
from typing import List


def solution(n) -> int:
    dp: List[List[int]] = [[0 for row in range(10)] for col in range(n + 1)]
    for i in range(10):
        dp[1][i] = 1
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1, 9):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
    return sum(dp[n]) % % 1000000000


def main():
    n: int = int(input())
    print(solution(n))


if __name__ == '__main__':
    main()
