'''
문제: 2×n 타일링(https://www.acmicpc.net/problem/11726)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n)
'''
from typing import List


def solution(n: int) -> int:
    if n == 1:
        return 1
    dp: List[int] = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    return dp[n]


def main():
    n: int = int(input())
    print(solution(n))


if __name__ == '__main__':
    main()
