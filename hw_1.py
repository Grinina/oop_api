students_list = []
lectors_list = []
reviewer_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)
    def _average_score(self):
        count_scores = 0
        for i in self.grades.values():
            sum_scores = sum(i)
            for j in i:
                count_scores += 1
        self.average_score = round(sum_scores / count_scores, 1)
    def __str__(self):
        self._average_score()
        res = f'Имя: {self.name}\nФамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.average_score}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_score < other.average_score

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lectors_list.append(self)
    def _average_score(self):
        count_scores = 0
        for i in self.grades.values():
            sum_scores = sum(i)
            for j in i:
                count_scores += 1
        self.average_score = round(sum_scores / count_scores, 1)
    def __str__(self):
        self._average_score()
        res = f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_score}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_score < other.average_score

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

first_student = Student('Ruoy', 'Eman', 'male')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Git']

second_student = Student('Kristina', 'Grin', 'female')
second_student.courses_in_progress += ['Java', 'Python']
second_student.finished_courses += ['Git']

first_lecturer = Lecturer('Ivan', 'Petrov')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Denis', 'Ignatov')
second_lecturer.courses_attached += ['Java', 'Git']

first_reviewer = Reviewer('Egor', 'Panov')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Aleksandr', 'Sidorov')
second_reviewer.courses_attached += ['Java']

first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Java', 9)
second_reviewer.rate_hw(second_student, 'Java', 10)
first_reviewer.rate_hw(second_student, 'Python', 1)

first_student.rate_lecture(first_lecturer, 'Python', 9)
second_student.rate_lecture(first_lecturer, 'Python', 2)
second_student.rate_lecture(second_lecturer, 'Java', 10)

print(first_student, second_student, sep='\n \n', end='\n \n')
print(first_lecturer, second_lecturer, sep='\n \n', end='\n \n')
print(first_reviewer, second_reviewer, sep='\n \n', end='\n \n')

print(first_student.courses_in_progress)
print(second_student.courses_in_progress)
if 'Java' in second_student.courses_in_progress:
    print('fghbjkms')

print(first_student > second_student)
print(first_lecturer > second_lecturer)
def rating(class_list, course_name):
    gpa = 0
    course_list = []
    all_grades_course = []
    name_class = []
    if len(class_list) == 0:
        return 'Ошибка, список пуст'
    else:
        for ins in class_list:
            if isinstance(ins, Student):
                name_class = ['студентов']
                if course_name in ins.courses_in_progress:
                    course_list.append(course_name)
                    for course in ins.grades:
                        if course == course_name:
                            for grade in ins.grades[course]:
                                all_grades_course.append(grade)

            elif isinstance(ins, Lecturer):
                name_class = ['лекторов']
                if course_name in ins.courses_attached:
                    course_list.append(course_name)
                    for course in ins.grades:
                        if course == course_name:
                            for grade in ins.grades[course]:
                                all_grades_course.append(grade)
        if len(course_list) == 0:
            return f"Ошибка, на этом курсе нет {name_class[0]}!"
        elif len(all_grades_course) > 0:
            gpa = round((sum(all_grades_course) / len(all_grades_course)), 1)
            return f"Средняя оценка для всех {name_class[0]} по курсу {course_name}: {gpa}"
        else:
            return 'Ошибка, за этот курс оценки не выставлены'


print(rating(students_list, 'Python'))
print(rating(lectors_list, 'Git'))
print(rating(lectors_list, 'Java'))
