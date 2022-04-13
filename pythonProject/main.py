stringFlag = False
integerFlag = False
beforeIntFlag = False
assignFlag = False

LETTER = []
DIGIT = []
ZERO = ['0']
WHITESPACE = ['\t', '\n', ' ']
MINUS = ['-']
OPERATOR = ['+', '*', '/']
OTHERS = []


def tokenize(input):
    ret = []
    if stringFlag:
        ret.append("STRING")
        ret.append(input)
    elif integerFlag:
        ret.append("INTEGER")
        ret.append(input)

    elif input in ["int", "INT"]:
        ret.append("VARTYPE")
        ret.append("INT")
    elif input in ["char", "CHAR"]:
        ret.append("VARTYPE")
        ret.append("CHAR")

    elif input in ["if", "IF"]:
        ret.append("KEYWORD")
        ret.append("IF")
    elif input in ["else", "ELSE"]:
        ret.append("KEYWORD")
        ret.append("ELSE")
    elif input in ["while", "WHILE"]:
        ret.append("KEYWORD")
        ret.append("WHILE")
    elif input in ["return", "RETURN"]:
        ret.append("KEYWORD")
        ret.append("RETURN")

    elif input == "<":
        ret.append("COMPARE")
        ret.append("<")
    elif input == ">":
        ret.append("COMPARE")
        ret.append(">")
    elif input == "<=":
        ret.append("COMPARE")
        ret.append("<=")
    elif input == ">=":
        ret.append("COMPARE")
        ret.append(">=")
    elif input == "!=":
        ret.append("COMPARE")
        ret.append("!=")
    elif input == "==":
        ret.append("COMPARE")
        ret.append("==")

    elif input == ";":
        ret.append("SEMICOLON")
    elif input == ",":
        ret.append("COMMA")
    elif input == "{":
        ret.append("LB")
    elif input == "}":
        ret.append("RB")
    elif input == "(":
        ret.append("LPAREN")
    elif input == ")":
        ret.append("RPAREN")

    else:
        ret.append("ID")
        ret.append(input)

    return ret

for i in range(65, 123):
    LETTER.append(chr(i))
    LETTER.append(chr(i + 32))
for i in range(49, 59):
    DIGIT.append(chr(i))

output = []

with open("test.c", "rt") as fin:
    while fin.read() != '':


with open("test.out", "wt") as fout:
    for element in output:
        if len(element) == 1:
            buffer = "<" + element[0] + ">\n"
        else:
            buffer = "<" + element[0] + ", " + element[1] + ">\n"
        fout.write(buffer)
