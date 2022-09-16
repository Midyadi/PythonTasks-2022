with open('input.txt', 'r', encoding='utf-8') as i:
    pupils = [pupil.strip().split() for pupil in i.readlines()]
    max_grades_schools = set()
    max_grade = int(max(pupils, key = lambda x: int(x[-1]))[-1])
    for pupil in pupils:
        if int(pupil[-1])==max_grade:
            max_grades_schools.add(int(pupil[-2]))
    print(*sorted(max_grades_schools))