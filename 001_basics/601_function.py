def get_total(price, qty=1, tax=0.1, discount=0):
    subtotal = price * qty * (1 - discount)
    print(subtotal * (1 + tax))


get_total(100)

# named parameter
# pythonでは何もしなくてもnamedになる。
get_total(100, qty=2)
get_total(price=100, qty=2)
get_total(tax=0.2, price=100, qty=2)

print("**************************")

work_hours = [("Kuroro", 100), ("Kirin", 800), ("Kohei", 400)]


def check_employee(employees):
    current_max = 0
    employee_of_month = ""

    for employee, hours in employees:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    # tupleを返す
    return (employee_of_month, current_max)


# tuple unpacking
name, hours = check_employee(work_hours)
print(name, hours)