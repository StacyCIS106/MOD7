user_prompt = input("Do you want to do this program? (yes/no): ")
num_employee = 0
total_gross_pay1 = 0
while user_prompt == 'yes' or user_prompt == 'YES' or user_prompt == 'Yes':
    last_name = input("Enter your last name: ")
    hours = int(input("Enter your hours worked: "))
    pay_rate = int(input("Enter your pay rate: "))
    gross_pay = hours * pay_rate
    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = 40 * pay_rate + overtime_hours * pay_rate * 1.5
    print((last_name), gross_pay)
    num_employee += 1
    print("Number of employees entered: ", num_employee)
    total_gross_pay1 = gross_pay + total_gross_pay1
    print("sum gross pay of all employees: ", total_gross_pay1)
    print("Count of employees: ", num_employee)
    print("Average gross pay of all employees: ", total_gross_pay1 / num_employee)
    user_prompt = input("Do you want to do this program? (yes/no): ")
