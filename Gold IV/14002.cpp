/*
문제: 가장 긴 증가하는 부분 수열 4(https://www.acmicpc.net/problem/14002)
분류: 다이나믹 프로그래밍
시간 복잡도: O(n^2)
 */
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> &numbers)
{
    vector<int> answer;
    vector<int> memo(numbers.size(), 1);
    vector<int> sourceIdx(numbers.size(), -1);
    int maxValue = 1, maxIdx = 0;
    for (int i = 1; i < numbers.size(); i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (numbers[j] < numbers[i])
            {
                if (memo[j] + 1 > memo[i])
                {
                    memo[i] = memo[j] + 1;
                    sourceIdx[i] = j;
                    if (maxValue < memo[i])
                    {
                        maxValue = memo[i];
                        maxIdx = i;
                    }
                }
            }
        }
    }
    stack<int> st;
    while (maxIdx != -1)
    {
        st.push(numbers[maxIdx]);
        maxIdx = sourceIdx[maxIdx];
    }
    while (!st.empty())
    {
        answer.push_back(st.top());
        st.pop();
    }
    return answer;
}
int main()
{
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++)
    {
        cin >> numbers[i];
    }
    vector<int> answer = solution(numbers);
    cout << answer.size() << '\n';
    for (int each : answer)
    {
        cout << each << ' ';
    }
    return 0;
}