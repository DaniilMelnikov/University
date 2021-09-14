class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def put_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
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
            f'Средняя оценка за домашние задания: {round(result, 1)} \n'\
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'\
            f'Завершённые курсы: {", ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other):
        sum_len = 0
        sum_grade = 0
        for value in self.grades.values():
            for grade in value:
                sum_len += 1
                sum_grade += grade
        self.result = sum_grade / sum_len
        sum_len = 0
        sum_grade = 0
        for value in other.grades.values():
            for grade in value:
                sum_len += 1
                sum_grade += grade
        other.result = sum_grade / sum_len
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.result < other.result

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        sum_len = 0
        sum_grade = 0
        for value in self.grades.values():
            for grade in value:
                sum_len += 1
                sum_grade += grade
        result = sum_grade / sum_len
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
            f'Средняя оценка за лекции: {round(result, 1)} \n'
        return res

    def __lt__(self, other):
        sum_len = 0
        sum_grade = 0
        for value in self.grades.values():
            for grade in value:
                sum_len += 1
                sum_grade += grade
        self.result = sum_grade / sum_len
        sum_len = 0
        sum_grade = 0
        for value in other.grades.values():
            for grade in value:
                sum_len += 1
                sum_grade += grade
        other.result = sum_grade / sum_len
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.result < other.result

class Reviewer(Mentor):
    def put_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        return res

Python_lecturer = Lecturer('Som', 'Bud')
Python_lecturer.courses_attached += ['Python']

GIT_lecturer = Lecturer('Othe', 'Green')
GIT_lecturer.courses_attached += ['GIT']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'GIT']
best_student.put_grade(Python_lecturer, 'Python', 10)
best_student.put_grade(GIT_lecturer, 'GIT', 9)

other_student = Student('Serkan', 'Boulat', 'man')
other_student.courses_in_progress += ['Python', 'GIT']
other_student.put_grade(Python_lecturer, 'Python', 8)
other_student.put_grade(GIT_lecturer, 'GIT', 1)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_reviewer.put_grade(best_student, 'Python', 10)
cool_reviewer.put_grade(best_student, 'Python', 10)
cool_reviewer.put_grade(best_student, 'GIT', 9)

cool_reviewer.put_grade(other_student, 'Python', 10)
cool_reviewer.put_grade(other_student, 'GIT', 9)
cool_reviewer.put_grade(other_student, 'GIT', 9)

print(best_student > other_student)
print(GIT_lecturer < Python_lecturer)
print(cool_reviewer)
print(Python_lecturer)
print(GIT_lecturer)
print(best_student)