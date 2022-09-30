with open('input.txt', 'r', encoding='utf-8') as i:
    pupils = sorted([pupil.strip().split() for pupil in i.readlines()], key=lambda x: x[0])
    for pupil in pupils:
        print(*pupil)
