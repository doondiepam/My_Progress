

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Employee(ABC):
    name: str = ""
    emp_id =  ""
    last_id = 0
    company = None

    last_id : int= 0

    def __post_init__(self):
        Employee.last_id += 1
        self.emp_id = 'Emp' + str(Employee.last_id)

    @abstractmethod
    def calculate_payment(self):
        pass

    def leave_company(self):
        if self.company == None:
            print(self.name, "is not in this compony")

        else:
            print(self.name, "is leaveing this company", self.company.name)
            self.company.fire(self)

@dataclass
class HourlyEmployee(Employee):
    hourly_rate: int = 0

    def calculate_payment(self):
        weekly_pay = self.hourly_rate * 40
        return weekly_pay

@dataclass
class SalariedEmployee(Employee):
    salary: int = 0

    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary

    def calculate_payment(self):
        weekly_pay = self.salary / 4
        return weekly_pay












