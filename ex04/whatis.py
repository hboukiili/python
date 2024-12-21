import sys  

def check_odd_or_even():
    
    try:

        if len(sys.argv) == 2:
        

            if not sys.argv[1].lstrip("-").isdigit():
                raise AssertionError("Argument is not an integer")
    
            num = int(sys.argv[1])

            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    check_odd_or_even()
