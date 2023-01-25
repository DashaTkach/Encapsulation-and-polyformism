class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_2mentor(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades_from_students:
                mentor.grades_from_students[course] += grade
            else:
                mentor.grades_from_students[course] = grade
        else:
            return 'Ошибка'

    def avr(self):
        certain_list = list(self.grades.values())
        return sum(certain_list) / len(certain_list)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avr()} ' \
              f'\nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы:: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Error')
            return
        return self.avr() < other.avr()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def avr(self):
        certain_list = list(self.grades_from_students.values())
        return sum(certain_list) / len(certain_list)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avr()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Error')
            return
        return self.avr() < other.avr()

    # def avr_all(self, other):
    #     avrall = {}
    #     for course in self.courses_attached:
    #         if isinstance(other, Lecturer):
    #             avrall[course] = (self.avr() + other.avr()) / 2
    #     return avrall
#  ПОПЫТАЛАСЬ СДЕЛАТЬ ПОДСЧЕТ СРЕДНЕЙ ОЦЕНКИ ПО ОДНОМУ КУРСУ - НЕ ПОЛУЧИЛОСЬ

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# Проверка работы кода = реализация всех методов:

# выставление оценок лекторам студентами и стедентам экспертами


first_student = Student('Ruoy', 'Eman', 'boy')
second_student = Student('Mary', 'Oman', 'girl')

cool_mentor = Reviewer('Josh', 'Key')
bad_mentor = Reviewer('Bill', 'Roller')
cool_lecturer = Lecturer('Pall', 'Allen')
bad_lecturer = Lecturer('Olga', 'Fell')

first_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Python']
cool_mentor.courses_attached += ['Python']
bad_mentor.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Python']
first_student.courses_in_progress += ['Web']
second_student.courses_in_progress += ['Web']
cool_mentor.courses_attached += ['Web']
bad_mentor.courses_attached += ['Web']
cool_lecturer.courses_attached += ['Web']
bad_lecturer.courses_attached += ['Web']
first_student.courses_in_progress += ['Java']
second_student.courses_in_progress += ['Java']
cool_mentor.courses_attached += ['Java']
bad_mentor.courses_attached += ['Java']
cool_lecturer.courses_attached += ['Java']
bad_lecturer.courses_attached += ['Java']

first_student.finished_courses += ['JavaScr']
second_student.finished_courses += ['JavaScr']
first_student.finished_courses += ['RStudio']
second_student.finished_courses += ['RStudio']

cool_mentor.rate_hw(first_student, 'Python', 10)
cool_mentor.rate_hw(first_student, 'Web', 9)
cool_mentor.rate_hw(first_student, 'Java', 9.5)
cool_mentor.rate_hw(second_student, 'Python', 4)
cool_mentor.rate_hw(second_student, 'Web', 2)
cool_mentor.rate_hw(second_student, 'Java', 3)

bad_mentor.rate_hw(first_student, 'Python', 8)
bad_mentor.rate_hw(first_student, 'Web', 7)
bad_mentor.rate_hw(first_student, 'Java', 9)
bad_mentor.rate_hw(second_student, 'Python', 3)
bad_mentor.rate_hw(second_student, 'Web', 1)
bad_mentor.rate_hw(second_student, 'Java', 2)

print(f'Оценки первого студента: {first_student.grades}')
print(f'Оценки второго студента: {second_student.grades}')

first_student.grade_2mentor(cool_lecturer, 'Python', 8)
first_student.grade_2mentor(cool_lecturer, 'Web', 9)
first_student.grade_2mentor(cool_lecturer, 'Java', 10)
first_student.grade_2mentor(bad_lecturer, 'Python', 2)
first_student.grade_2mentor(bad_lecturer, 'Web', 3)
first_student.grade_2mentor(bad_lecturer, 'Java', 5)

second_student.grade_2mentor(cool_lecturer, 'Python', 9)
second_student.grade_2mentor(cool_lecturer, 'Web', 9)
second_student.grade_2mentor(cool_lecturer, 'Java', 9)
second_student.grade_2mentor(bad_lecturer, 'Python', 3)
second_student.grade_2mentor(bad_lecturer, 'Web', 5)
second_student.grade_2mentor(bad_lecturer, 'Java', 4)

print(f'Оценки крутого лектора: {cool_lecturer.grades_from_students}')
print(f'Оценки плохого лектора: {bad_lecturer.grades_from_students}')

# вывести str() для всех классов

print(first_student)
print(second_student)
print(cool_mentor)
print(bad_mentor)
print(cool_lecturer)
print(bad_lecturer)

# сравнение лекторов и студентов по средним баллам

print(first_student.__lt__(second_student))
print(second_student.__lt__(first_student))

print(cool_lecturer.__lt__(bad_lecturer))
print(bad_lecturer.__lt__(cool_lecturer))

# подсчет средней оценки по всем студентам и лекторам

