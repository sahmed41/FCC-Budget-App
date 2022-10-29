import budget


food = budget.Category("Food")
clothing = budget.Category("Clothing")
food.deposit(50, "From salary")
food.deposit(50, "12345678998765432112345")
food.withdraw(40, "12345678998765432112346")
food.withdraw(23, "For food")
print(food.withdraw(20, "To eat"))
food.deposit(1000.678676, "Given money")


print(food.get_balance())

print(10 * "--")
print(clothing.categoryName)
print(food.transfer(500, clothing))
print(clothing.ledger)
print(clothing.get_balance())
print(food.get_balance())
food.withdraw(45.67, 'milk, cereal, eggs, bacon')
clothing.withdraw(20, "Shirt")
print(clothing.withdraw("220", "For some clothes"))
entertainment = budget.Category("Entertainment")
entertainment.deposit(1000)


# print(food.ledger)
# print(food)
#
print("----------------------------")
# print('****[47 chars]     900.00\nmilk, cereal, eggs, bac -45.67\nT[40 chars]4.33')
print(budget.create_spend_chart([food, clothing, entertainment]))
print(food)
print(clothing)

print(food.ledger)
print(clothing.ledger)