from company import Company

from employee import HourlyEmployee
from employee import SalariedEmployee
from domain import Domain

company_name = input("Enter Company Name: ")
domain_name = input("Enter Domain Name: ")

if domain_name == "TECHNOLOGY":
    domain = Domain.TECHNOLOGY
elif domain_name == "HEALTHCARE":
    domain = Domain.HEALTHCARE
elif domain_name == "RETAIL":
    domain = Domain.RETAIL
else:
    print("Invalid domain")
    exit()

company = Company(company_name, domain, [])

n = int(input("Enter Number of Employees: "))

for i in range(n):
    print("\nemployees",i+1)

    name = input("Enter Employee Name: ")
    company_type = input("type (HourlyEmployee, SalariedEmployee): ")

    if company_type == "HourlyEmployee":
        hourly_rate = int(input("Enter Hourly hourly_rate: "))
        emp = HourlyEmployee(name, hourly_rate = hourly_rate)

    else:
        salary = int(input("Enter Salary: "))
        emp = SalariedEmployee(name, salary = salary)

    company.hire(emp)

print(company)



