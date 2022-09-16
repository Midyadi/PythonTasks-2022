import collections
n = int(input())
with open('input.txt', 'rt', encoding = 'utf-8') as i:
    words = i.read().split()
    common = collections.Counter(words).most_common(n)
    for word in common:
        print(word[0])