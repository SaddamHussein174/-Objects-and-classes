
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = 0

    def grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def middle_grades(self):
        count = 1
        for element in self.grades.values():
            count += len(element)
        return \
            sum(map(sum, self.grades.values())) / count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.middle_grades}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('не Student')
            return \
                self.middle_grades() < other.middle_grades()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('не Student')
            return \
                self.middle_grades() < other.middle_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = ['Python', 'git']
        self.grades = {}
        self.average_grade = 0

    def middle_grades(self):
        count = 1
        for element in self.grades.values():
            count += len(element)
        return \
            sum(map(sum, self.grades.values())) / count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.middle_grades}\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('не Lecturer')
            return
        return self.middle_grades() > other.middle_grades()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('не Lecturer')
            return
        return self.middle_grades() < other.middle_grades()


def average_grade_student(students, course):
    if len(students):
        sum_ = 0
        for student in students:
            if isinstance(student, Student) and student.grades and course in student.grades:
                sum_ = sum_ + sum(student.grades[course])
            return sum_ / len(students)
    else:
        return 0


def average_grade_lecturer(lecturers, course):
    if len(lecturers):
        sum_ = 0
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and lecturer.grades and course in lecturer.grades:
                sum_ = sum_ + sum(lecturer.grades[course])
        return sum_ / len(lecturers)
    else:
        return 0


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

student1 = Student('Дмитрий', 'Трисмаков', 'м')
student2 = Student('Марат', 'Мовламов', 'м')

lecturer1 = Lecturer('Олег', 'Булыгин')
lecturer2 = Lecturer('Елена', 'Никитина')

reviewer1 = Reviewer('Александр', 'Бардин')
reviewer2 = Reviewer('Олег', 'Булыгин')

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'git', 5)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'git', 10)

student1.grade_lecturer(lecturer1, 'Python', 10)
student1.grade_lecturer(lecturer1, 'Python', 9)
student1.grade_lecturer(lecturer1, 'git', 10)
student1.grade_lecturer(lecturer1, 'git', 10)

student2.grade_lecturer(lecturer1, 'Python', 10)
student2.grade_lecturer(lecturer1, 'Python', 9)
student2.grade_lecturer(lecturer1, 'git', 10)

if student1 > student2:
    print(f'{student1.name} > {student2.name}\n')
else:
    print(f'{student1.name} < {student2.name}\n')
if student2 > student1:
    print(f'{student2.name} > {student1.name}\n')

if lecturer1 < lecturer2:
    print(f'{lecturer1.name} < {lecturer2.name}\n')
else:
    print(f'{lecturer1.name} > {lecturer2.name}\n')

print(f'Проверяющий: \n{reviewer1}\n')
print(f'Лектор: \n{lecturer1}\n')
print(f'Студент: \n{student1}\n')
print(f'Студент: \n{student2}\n')

print(student1.name, student1.grades)
print(student2.name, student2.grades)

print(f"Сердний бал по Python у студентов:  {average_grade_student([student1, student2], 'Python')}")
print(f"Сердний бал по git у студентов: {average_grade_student([student1, student2], 'git')}")

print(f"Сердний бал по Python у лекторов: {average_grade_lecturer([lecturer1, lecturer2], 'Python')}")
print(f"Сердний бал git лекторов: {average_grade_lecturer([lecturer1, lecturer2], 'git')}")

