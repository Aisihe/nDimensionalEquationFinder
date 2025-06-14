import numpy as np
import matplotlib.pyplot as plt
import math

class FindPolynomial:
  def find_equation_Human(input_vals, output):
    '''
    input_vals = inputs (nx2; nx4):: output = output (always nx1 array)
    '''
    dimensionality = input_vals.shape[1] + 1
    degree = int(math.pow(input_vals.shape[0],1/(dimensionality-1)))
    general = degree**(dimensionality-1)
    dimSmall = dimensionality-1
    
    main = np.ones([general, general])

    for i in range(general): #equation number
          for j in range(general): #equation element
              counter = degree**np.arange(dimSmall)
              middle = (j//counter)%degree
              main[i, j] = np.prod(input_vals[i, :]**(degree-middle-1))
    
    sup = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]          
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    var = np.empty([general, 1], dtype='U100')
    for j in range(general): #equation element
      temp = ""
      for coNum in range(dimSmall):
          counter = degree**coNum
          middle = (j//counter)%degree
          temp += letters[coNum] + sup[degree-middle-1]
          var[j, 0] = temp

    answers = np.linalg.inv(main) @ output
    
    fin = ""

    for i in range(general):
      if round(answers[i, 0], 10) == 0:
          continue
      elif answers[i, 0] < 0:
          fin += "- " + str(round(answers[i, 0], 2))[1:] + " " + var[i, 0] + " "
      else:
          fin += "+ " + str(round(answers[i, 0], 2)) + " " + var[i, 0] + " "
      
    return(fin)
  
  def find_equation(input_vals, output):
    '''
    degree = degree :: dimensionality = dimensions :: input_vals = inputs (nx2; nx4):: output = output (always nx1 array)
    '''
    dimensionality = input_vals.shape[1] + 1
    degree = int(math.pow(input_vals.shape[0],1/(dimensionality-1)))
    general = degree**(dimensionality-1)
    dimSmall = dimensionality-1
    
    main = np.ones([general, general])

    for i in range(general): #equation number
          for j in range(general): #equation element
              counter = degree**np.arange(dimSmall)
              middle = (j//counter)%degree
              main[i, j] = np.prod(input_vals[i, :]**(degree-middle-1))
    
    return(np.linalg.inv(main) @ output)
      

  def find2dEquation(input_vals, output, answers):
      dimensionality = input_vals.shape[1] + 1
      degree = int(math.pow(input_vals.shape[0],1/(dimensionality-1)))
      general = degree**(dimensionality-1)
      x = np.arange(-20, 20, .1)
      y = 0
      for elements in range(general):
          y += answers[elements]*(x**(general-elements-1))
      
      fig, ax = plt.subplots(figsize=(10,10), constrained_layout=False)
      ax.plot(x, y)
      ax.set_aspect('equal')
      ax.set(xlim=(-100,100), ylim=(-100,100))
      ax.set_xlabel('x')
      ax.set_ylabel('y')
      ax.scatter(input_vals[:, 0], output[:], c=output[:])
        
      plt.ion()
      plt.show()


  
