import sys
import string

def analyze_string(input_string):
    
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    digit_count = sum(1 for char in input_string if char.isdigit())
    punctuation_count = sum(1 for char in input_string if char in string.punctuation)
    space_count = sum(1 for char in input_string if char.isspace())

    print(f"The text contains {len(input_string)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():

    try:
        if len(sys.argv) > 2:
            raise AssertionError("More than one argument is provided")
        elif len(sys.argv) == 2:
            input_string = sys.argv[1]
        else:
            input_string = input("What is the text to count?\n")

        analyze_string(input_string)

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
