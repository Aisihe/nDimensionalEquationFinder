import numpy as np
import matplotlib.pyplot as plt

class FindPolynomial:
  def find_equation_Human(degree, dimensionality, input_vals, output):
    '''
    degree = degree :: dimensionality = dimensions :: input_vals = inputs (nx2; nx4):: output = output (always nx1 array)
    '''
    degree = degree + 1
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
  
  def find_equation(degree, dimensionality, input_vals, output):
    '''
    degree = degree :: dimensionality = dimensions :: input_vals = inputs (nx2; nx4):: output = output (always nx1 array)
    '''
    degree = degree + 1
    general = degree**(dimensionality-1)
    dimSmall = dimensionality-1
    
    main = np.ones([general, general])

    for i in range(general): #equation number
          for j in range(general): #equation element
              counter = degree**np.arange(dimSmall)
              middle = (j//counter)%degree
              main[i, j] = np.prod(input_vals[i, :]**(degree-middle-1))
    
    return(np.linalg.inv(main) @ output)
      

  def f(x, y, degree, dimensionality, answers):
    total = 0
    degree += 1
    general = degree**(dimensionality-1)
    for j in range(general):
        total += answers[j]*y**(degree-(j//degree)%degree-1)*x**(degree-(j%degree)-1)
    return total

  def find2dEquation(input_vals, output, answers, degree, dimensionality):
      degree += 1
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

  def find3dEquation(input_vals, output, degree, dimensionality, answers):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = FindPolynomial.f(x=X, y=Y, degree=degree, dimensionality=dimensionality, answers=answers)
  
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, linewidth=1, cmap='hsv')
    ax.scatter3D(input_vals[:, 0], input_vals[:, 1], output[:, 0], c=output[:], alpha=1)
    ax.set(xlim=(-10,10), ylim=(-10,10), zlim=(-10,10))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.ion()
    plt.show()


  
