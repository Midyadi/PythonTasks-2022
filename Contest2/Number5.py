with open('input.txt', 'rt', encoding='utf-8') as i:
    lines = list(line.strip() for line in i.readlines())
    for line in lines[::-1]:
        print(line[::-1])
