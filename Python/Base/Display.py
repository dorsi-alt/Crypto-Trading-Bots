darker_blue_background = '\x1b[48;5;52m\x1b[K\x1b[0m'
darker_green_background = '\033[48;5;22m'
dark_red_background = '\033[48;5;52m'

reset_color = '\033[0m'

# Print the text with the specific line in darker blue background
def printBlueText(string):
    print("", end="")
    print(darker_blue_background + string + reset_color, end="")
    print("")


def printGreenText(string):
    print("", end="")
    print(darker_green_background + string + reset_color, end="")
    print("")

def printRedText(string):
        print("", end="")
        print(dark_red_background + string + reset_color, end="")
        print("")