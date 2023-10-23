# Question 1
usr_input = input("Enter a value: ")

try:
    usr_input = float(usr_input)
    # usr_input = int(usr_input)

except ValueError:
    print("ValueError occurred")


# Question 2
def dummy_func(data):
    try:
        if not isinstance(data, list):
        # if not isinstance(data, dict):
            raise TypeError
    except TypeError:
        print("TypeError occurred")