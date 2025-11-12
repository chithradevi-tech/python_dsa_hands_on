# object_reference_examples_with_section_output.py

# =============================================================
# Example 1: Class and Object References
# =============================================================

class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

"""
OUTPUT:

Cookie one is green
Cookie two is blue

Cookie one is now yellow
Cookie two is still blue
"""


# =============================================================
# Example 2: Integer Variable Reference (Immutable)
# =============================================================

num1 = 11
num2 = num1

print("\n#####################################")
print("\nBefore num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

"""
OUTPUT:

#####################################

Before num2 value is updated:
num1 = 11
num2 = 11

num1 points to: 136750401750024
num2 points to: 136750401750024

After num2 value is updated:
num1 = 11
num2 = 22

num1 points to: 136750401750024
num2 points to: 136750401750376
"""


# =============================================================
# Example 3: Dictionary Reference (Mutable)
# =============================================================

dict1 = {
    'value': 11
}

dict2 = dict1

print("\n#####################################")
print("\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

"""
OUTPUT:

#####################################

Before value is updated:
dict1 = {'value': 11}
dict2 = {'value': 11}

dict1 points to: 133029789964672
dict2 points to: 133029789964672

After value is updated:
dict1 = {'value': 22}
dict2 = {'value': 22}

dict1 points to: 133029789964672
dict2 points to: 133029789964672
"""
