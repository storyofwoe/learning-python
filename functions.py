# https://www.learnpython.org/en/Functions

def list_benefits():
    return ["More organised code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return f"{benefit} is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# https://pynative.com/python-functions-exercise-with-solutions/

def func1(*args):
    print(*args)

func1(100, 2000, 3000)
func1(1,2,3,4,5,6,7,8)

# === Exercise 3
def calculation(a, b):
    return a + b, a - b

print(calculation(40, 10))

# === Exercise 4
def show_employee(name, salary = 9000):
    return f"Name: {name}, salary: {salary}"

print(show_employee("Ben", 12000))
print(show_employee("Jessa"))