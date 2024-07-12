student_id = input("Student Id: ")

# Convert the student ID string to a list of integers
digits = [int(digit) for digit in student_id]

# Iterate through the digits of the student ID
for i in range(1, len(digits)):
    current_digit = digits[i]
    previous_digit = digits[i - 1]

    # Calculate and print the sum, subtraction, and multiplication
    print(f"Current Digit: {current_digit}, Previous Digit: {previous_digit}")
    print(f"Sum: {current_digit + previous_digit}")
    print(f"Subtraction: {current_digit - previous_digit}")
    print(f"Multiplication: {current_digit * previous_digit}")
    print("---")

