
from dataclasses import dataclass
from employee import HourlyEmployee
from employee import SalariedEmployee
from domain import Domain

@dataclass
class Company:
    name = str
    domain = Domain
    employer = list

    def __init__(self, name, domain, employer):
        self.name = name
        self.domain = domain
        self.employer = employer

    def hire(self, emp):
        if emp in self.employer:
            print(emp.name,"is there in company")
            return
        if emp.company != None:
            print(emp.name, " works in", emp.company.name)
            return
        self.employer.append(emp)
        emp.company = self
        print(emp.name, "was hired by", self.name)

    def fire(self, emp):
        if emp in self.employer:
            self.employer.remove(emp)
            emp.company = None
            print(emp.name, "is fired" )
        else:
            print(emp.name, "is not there")

    def raise_pay(self, emp, amount):
        if emp not in self.employer:
            print(emp.name, "is not there")
            return
        if isinstance(emp, HourlyEmployee):
            emp.hourly_rate = emp.hourly_rate + amount
        elif isinstance(emp, SalariedEmployee):
            emp.salary = emp.salary + amount



        print("pay is high for" , emp.name)
    def __repr__(self):
        return "Company(" + self.name + ", " + self.domain.name + ", employer: " + str(len(self.employer)) + ")"




