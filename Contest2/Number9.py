with open('input.txt', 'r', encoding='utf-8') as i:
    pupils = [[int(i) for i in pupil.strip().split()[-2:]]for pupil in i.readlines()]
    counts = [0,0,0]
    sums = [0,0,0]
    for pupil in pupils:
        grade, mark = pupil
        counts[grade - 9] += 1
        sums[grade - 9] +=mark
    for count, sum in zip(counts, sums):
        print(sum/count, end = ' ')

