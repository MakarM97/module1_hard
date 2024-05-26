grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


student_grades = dict(zip(students, grades))

average_grades = {}
for student, grades_list in sorted(student_grades.items()):
    average_grade = sum(grades_list) / len(grades_list)
    average_grades[student] = average_grade

print(average_grades) # тут есть алфавитный порядок у студентов

grades_dict = {}
for i in range(len(students)):
    total_grades = sum(grades[i])
    avg_grade = total_grades / len(grades[i])
    grades_dict[list(students)[i]] = avg_grade

print(grades_dict) # тут есть алфавитный порядок у оценок, но как сделать, чтобы вместе работало, я не могу понять