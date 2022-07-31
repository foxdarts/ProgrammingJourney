#file to calculate a employee salary given hours worked and payrate.

class Emp:
    def __init__(self, empname, employeeID):
        self.empname = empname
        self.empID = employeeID
        self.salary = None
    def calcSal(self):
        raise NotImplementedError("The subclass for this example needs to use the abstract method")

class Hourly(Emp):
    def __init__(self, empname, employeeID):
        Emp.__init__(self, empname, employeeID)
        self.hoursWorked = None
        self.payRate = None
    def calcSal(self):
        self.hoursWorked = input("How many hours does the person work each week?")
        self.payRate = input("Pay rate:")
        self.salary = int(self.hoursWorked)*float(self.payRate)*52

class Yearly(Emp):
    def __init__(self, empname, employeeID):
        Emp.__init__(self, empname, employeeID)
        self.years = None
        self.basePay = None
    def calcSal(self):
        self.years = input("How many years did the employee work at this company?")
        self.basePay = input("The base yearly pay:")
        self.salary = int(self.basePay)+(int(self.basePay)*.10*int(self.years))


if __name__ == '__main__':
    employees = list()
    employees.append(Hourly("Mary",1))
    employees.append(Yearly("John",2))
    for emp in employees:
        emp.calcSal()
        print(emp.empname,"has salary of",emp.salary,"each year.")
