grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = {} # создание пустого словаря.
for a, student in enumerate(sorted(students)): # для переменной "a" оперант Enumerate как счетчик считывается с 0 или выставляет по порядку значения. Sorted - сортировать список.
    average_grades[student] = sum(grades[a]) / len(grades[a]) # средние оценки по отработанному списку студентов в алф.порядке по формуле = сумма оценок / количество.
    print(average_grades)

student_name = input("Введите имя студента: ")
if student_name in average_grades:
    print(f"Средний балл {student_name}: {average_grades[student_name]}") # вывести из множества студентов со средним баллом.
else:
    print("Студента с таким именем нет в списке.") # писать строго с заглавной буквы имя!
