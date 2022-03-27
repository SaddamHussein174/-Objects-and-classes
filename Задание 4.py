
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def middle_grades(self):
        count = 0
        for element in self.grades.values():
            count += len(element)
        return sum(map(sum, self.grades.values()))/count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.middle_grades}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    @property
    def middle_grades(self):
        count = 0
        for element in self.grades.values():
            count += len(element)
        return sum(map(sum, self.grades.values())) / count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.middle_grades}\n')


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_mentor = Reviewer('Some', 'Buddy')
best_mentor.courses_attached += ['Python']
best_mentor.courses_attached += ['Git']

best_mentor.rate_hw(best_student, 'Python', 10)
best_mentor.rate_hw(best_student, 'Python', 8)
best_mentor.rate_hw(best_student, 'Git', 7)
best_mentor.rate_hw(best_student, 'Git', 9)

best_teach = Lecturer('Some', 'Buddy')

best_student.rate_lecturer(best_teach, 'Python', 4)
best_student.rate_lecturer(best_teach, 'Python', 6)
best_student.rate_lecturer(best_teach, 'Git', 6)
best_student.rate_lecturer(best_teach, 'Git', 5)

print(best_student)
print(best_mentor)
print(best_teach)



