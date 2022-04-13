stringFlag = False
integerFlag = False
beforeintFlag = False

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
        ret.append("INT")
    elif input in ["int", "INT"]:
        ret.append("VARTYPE")
        ret.append("INT")
    elif input in ["int", "INT"]:
        ret.append("VARTYPE")
        ret.append("INT")
    elif input in ["int", "INT"]:
        ret.append("VARTYPE")
        ret.append("INT")
    elif input in ["int", "INT"]:
        ret.append("VARTYPE")
        ret.append("INT")