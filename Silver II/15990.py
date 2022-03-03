'''
문제: 1, 2, 3 더하기 5(https://www.acmicpc.net/problem/15990)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n)
'''
from typing import List


def solution(number: int, dp: List[List[int]]) -> int:
    return sum(dp[number]) % 1000000009


def init() -> List[List[int]]:
    dp: List[List[int]] = [[-1, -1, -1] for i in range(100001)]
    dp[0][0] = dp[0][1] = dp[0][2] = 0

    # 1 : 1
    dp[1][0] = 1
    dp[1][1] = dp[1][2] = 0

    # 2 : 2
    dp[2][0] = dp[2][2] = 0
    dp[2][1] = 1

    # 3 :1 + 2, 2 + 1, 3
    dp[3][0] = dp[3][1] = dp[3][2] = 1

    for i in range(4, 100001):
        for j in range(3):
            dp[i][j] = (dp[i - j - 1][(j + 1) % 3] +
                        dp[i - j - 1][(j + 2) % 3]) % 1000000009

    return dp


def main():
    n: int = int(input())
    dp: List[List[int]] = init()

    for i in range(n):
        number = int(input())
        print(solution(number, dp))


if __name__ == '__main__':
    main()
