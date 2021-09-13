class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def put_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sum_len = 0
        sum_grade = 0
        for value in self.grades.values():
            for grade in value:
                sum_len += 1
                sum_grade += grade
        result = sum_grade / sum_len
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'\
            f'Средняя оценка за домашние задания: {result} \n'\
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'\
            f'Завершённые курсы: {", ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def put_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# def avr(dict_1):
#     sum_len = 0
#     sum_grade = 0
#     for value in dict_1.value():
#         sum_len += len(dict_1)
#         for grade in value:
#             sum_grade += grade
#     return sum_grade / len(dict_1)

cool_lecturer = Lecturer('Som', 'Bud')
cool_lecturer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'GIT']
best_student.put_grade(cool_lecturer, 'Python', 10)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_reviewer.put_grade(best_student, 'Python', 10)
cool_reviewer.put_grade(best_student, 'Python', 9.5)
cool_reviewer.put_grade(best_student, 'GIT', 9)

print(best_student.grades)
print(cool_lecturer.grades)
print(best_student)