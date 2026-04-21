class Salary:
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary*12)+self.bonus
    
class Employee:

    def __init__(self,name,age,salary,bonus):
        self.name = name
        self.age = age
        self.sal_obj= Salary(salary,bonus)
    
    def total_salary(self):
        return self.sal_obj.annual_salary()


e = Employee("Manish",25,10000,2000)
print(e.total_salary())