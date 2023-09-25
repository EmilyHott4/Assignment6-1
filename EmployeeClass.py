class EmployeeClass:
    def __init__(self, name,IDnumber,department,jobTitle, monthlySalary):
        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department
        self.__jobTitle = jobTitle
        self.__monthlySalary = monthlySalary
        
    def getName(self):
        return self.__name

    def getIDnumber(self):
        return self.__IDnumber
    
    def getDepartment(self):
        return self.__department

    def getjobTitle(self):
        return self.__jobTitle

    def getmonthlySalary(self):
        return self.__monthlySalary
    
class ShiftSupervisor(EmployeeClass):
    def __init__(self, name, IDnumber, annual_salary, annual_bonus):
        super().__init__(name, IDnumber)
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus
    
    def get_annual_salary(self):
        return self.annual_salary
    
    def get_annual_bonus(self):
        return self.annual_bonus
    
    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary
    
    def set_annual_bonus(self, annual_bonus):
        self.annual_bonus = annual_bonus

class ProductionWorker(EmployeeClass):
    def __init__(self, name, IDnumber, shift, hourly_pay):
        super().__init__(name, IDnumber)
        self.shift = shift
        self.hourly_pay = hourly_pay
    
    def get_shift(self):
        return self.shift
    
    def get_hourly_pay(self):
        return self.hourly_pay
    
    def set_shift(self, shift):
        self.shift = shift
    
    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay

def main():
    print("Please Enter Worker's Information:")
    
    name = input("Name: ")
    
    IDnumber = input("Employee ID Number: ")
    
    shift = int(input("Shift 1(Morning) or 2(Night): "))
    
    hourly_pay = float(input("Hourly Pay: "))

    department = float(input(" Department: "))

    
    worker = ProductionWorker(name, IDnumber, shift, hourly_pay)

    print("\nEnter Supervisor's Information:")
    
    name = input("Name: ")
    
    IDnumber = input("Employee ID Number: ")
    
    annual_salary = float(input("Annual Salary: "))
    
    annual_bonus = float(input("Annual Bonus: "))

    supervisor = ShiftSupervisor(name, IDnumber, annual_salary, annual_bonus)

    print("\n Worker Information:")
    print(f"Name: {worker.get_name()}") 
    print(f"Employee ID Number: {worker.get_IDnumber()}")   
    print(f"Shift: {worker.get_shift()}") 
    print(f"Hourly Pay: {worker.get_hourly_pay()}")

    
    print("\n Supervisor Information:")  
    print(f"Name: {supervisor.get_name()}")  
    print(f"EmployeeID Number: {supervisor.get_IDnumber()}") 
    print(f"Annual Salary: {supervisor.get_annual_salary()}")
    print(f"Annual Bonus: {supervisor.get_annual_bonus()}")


if __name__ == "__main__":
    main() 