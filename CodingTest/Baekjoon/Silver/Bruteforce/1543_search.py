docs = input()
target = input()

count = 0
i = 0
while i < len(docs) - len(target) + 1:
    if docs[i] == target[0]:
        j = 0
        while j < len(target):
            if docs[i + j] != target[j]:
                break
            j += 1
        if j == len(target):
            count += 1
            i = i + j
            continue
    i += 1

print(count)
