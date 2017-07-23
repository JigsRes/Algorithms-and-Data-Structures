# Enter your code here. Read input from STDIN. Print output to STDOUTimport os
import os

f = open(os.environ['OUTPUT_PATH'], 'w')


def solution():
    X = int(raw_input())
    N = int(raw_input())

    def powersum(match, power, base):
        difference = match - pow(base, power)
        if difference == 0:
            return 1
        if difference < 0:
            return 0
        if difference > 0:
            return powersum(difference, power, base + 1) + powersum(match, power, base + 1)

    return powersum(X, N, 1)


f.write(str(solution()) + "\n")

f.close()
