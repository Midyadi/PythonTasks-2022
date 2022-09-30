with open('input.txt', 'r', encoding='utf-8') as i:
    max_grades = [0, 0, 0]
    pupils = [pupil.strip().split() for pupil in i.readlines()]
    for pupil in pupils:
        grade, mark = [int(i) for i in pupil[-2:]]
        if mark > max_grades[grade - 9]:
            max_grades[grade - 9] = mark
    print(*max_grades)
