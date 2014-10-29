from sys import *
lexeme = ['']*100
f = None
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF =-1
MULT_OP = 23
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
nextToken = 1
nextChar = ""
##############################################################################
def main():
    global f,nextToken,charClass,lexLen,nextChar
    try:
        try:
            f = open("lex.txt", "r")                  
        except Exception, e:
            print "ERROR: cannot open lex.txt"
        finally:
            getChar()
            Z = 0
        while nextToken != EOF:      
            lex() 
            Z+=1
        f.close()
    except Exception, e:
        print e
############################################################################
# addChar - a function to add nextChar to lexeme

def addChar():
    global f,nextToken,charClass,lexLen,lexeme,nextChar
    if lexLen <= 98:       
        lexeme[lexLen + 1] = nextChar
        lexeme[lexLen] = 0
    else:
        print "Error:lexeme is too long."
###############################################################################
# getChar - a function to get the next character of input and determine its character class    

def getChar():
    global f,nextToken,charClass,lexLen,nextChar
    try:
        rd = f.read(1)
        if rd != "-1":
            nextChar = rd
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN            
        
	else:
            charClass = EOF
            nextChar = '\0'        
    except Exception, e:
        print e
#################################################################################
# getNonBlank - a function to call getChar until it returns a non-whitespace character    

def getNonBlank():
    global f,nextToken,charClass,lexLen,nextChar
    while nextChar.isspace():
        getChar()
#################################################################################
# lookup - a function to lookup operators and parentheses and return the token

def lookup(ch):      
    global f,nextToken,charClass,lexLen,lexeme,nextChar
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
#####################################################################    	   
#lex - a simple lexical analyzer for arithmetic expressions

def lex():
    global f,nextToken,charClass,lexLen,lexeme,nextChar
    lexLen = 0
    lexeme = ['']*100
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()        
        while charClass == LETTER:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
	   
    if nextToken!=-1:
    	print "Next token is: " + str(nextToken) + " Next lexeme is " + str(lexeme[1])
    else:
    	print "Next token is: " + str(nextToken) + " Next lexeme is EOF"

main()
