import re

problem = ["32 - 698", "3001 - 2", "45 + 43", "123 + 49"]

lineas = ["","","","",""]

if len(problem)>5:
    print('Error: Too many problems.') # Break, return Error 

for operation in problem:

    opera = re.findall('[+-]+', operation)
    numbers = re.findall('[0-9]+', operation)

    if len(opera) == 1:

        if len(numbers)<3:
            if len(numbers[0])<5 and len(numbers[1])<5:

                if opera[0] == '+':

                    suma = int(numbers[0]) + int(numbers[1])
                    suma = str(suma)

                else:
                    suma = int(numbers[0]) - int(numbers[1])
                    suma = str(suma)

                up = len(numbers[0])
                down = len(numbers[1])

                maxlen = max(up,down)

                lineas[0] =  "  " + (maxlen-up)*" "+ numbers[0] + 4*" " + lineas[0]
                lineas[1] = opera[0] +" " + (maxlen-down)*" "+ numbers[1]+ 4*" " + lineas[1]
                lineas[2] =  "--" + (maxlen)*"-" + 4*" " + lineas[2]
                lineas[3] = (5-len(suma))*" "+suma +4*" "+lineas[3]






            else:
                print('Error: Numbers cannot be more than four digits.')
        else:
            print('Error: Numbers must only contain digits.')

    else:
        print('''Error: Operator must be '+' or '-'.''') #Break return error
    

    
for i in range(4):
    print( lineas[i] )  
