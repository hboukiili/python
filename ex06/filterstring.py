import sys
from ft_filter import ft_filter

def main():
    """
    Main program to process input arguments and output filtered words.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("The arguments are bad")

        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("The second argument must be an integer")

        S = sys.argv[1]
        if not isinstance(S, str):
            raise AssertionError("The first argument must be a string")

        words = S.split()

        filtered_words = ft_filter(lambda word: len(word) > N, words)

        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
