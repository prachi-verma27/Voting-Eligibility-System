
# Project Title: Voting Eligibility System
# PS No.: 24

def check_eligibility(name, age, citizen):

    if age >= 18 and citizen == "y":
        print(f"{name} is eligible to vote.")
        return True

    else:
        print(f"{name} is not eligible to vote.")

        if age < 18:
            years_left = 18 - age
            print("Years left to become eligible:", years_left)

        if citizen == "n":
            print("Reason: Not an Indian citizen.")

        return False


# Main Program

eligible_count = 0
not_eligible_count = 0
total_voters = 0

print("================================")
print("     VOTING ELIGIBILITY SYSTEM")
print("================================")

while True:

    name = input("\nEnter your name: ")

    # Validate age using exception handling
    while True:
        try:
            age = int(input("Enter your age: "))

            if age < 0 or age > 120:
                print("Invalid age. Age must be between 0 and 120.")
                continue

            break

        except ValueError:
            print("Invalid input. Enter a whole number.")

    # Validate citizenship input
    while True:
        citizen = input("Indian citizen (y/n): ").lower()

        if citizen in ["y", "n"]:
            break

        print("Invalid input. Please enter y or n.")

    # Check eligibility
    result = check_eligibility(name, age, citizen)

    total_voters += 1

    if result:
        eligible_count += 1
    else:
        not_eligible_count += 1

    # Ask for another voter
    another = input("\nCheck another voter? (y/n): ").lower()

    if another != "y":
        break


# Display final results
print("\n================================")
print("          FINAL REPORT")
print("================================")

print("Voters checked:", total_voters)
print("Eligible:", eligible_count)
print("Not eligible:", not_eligible_count)

print("================================")
print("       Thank you!")
