def calculate_bmi(weight, height_in_inches):
    """Calculate BMI given weight in pounds and height in inches."""
    bmi = (weight / (height_in_inches ** 2)) * 703
    return round(bmi, 1)

def get_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def boundary_test_get_bmi_category():
    """Automatically test the get_bmi_category function with boundary values."""
    print("\nRunning Boundary Tests for 'get_bmi_category'...")
    test_cases = [
        (18.4, "Underweight"),
        (18.5, "Normal weight"),
        (24.9, "Normal weight"),
        (25.0, "Overweight"),
        (29.9, "Overweight"),
        (30.0, "Obese")
    ]
    
    all_passed = True
    for bmi, expected in test_cases:
        result = get_bmi_category(bmi)
        if result == expected:
            print(f"Test Passed: BMI={bmi}, Expected={expected}, Got={result}")
        else:
            print(f"Test Failed: BMI={bmi}, Expected={expected}, Got={result}")
            all_passed = False
    
    if all_passed:
        print("All boundary tests passed!")
    else:
        print("Some boundary tests failed.")

def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input for height
    try:
        feet = int(input("Enter your height (feet): "))
        inches = int(input("Enter additional height (inches): "))
        weight = float(input("Enter your weight (pounds): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Convert height to inches
    total_height_in_inches = (feet * 12) + inches
    
    # Calculate BMI
    bmi = calculate_bmi(weight, total_height_in_inches)
    category = get_bmi_category(bmi)
    
    # Display results
    print(f"\nYour BMI is: {bmi}")
    print(f"You are classified as: {category}")

def test_functions():
    print("\nTesting Functions Individually:")
    print("1. Test 'calculate_bmi' function")
    print("2. Test 'get_bmi_category' function")
    print("3. Run boundary tests for 'get_bmi_category'")
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        try:
            weight = float(input("Enter weight in pounds: "))
            height_in_inches = float(input("Enter height in inches: "))
            bmi = calculate_bmi(weight, height_in_inches)
            print(f"Calculated BMI: {bmi}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif choice == "2":
        try:
            bmi = float(input("Enter BMI value: "))
            category = get_bmi_category(bmi)
            print(f"BMI Category: {category}")
        except ValueError:
            print("Invalid input. Please enter a numeric BMI value.")
    elif choice == "3":
        boundary_test_get_bmi_category()
    else:
        print("Invalid choice. Returning to main menu.")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Run the full BMI Calculator program")
    print("2. Test functions individually")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        main()
    elif choice == "2":
        test_functions()
    else:
        print("Invalid choice. Exiting program.")