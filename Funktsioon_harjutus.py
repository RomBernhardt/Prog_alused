"""Function examples."""


# func()
def func():
    print("I´m inside the function")

# my_name_is(name)
def my_name_is(name):
    print(f"My name is {name}")

my_name_is("Rom")

# sum_six(num)`
def sum_six(num):
    return 6 + num

print(sum_six(1))
print(sum_six(6))

# sum_numbers()
def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 5))
print(sum_numbers(0, 25))

# usd_to_eur()
def usd_to_eur(usd):
    return usd * 0.8

print(usd_to_eur(100))