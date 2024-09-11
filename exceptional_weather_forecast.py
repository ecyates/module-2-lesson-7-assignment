# 1. Exceptional Weather Forecast
# Objective: The aim of this assignment is to enhance your understanding of exception handling 
# by creating a weather forecast application that gracefully handles unexpected user input 
# and provides user-friendly error messages.

# Task 1: Start 
# Begin by asking the user to enter the temperature in Fahrenheit.

# Task 2: Temperature Conversion 
# Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?

# Task 3: User Experience 
# Implement an else block that prints the converted temperature in a user-friendly format. 

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally 
# Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

# Function that converts fahrenheit to celsius
def temp_converter(fahrenheit):
    celsius = (fahrenheit-32)*5/9
    return celsius

# Get the user input for the temperature in Fahrenheit and convert to integer
try:
    user_temp = float(input("What's the temperature in Fahrenheit?\n"))
    print(f"{user_temp} degrees in Fahrenheit is {temp_converter(user_temp):.2f} degrees in Celsius.")
# If the user doesn't input a number, catch the error
except ValueError:
    print("Oops! This requires a number. Try again...")
# Catch any other errors that occur from the conversion
except Exception as e:
    print(f"An unknown exception {e} has occurred.")
# Finally, thank the user for using the app
finally:
    print("Thank you for using the weather forecast app! Have a great day, regardless of the weather.")