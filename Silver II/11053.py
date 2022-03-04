'''
문제: 가장 긴 증가하는 부분 수열(https://www.acmicpc.net/problem/11053)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n^2)
'''
from typing import List


def solution(number: List[int]) -> int:
    answer: int = 1
    dp: List[int] = [1] * len(number)
    for i in range(len(number)):
        for j in range(i):
            if number[i] > number[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


def main():
    n: int = int(input())
    numbers: List[int] = list(map(int, input().split()))
    print(solution(numbers))


if __name__ == '__main__':
    main()
