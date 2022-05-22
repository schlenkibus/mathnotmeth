import getopt
import sys
import random

numberOfProblems = 1
numberOfExpressions = 2
allowedOperators = ["+", "-", "*", "/"]
allowedDigitCount = 2
seed = random.randint(0, 18927891729)


#parse arguments to script

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:e:o:d:s:", ["number=", "expressions=", "operators=", "digits=", "seed="])
except getopt.GetoptError:
    print("create_math_problems.py -n <numberOfProblems> -e <numberOfExpressions> -o <allowedOperators> -d <allowedDigitCount> -s <seed>")
    sys.exit(2)

for opt, arg in opts:
    if opt == "-n":
        numberOfProblems = int(arg)
    elif opt == "-e":
        numberOfExpressions = int(arg)
    elif opt == "-o":
        allowedOperators = arg.split(",")
    elif opt == "-d":
        allowedDigitCount = int(arg)
    elif opt == "-s":
        seed = int(arg)


random.seed(seed)

print(allowedOperators)

def createDigit(allowedDigitCount):
    range_start = 1
    range_end = (10**allowedDigitCount)-1
    return str(random.randint(range_start, range_end))

def createOperator(allowedOperators):
    return allowedOperators[random.randint(0, len(allowedOperators) - 1)]

def createExpressionPart(allowedOperators, allowedDigitCount):
    return createDigit(allowedDigitCount) + createOperator(allowedOperators) + createDigit(allowedDigitCount)

def createRandomExpression(allowedOperators, allowedDigitCount):
    if random.random() < 0.5:
        return createExpressionPart(allowedOperators, allowedDigitCount)
    else:
        return createDigit(allowedDigitCount)

def createExpression(numberOfExpressions, allowedOperators, allowedDigitCount):
    expression = ""
    for i in range(numberOfExpressions):
        if len(expression) == 0:
            expression += createRandomExpression(allowedOperators, allowedDigitCount)
        else:
            expression += createOperator(allowedOperators) + '(' + createRandomExpression(allowedOperators, allowedDigitCount) + ')'
    return expression

#create problems
for i in range(numberOfProblems):
    expr = createExpression(numberOfExpressions, allowedOperators, allowedDigitCount)
    result = ""
    try:
        result = str(eval(expr))
    except Exception as e:
        result = str(e)
    print("Problem " + str(i+1) + ": " + expr + " = " + result)