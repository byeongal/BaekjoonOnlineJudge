'''
문제: 제곱수의 합(https://www.acmicpc.net/problem/1699)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n * sqrt(n))
'''
from typing import List


def solution(n: int) -> int:
    dp: List[int] = [each for each in range(n + 1)]
    for i in range(2, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i-j*j] + 1)
            j += 1
    return dp[n]


def main():
    n: int = int(input())
    print(solution(n))


if __name__ == '__main__':
    main()
