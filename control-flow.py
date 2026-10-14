# === CONTROL FLOW AND ITERABLES
command = "run"

match command:
    case "run":
        print("The robot started to run")
    case "speak" | "say_hi":
        print("The robot said hi")
    case code if command.isdigit():
        print(f"The robot executed code: {code}")
    case _:
        print("Invalid command")

animals = ["dog", "cat", "horse"]

for animal in animals:
    print(f"{animal} is a mammal")
    print("{} is a mammal".format(animal))

for i in range(4):
    print(i) # => 0, 1, 2, 3

for i, value in enumerate(animals):
    print(i, value) # => 0 dog, 1 cat, 2 horse