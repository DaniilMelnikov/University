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
list_student = []
lecturer_list = []

def student_avr_mark(student_list, course):
    count = 0
    sum_avr_grade = 0
    for student in student_list:
        if isinstance(student, Student) and course in student.finished_courses or course in student.courses_in_progress:
            count += 1
            sum_len = 0
            sum_grade = 0
            for value in student.grades.values():
                for grade in value:
                    sum_len += 1
                    sum_grade += grade
            student.student_avr_grade = sum_grade / sum_len
            sum_avr_grade += student.student_avr_grade
        else:
            return 'Ошибка'
    result = sum_avr_grade / count
    return print(f'Курс: {course} {result}')

def lecturer_avr_mark(lecturer_list, course):
    count = 0
    sum_avr_grade = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            count += 1
            sum_len = 0
            sum_grade = 0
            for value in lecturer.grades.values():
                for grade in value:
                    sum_len += 1
                    sum_grade += grade
            lecturer.lecturer_avr_grade = sum_grade / sum_len
            sum_avr_grade += lecturer.lecturer_avr_grade
        else:
            return 'Ошибка'
    result = sum_avr_grade / count
    return print(f'Курс: {course} {result}')

Python_lecturer = Lecturer('Python', 'Javov')
Python_lecturer.courses_attached += ['Python']

GIT_lecturer = Lecturer('Git', 'Consolov')
GIT_lecturer.courses_attached += ['GIT']

best_student = Student('Eda', 'Eldis', 'woman')
best_student.courses_in_progress += ['Python', 'GIT']
best_student.finished_courses += ['English']
best_student.put_grade(Python_lecturer, 'Python', 10)
best_student.put_grade(GIT_lecturer, 'GIT', 9)

other_student = Student('Serkan', 'Boulat', 'man')
other_student.courses_in_progress += ['Python', 'GIT']
other_student.finished_courses += ['English']
other_student.put_grade(Python_lecturer, 'Python', 8)
other_student.put_grade(GIT_lecturer, 'GIT', 8)

cool_reviewer = Reviewer('Funny', 'Flower')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_reviewer.put_grade(best_student, 'English', 8)
cool_reviewer.put_grade(best_student, 'Python', 10)
cool_reviewer.put_grade(best_student, 'GIT', 10)

cool_reviewer.put_grade(other_student, 'English', 10)
cool_reviewer.put_grade(other_student, 'GIT', 9)
cool_reviewer.put_grade(other_student, 'GIT', 9)

other_reviewer = Reviewer('Allknower', 'Masterov')

other_reviewer.put_grade(best_student, 'English', 9)
other_reviewer.put_grade(best_student, 'Python', 8)
other_reviewer.put_grade(best_student, 'GIT', 10)

other_reviewer.put_grade(other_student, 'English', 9)
other_reviewer.put_grade(other_student, 'Python', 8)
other_reviewer.put_grade(other_student, 'GIT', 10)

list_student.append(best_student)
list_student.append(other_student)
student_avr_mark(list_student, 'GIT')

lecturer_list.append(Python_lecturer)
lecturer_list.append(GIT_lecturer)
lecturer_avr_mark(lecturer_list, 'GIT')

print(best_student > other_student)
print(GIT_lecturer < Python_lecturer)
print(other_reviewer)
print(cool_reviewer)
print(Python_lecturer)
print(GIT_lecturer)
print(best_student)
print(other_student)