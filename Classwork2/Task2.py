import itertools as iter
with open('input.txt', 'rt', encoding = 'utf-8') as i, open('output.txt', 'w', encoding='utf-8') as o:
    count,*lines = i.readlines()
    for number,line in zip(iter.cycle(range(int(count))), lines):
        print(number,line, file = o, end = '')