from itertools import permutations


def solution(k, dungeons):
    answer = -1
    now_k = k
    cases = list(permutations(dungeons))
    for case in cases:
        count = 0
        for need, use in case:
            if now_k >= need:
                now_k -= use
                count += 1
                answer = max(answer, count)
            else:
                now_k = k
                break

    return answer
