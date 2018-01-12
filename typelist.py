#input
input = ['magical unicorns',19,'hello',98.98,'world']




def typelist(input):
    sum = 0.00
    newStr = ""
    for count in range(0, len(input)):
        if isinstance(input[count], int):
            sum = input[count] + sum
            print sum
        if isinstance(input[count], float):
            sum = input[count] + sum
            print sum
        if isinstance(input[count], str):
            newStr = newStr + " " + input[count]
            print newStr
    print(sum, newStr)
        

typelist(input)