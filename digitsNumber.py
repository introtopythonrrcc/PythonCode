"""

Caden Picard
CSC119-471
Project: digitsNumber
Design: Write program that computes the first and last digit of a number. 
Date: 6/20/2017
Source: General Knowledge
Sources
"""
def main():
    # variables 
    numberInput = input("Please enter an integer:")
    numberTostring = str(numberInput)
    
    # process formulas
    firstnumber = numberTostring[0]
    lastnumber = int(numberInput) % 10
    
    # output
    print(firstnumber)
    print(lastnumber)
    
main()
