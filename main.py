class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за Домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}

    def average_rate(self):
        self.average = round(sum(sum(self.grades1.values(), [])) / len(sum(self.grades1.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_rate()} '
        return res


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


Anna_student = Student('Anna', 'Petrova', 'female')
Victor_student = Student('Victor', 'Chadov', 'Male')
Anna_student.finished_courses += ['Введение в программирование']
Anna_student.courses_in_progress += ['Python', 'Git']
Victor_student.finished_courses += ['Введение в программирование', 'GIT']
Victor_student.courses_in_progress += ['Python']

Ivan_mentor = Mentor('Ivan', 'Ivanov')
Olga_mentor = Mentor('Olga', 'Smirnova')

Alexandr_lecturer = Lecturer('Alexandr', 'Gaer')
Rita_lecturer = Lecturer('Rita', 'Smirnova')
Alexandr_lecturer.courses_attached += ['Python', 'Git']
Rita_lecturer.courses_attached += ['Python', 'Git']

Vladimir_reviewer = Reviewer('Vladimir', 'Dudarev')
Darya_reviewer = Reviewer('Darya', 'Dugina')
Vladimir_reviewer.courses_attached += ['Python', 'Git']
Darya_reviewer.courses_attached += ['Python', 'Git']

Anna_student.rate_lecturer(Alexandr_lecturer, 'Python', 9)
Anna_student.rate_lecturer(Rita_lecturer, 'Python', 7)
Victor_student.rate_lecturer(Alexandr_lecturer, 'Python', 10)
Anna_student.rate_lecturer(Rita_lecturer, 'Python', 9)
Victor_student.rate_lecturer(Alexandr_lecturer, 'Python', 8)

Vladimir_reviewer.rate_hw(Anna_student, 'Python', 9)
Vladimir_reviewer.rate_hw(Victor_student, 'Python', 10)
Darya_reviewer.rate_hw(Victor_student, 'Python', 10)
Darya_reviewer.rate_hw(Victor_student, 'Python', 7)
Darya_reviewer.rate_hw(Victor_student, 'Python', 9)
Vladimir_reviewer.rate_hw(Anna_student, 'Git', 8)

Anna_student.average_grade()
Victor_student.average_grade()
print(Anna_student < Victor_student)
print(Anna_student)
print(Victor_student)

Alexandr_lecturer.average_rate()
Rita_lecturer.average_rate()
print(Alexandr_lecturer < Rita_lecturer)
print(Alexandr_lecturer)
print(Rita_lecturer)

print(Vladimir_reviewer)
print(Darya_reviewer)

student_list = [Anna_student, Victor_student]


def grade_av_student(student_list, course):
    sum = 0
    count = 0
    for person in student_list:
        for i in person.grades[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


lecturer_list = [Alexandr_lecturer, Rita_lecturer]


def grade_av_lecturer(lecturer_list, course):
    sum = 0
    count = 0
    for person in lecturer_list:
        for i in person.grades1[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


print(grade_av_student(student_list, 'Python'))
print(grade_av_lecturer(lecturer_list, 'Python'))
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
