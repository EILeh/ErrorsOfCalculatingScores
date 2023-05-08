"""
Errors of calculating scores

Program ask the name of the file that contains the information of the scores.
Program tries to open the file and read the file and if it can't do it,
an error will be printed. Otherwise goes through the file and if the file
contains a line that doesn't consist of two strings separated by (a) space
character(s), the program prints an error message. The file will be processed
line by line from the beginning towards the end. The program will print the
error message related to the first error it finds. The execution of the program
will end immediately after printing the first error message. This means, that if
there are multiple errors in the file, only the first one will be reported.
The program helps you add up the scores that various contestants have obtained
in a game. The scores are stored in a text file that the program uses as input.
The scores can be entered to the file in practically any order, and the program
does not even take a stand on how many scores each contestant gets. The only
operations the program performs are the calculation of the sum of scores of the
contestants with the same name and printing the scores of all the contestants in
alphabetical order, according to the player's name.

Writer of the program: EILeh

"""


def main():

    filename = input("Enter the name of the score file: ")
    score_book = {}

    try:
        score_file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return score_book

    # Goes through every line in the file.
    for line in score_file:
        # Removes all the extra spaces.
        line = line.strip()
        split_line = line.split(" ")
        split_line_length = len(split_line)

        # If there is a line that haven't been separated by space or line
        # contains only one information, an error will be printed.
        if split_line_length < 2:
            print("There was an erroneous line in the file:")
            print(line, end="")
            return

        # In every line the information at index 1 should be possible to
        # represent as an integer. If it isn't possible, an error will be
        # printed.
        for number_string in split_line[1]:
            try:
                number = int(number_string)

            except ValueError:
                print("There was an erroneous score in the file:")
                print(f"{split_line[1]}")
                return

        name = split_line[0]
        score = int(split_line[1])

        # If the name isn't found in dictionary score_book, then this is the
        # first time it comes up and a new key-value pair is added to the
        # score_book.
        if name not in score_book:
            score_book[name] = score

        # If the name is found in the dictionary socre_book, the current
        # score is updated by adding the new score to the old score.
        else:
            score_book[name] += score

    print("Contestant score:")

    score_file.close()

    # The information from the dictionary score_book is printed.
    for name, score in sorted(score_book.items()):
        print(f"{name} {score}")

if __name__ == "__main__":
    main()