# This function takes two input values (as strings representing "True" or "False") from the user
# and evaluates several logical operations between the converted boolean values.
def true_false(t, f):
    t = input("Enter True or False: ") == "True"  # Convert user input to a boolean
    f = input("Enter True or False: ") == "True"  # Convert user input to a boolean
    and_t_f = t and f  # Logical AND operation
    or_t_f = t or f  # Logical OR operation
    not_t = not t  # Logical NOT operation on the first value
    not_f = not f  # Logical NOT operation on the second value
    equal = t == f  # Check if both values are equal
    not_equal = t != f  # Check if both values are not equal
    return and_t_f, or_t_f, not_t, not_f, equal, not_equal  # Return the results of all operations


# Call the function and store the results of the logical operations
result_true_false = true_false(True, False)

# Print the results of the logical operations to the console
print(f"AND result: {result_true_false[0]}\n"
      f"OR result: {result_true_false[1]}\n"
      f"NOT result: {result_true_false[2]}\n"
      f"NOT result: {result_true_false[3]}\n"
      f"EQUAL result: {result_true_false[4]}\n"
      f"NOT EQUAL result: {result_true_false[5]}\n")
