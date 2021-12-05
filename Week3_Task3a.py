# https://lucid.app/lucidchart/e98a1751-99bc-4d66-812c-a2baad5cd726/edit?invitationId=inv_be24c85e-ea8f-4e5f-8940-237c62e6d328

# Select coffee type
coffee = input("What coffee would you like to order?")

# Select cup size
cup_size = input("What coffee size would you like to order?")

# Want sugar?
sugar = input("Would you like some sugar?")
if sugar == "yes":
    # How much sugar?
    sugar_amount = input("How much sugar do you want?")

# Pay cashier
print("Please go to the cashier")