with open('input.txt', 'rt', encoding='utf-8') as i:
    lines = list(i.readlines())
    print(*lines[::-1], sep = '')