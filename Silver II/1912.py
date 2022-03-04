'''
문제: 연속합(https://www.acmicpc.net/problem/1912)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n)
'''
from typing import List


def solution(number: List[int]) -> int:
    dp: List[int] = number[:]
    for i in range(1, len(number)):
        dp[i] = max(dp[i-1] + number[i], dp[i])
    return max(dp)


def main():
    n: int = int(input())
    numbers: List[int] = list(map(int, input().split()))
    print(solution(numbers))


if __name__ == '__main__':
    main()
