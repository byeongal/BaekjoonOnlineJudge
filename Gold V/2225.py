'''
문제: 합분해(https://www.acmicpc.net/problem/2225)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n*n*k)
'''
from typing import List


def solution(n: int, k: int) -> int:
    dp: List[List[int]] = [[0 for col in range(n + 1)] for row in range(k + 1)]
    for i in range(0, n + 1):
        dp[1][i] = 1
    for i in range(1, k + 1):
        for j in range(0, n+1):
            for _k in range(j + 1):
                dp[i][j] += dp[i-1][j-_k]
                dp[i][j] %= 1000000000
    return dp[k][n]


def main():
    n, k = map(int, input().split())
    print(solution(n, k))


if __name__ == '__main__':
    main()
