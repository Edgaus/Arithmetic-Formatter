import re

def arithmetic_arranger(problems, answer=False):

  lineas = ["","","",""]

  if len(problems) > 5:
    return ('Error: Too many problems.')  # Break, return Error

  for problem in problems:
    opera = re.findall('[+-]+', problem)
    numbers = re.findall('[0-9]+', problem)
    

    if opera ==['+'] or opera == ['-']:

      if len(numbers) < 3:
        if len(numbers[0]) < 5 and len(numbers[1]) < 5:

            if opera[0] == '+':
                suma = int(numbers[0]) + int(numbers[1])
                suma = str(suma)

            else:
                suma = int(numbers[0]) - int(numbers[1])
                suma = str(suma)

            up = len(numbers[0])
            down = len(numbers[1])

            maxlen = max(up, down)

            lineas[0] = lineas[0] + "  " + (maxlen -up) * " " + numbers[0] + 4 * " " 
            lineas[1] = lineas[1] + opera[0] + " " + (maxlen - down) * " " + numbers[1] + 4 * " " 
            lineas[2] = lineas[2] + "--" + (maxlen) * "-" + 4 * " " 
            lineas[3] = lineas[3] + (2+maxlen - len(suma)) * " " + suma +  4* " " 

        else:
          return 'Error: Numbers cannot be more than four digits.'
      else:
        return ('Error: Numbers must only contain digits.')

    else:
      return ('''Error: Operator must be '+' or '-'.''')  #Break return error

  arranged_problems = ""
  for i in range(3):
    if i<2:
        arranged_problems = arranged_problems + str(lineas[i][:-4]) +'\n'
    else:
        arranged_problems=arranged_problems + str(lineas[2][:-4])

  if answer:
      arranged_problems =   arranged_problems+'\n' + str(lineas[3][:-4])
  return arranged_problems

