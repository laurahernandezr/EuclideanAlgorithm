

#Formula for the Euclidean Algorithm
#a = d * q +r
#0   1   2  3
def get_a_and_r(n1, n2):
    #local equation that saves the numbers
    equation = [n1, n2, 0, 0]
    i = 1
    #puts the maximum in a and the min in d
    if n2 > n1:
        equation[0] = n2
        equation[1] = n1
    #finds the quotient q by trying every number
    while equation[1] * i <= equation[0]:
        equation[2] = i
        i = i + 1
    #updates the formula and returns it
    equation[3] = equation[0] - (equation[1] * equation[2])
    equation[0] = equation[1]
    equation[1] = equation[3]
    return equation

def main():
    n1 = int(input("Please enter the first number you want to calculate: "))
    n2 = int(input("Please enter the second number you want to calculate: "))
    process_equation = [n1, n2, 10, 10]
    while process_equation[3] > 0:
        process_equation = get_a_and_r(process_equation[0], process_equation[1])
        #goes until the remainder is 0 but prints the remainder before that as the gcd
        if process_equation[3] != 0:
            final_equation = process_equation
    print("The greatest common denominator for "+ str(n1) + " and " + str(n2) + " is " + str(final_equation[3]))

main()
