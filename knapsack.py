import sys
sys.setrecursionlimit(5500)

def read_input(path):
    with open(path) as f:
        lines = f.readlines()
    n = int(lines[0].split(' ')[0])
    capacity = int(lines[0].split(' ')[1])
    wt = [int(x.split(' ')[0]) for x in lines[1:]]
    val = [int(x.split(' ')[1]) for x in lines[1:]]
    return capacity, wt, val, n

def knapsack(capacity, wt, val, n):
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for cap in range(1, capacity + 1):
            if wt[i - 1] <= cap:
                dp[i][cap] = max(val[i - 1] + dp[i - 1][cap - wt[i - 1]], dp[i - 1][cap])
            else:
                dp[i][cap] = dp[i - 1][cap]

    example_optional_set: set = set()
    _construct_solution(dp, wt, n, capacity, example_optional_set)

    return dp[n][cap], dp, example_optional_set

def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


capacity, wt, val, n = read_input('.\instances\mochila00.txt.txt')

optimal_solution, _, optimal_set = knapsack(capacity, wt, val, n)

print(f'optimal max value : {optimal_solution}\nchosen products : {optimal_set}')