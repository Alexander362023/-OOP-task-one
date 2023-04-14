from statistics import mean

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
       
        
class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached2 = []
        self.grades = {}
        self.ins = mean([9.9, 9.9, 10])
        self.progress = 'Python', 'Git'
        
    def rate_sp(self, lecturer, course, grade):
        '''выставляет оценкулекторам'''
        if isinstance(lecturer, Lecturer) and course in self.courses_attached2 and course in lecturer.courses_in_progress2:   
            if course in lecturer.gradess:
                lecturer.gradess[course] += [grade]
            else:
                lecturer.gradess[course] = [grade]
        else:
            return 'Ошибка'
         
    def __str__(self,):               
        return "Имя: {0} \nФамилия: {1} \nСредняя оценка за лекции: {2}".format(self.name, self.surname, self.ins)

    def fg(courses, stude):
        '''4 задание'''
        print('Курс: ' + courses)   
        for student in stude: 
            print(student)
    students_list = ['Денис', 'Юля']
    fg('Python', students_list)
  

class Reviewer(Mentor):
     
    def __init__(self, name, surname):
         super().__init__(name, surname)        
        
    def rate_hw(self, student, course, grade):
        '''Выставляет студентам оценки за домашнее задание''' 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return "Имя: {0} \nФамилия: {1}".format(self.name, self.surname) 


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.inss = mean([9.9, 9.9, 10])
        self.courses_in_progress2 = []
        self.gradess = {}
    def __str__(self):
        return "Имя: {0} \nФамилия: {1} \nСредняя оценка за лекции: {2}".format(self.name, self.surname, self.inss) 
def fg(courses, lecturer):
    '''4 задание'''
    print('Курс: ' + courses)   
    for student in lecturer: 
        print(student)
lecturer_list = ['Маша', 'Наташа']
fg('Python', lecturer_list)


R = Mentor('Павел', 'Маркович')
T = Mentor('Вячеслав', 'Маркович')

best_student = Student('Ruoy', 'Eman', 'M')
best_student.courses_in_progress += ['Python']

cool_student = Student('Ruoy', 'Eman', 'M')
cool_student.courses_attached2 += ['Python']
print(cool_student,  '\nКурсы в процессе изучения: %s, %s' % cool_student.progress, '\nЗавершенные курсы: Введение в программирование')


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
print(cool_reviewer)
B = Reviewer('Jim', 'Ted')


best_lecturer = Lecturer('Денис', 'Сергеевичь')  
best_lecturer.courses_in_progress2 += ['Python'] 
print(best_lecturer)
G = Lecturer('Вова', 'Иванович') 


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_student.rate_sp(best_lecturer, 'Python', 9)

print(best_student.grades)
print(best_lecturer.gradess)

class Comparison(): 
    def comparison(self):
        '''Сравнивает среднюю оценку Лекторов и студентов из словарей'''
        for lectur in best_lecturer.gradess.values():
            midl = mean(lectur)            
        for stude in cool_student.grades.values():
            midl2 = mean(stude)    
            
        if midl == midl2:
            print('Средняя оценка равна')  
        elif midl > midl2:
            print('Студенты молодцы')   
        elif midl < midl2:
            print('Лекторы красавцы')    

    def comparison(self):
        '''Сравнивает среднюю оценку лекторов и студентов из атрибутов inss и ins'''
        if best_lecturer.inss == cool_student.ins:
            print('Средняя оценка равна')  
        elif best_lecturer.inss > cool_student.ins:
            print('Студенты молодцы')   
        elif best_lecturer.inss < cool_student.ins:
            print('Лекторы красавцы')

I = Comparison()
I.comparison()
J = Comparison() 




