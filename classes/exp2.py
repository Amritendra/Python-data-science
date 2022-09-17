class Employee:
    #constructer 
    def __init__(self,name,desig,dept,salary,skills=None):
        self.name=name
        self.designation=desig
        self.department=dept
        self.salary=salary
        self.skills=skills
    
    def do_task(self,task):
        print(f'Employee {self.name} is doing {task}')
    
    def info(self):
        print('Employee details')
        print(f'Name:{self.name}')
        print(f'Department:{self.department}')
        print(f'designation:{self.designation}')
        print(f'salary:{self.salary}')
        print(f'skills:{", ".join(self.skills)}')

        


    def add_skills(self,skillname):
        if self.skills is None:
            self.skills=[skillname]
        else:
            self.skills.append(skillname)

e1=Employee('amrit','assistant 2','sales',40000,['talking'])
e2=Employee('ashmit','staff officer','finance',700000,['management','leadership'])
e3=Employee('pratham','manager',"managing office",1200000,['team managemt','trustworthy'])
e1.info()
e2.info()
e3.info()
e1.do_task("making some sales")
e2.do_task("firing employees")
e3.do_task('managing office works')
e1.add_skills('helping')
e1.add_skills('confidence')
e1.info()


