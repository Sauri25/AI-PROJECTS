# Pahila function banako jasle age arguement linxa ani check garxa kun group ko vanera

def age_group(age):
    if age == 0 or age < 0:
        print("Please enter valid age")
    if age < 10:
        print("You are a child")
    elif age < 18:
        print("You are a teenager")
    elif age <= 59:
        print("You are an adult")
    elif age > 59:
        print("You are a senior citizen")


print("\n\n\t\t\t\tAGE GROUP CHECKER\n")
# naam input liyo
name = input("Please enter your name: ")
print(f"Hey, {name} welcome to our age group checker program.")

# euta while loop vitra xiryo jaha try and except case haru xa
while True:
    try:
        # age input liera function lai age pass garyo ra edi age valid xa vaney output dinxa
        age = int(input("Please enter your age: "))
        age_group(age)

    # if age ko thau ma kunai character or aru data type diyo vane error consider garieko xa
    except ValueError:
        print("Please enter valid age")

    # feri run garne vanera sodhxa if yes then run hunxa kinaki loop ma condition true nai hunxa tara no vanyo vane loop break hunxa
    b = input("Do you want to try again?(answer in yes or no)")
    if b.lower() != "yes":
        break
print("\nThankyou")
