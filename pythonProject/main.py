stringFlag = False  # if this flag is true, letter will include in string
integerFlag = False  # if this flag is true, letter will include in integer
beforeIntFlag = False  # if present letter is - and this flag is true, it means
doneFlag = False  # if next character is last character of this token, it turns true
wordFlag = False  # if this token includes in id, keyword, type, it turns true

LETTER = []
DIGIT = []
ZERO = ['0']
WHITESPACE = ['\t', '\n', ' ']
MINUS = ['-']
OPERATOR = ['+', '*', '/']
OTHERS = ['(', ')', '{', '}', ',', ';']


def tokenize(input):
    ret = []
    if stringFlag:  # string token
        ret.append("STRING")
        ret.append(input)
    elif integerFlag:  # integer token
        ret.append("INTEGER")
        ret.append(input)

    # variable type token
    elif input in ["int", "INT"]:
        ret.append("VARTYPE")
        ret.append("INT")
    elif input in ["char", "CHAR"]:
        ret.append("VARTYPE")
        ret.append("CHAR")

    # keyword token
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

    # operator token
    elif input in OPERATOR + MINUS:
        ret.append("OP")
        ret.append(input)
    elif input == '=':
        ret.append("ASSIGN")
        ret.append(input)

    # compare operation token
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

    # other character token
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

    # identifier token
    else:
        ret.append("ID")
        ret.append(input)

    output.append(ret)


for i in range(65, 123):
    LETTER.append(chr(i))
    LETTER.append(chr(i + 32))
for i in range(49, 58):
    DIGIT.append(chr(i))

output = []
string = ""

with open("test.c", "rt") as fin:
    buff1 = fin.read(1)
    while True:
        if buff1 == '':
            break
        buff2 = fin.read(1)
        if stringFlag:
            string += buff1
        elif doneFlag:
            string += buff1
            tokenize(string)
            doneFlag = False
        elif buff1 in LETTER:
            if wordFlag:
                string += buff1
            else:
                string = buff1
                wordFlag = True
            if buff2 not in LETTER + ZERO + DIGIT:
                tokenize(string)
                string = ""
                wordFlag = False
        elif buff1 in ZERO + DIGIT:
            if integerFlag:
                string += buff1
                if buff2 not in ZERO + DIGIT:
                    tokenize(string)
                    string = ""
                    integerFlag = False
                    beforeIntFlag = True
            elif wordFlag:
                string += buff1
                if buff2 not in ZERO + DIGIT + LETTER:
                    tokenize(string)
                    string = ""
                    wordFlag = False
            elif buff1 in ZERO:
                integerFlag = True
                tokenize(buff1)
                beforeIntFlag = True
                integerFlag = False
            else:
                string = buff1
                integerFlag = True
                if buff2 not in ZERO + DIGIT:
                    tokenize(string)
                    integerFlag = False
        elif buff1 in OPERATOR:
            tokenize(buff1)
        elif buff1 in MINUS:
            if beforeIntFlag:
                tokenize(buff1)
                beforeIntFlag = False
            else:
                string = buff1
                integerFlag = True
        elif buff1 in OTHERS:
            tokenize(buff1)
        elif buff1 in ['<', '>', '!', '=']:
            string = buff1
            if buff2 == '=':
                doneFlag = True
            else:
                tokenize(string)
        elif buff1 == '"':
            if stringFlag:
                string += buff1
                tokenize(string)
                stringFlag = False
            else:
                string = buff1
                stringFlag = True
        buff1 = buff2


with open("test.out", "wt") as fout:
    for element in output:
        if len(element) == 1:
            buffer = "<" + element[0] + ">\n"
        else:
            buffer = "<" + element[0] + ", " + element[1] + ">\n"
        fout.write(buffer)
