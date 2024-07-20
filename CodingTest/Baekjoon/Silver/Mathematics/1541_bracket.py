import sys
input = sys.stdin.readline

formula = input().rstrip()

first_minus_idx = formula.find('-')
if first_minus_idx == -1:
    answer = sum(map(int, formula.split('+')))
else:
    answer = sum(map(int, formula[:first_minus_idx].split('+')))
    answer -= sum(map(int, formula[first_minus_idx + 1:].replace('-', '+').split('+')))

# formula = input().rstrip()

# minusFormulas = list(formula.split(sep='-'))

# answer = sum(map(int, minusFormulas[0].split(sep='+')))

# for i in range(1, len(minusFormulas)):
#     answer -= sum(map(int, minusFormulas[i].split(sep='+')))

print(answer)