# In class, we did this exercise that adds a bunch of items to mom's shopping cart, then we counted the occurrence of each grocery item in the shopping cart.
# Find the TODO section of this file, and find instructions there.

import random


def count_occurrence(item, my_list):
    total = 0
    for i in my_list:
        if i == item:
            total += 1  # total = total + 1
    return total


# mom bought a lot of grocery items
grocery_item = ["apple", "banana", "broccoli", "milk", "bread"]
shopping_cart = []

for i in range(100):
    # throws random items from grocery_item into shopping_cart
    shopping_cart.append(random.choice(grocery_item))

print("Mom bought:")
print(str(count_occurrence("apple", shopping_cart)) + " apples")
print(str(count_occurrence("banana", shopping_cart)) + " bananas")
print(str(count_occurrence("broccoli", shopping_cart)) + " broccolis")
print(str(count_occurrence("milk", shopping_cart)) + " gallons of milk")
print(str(count_occurrence("bread", shopping_cart)) + " loaves of bread")

# TODO: write a for loop that removes all "banana"s from shopping_cart

shopping_cart_copy = shopping_cart.copy()
for i in shopping_cart_copy:
    if (i=="banana"):
        shopping_cart.remove("banana")

print("After removing all bananas, mom bought:")
print(str(count_occurrence("apple", shopping_cart)) + " apples")
print(str(count_occurrence("banana", shopping_cart)) + " bananas")
print(str(count_occurrence("broccoli", shopping_cart)) + " broccolis")
print(str(count_occurrence("milk", shopping_cart)) + " gallons of milk")
print(str(count_occurrence("bread", shopping_cart)) + " loaves of bread")






