MIN_AGE = 8
MAX_AGE = 99

customer_age_OK = False

age = int(input("what is the age of the customer"))

# if age >= MIN_AGE and age <= MAX_AGE:
if MIN_AGE <= age <= MAX_AGE:
    customer_age_OK = True

if customer_age_OK:
    print("This customer is able to use this product")

# .... lots of other stuff here

if customer_age_OK:
    print("write the customer to a mailing list")
