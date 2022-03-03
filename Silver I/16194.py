'''
문제: 카드 구매하기 2(https://www.acmicpc.net/problem/16194)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n^2)
'''
from typing import List


def solution(prices: List[int]) -> int:
    n = len(prices)
    dp: List[int] = [0] * (n + 1)
    dp[1] = prices[0]
    for i in range(2, n + 1):
        dp[i] = prices[i-1]
        for j in range(1, i):
            dp[i] = min(dp[i], dp[i-j] + prices[j-1])
    return dp[n]


def main():
    n: int = int(input())
    prices: List[int] = list(map(int, input().split()))
    print(solution(prices))


if __name__ == '__main__':
    main()
