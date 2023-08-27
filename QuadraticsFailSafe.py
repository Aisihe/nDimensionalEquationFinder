import numpy as np
import matplotlib.pyplot as plt

def find_equation(first_dim, dimensionality, general, input_vals, output):
  dimSmall = dimensionality-1
  main = np.ones([general, general])

  #done in multiple passes
  for i in range(general): #equation number
        for j in range(general): #equation element
            counter = first_dim**np.arange(dimSmall)
            middle = (j//counter)%first_dim
            main[i, j] = np.prod(input_vals[i, :]**(first_dim-middle-1))
  
  sup = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]          
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  var = np.empty([general, 1], dtype='U100')
  for j in range(general): #equation element
    temp = ""
    for coNum in range(dimSmall):
        counter = first_dim**coNum
        middle = (j//counter)%first_dim
        temp += letters[coNum] + sup[first_dim-middle-1]
        var[j, 0] = temp
    #print(temp)
        

  answers = np.linalg.inv(main) @ output
  
  
  return([answers, var])

##################################################################################################

choice = int(input("Custom or example? (1, 2): "))

if choice == 1:
  

  first_dim = int(input("Degree of polynomial: ")) + 1
  dimensionality = int(input("Dimensions: "))
  general, dimSmall = (first_dim)**(dimensionality-1), dimensionality-1
  input_vals, output = np.empty([general, dimSmall]), np.empty([general, 1])
  print(f"Input {general} pairs of coordinates")

  for i in range(general):
      inp = input(f"Coordinate pair {i}: ")
      coords = tuple(float(x) for x in inp.split(","))
      for j in range(dimSmall):
          input_vals[i, j] = coords[j]
      output[i] = coords[-1]

elif choice == 2:
    exNum = int(input("Enter the example number (1-4): "))
    
    if(exNum == 1):
      input_vals = np.array([[0, 0], [1, 1], [-1, -1], [1, 2], [2, 1], [0, 1], [0, 2], [3, 3], [3, 2]])
      output = np.array([[0], [1],[2],[5],[5],[1],[4],[18],[13]])
    elif(exNum == 2):
      input_vals = np.array([[0, 0], [1, 1], [-1, -1], [1, 2], [2, 1], [0, 1], [0, 2], [3, 3], [3, 2]])
      output = np.array([[0], [2],[2],[5],[5],[1],[4],[18],[13]])
    elif(exNum ==3):
      input_vals = np.array([[0, 0], [1, 1], [1, 2], [2, 1]])
      output = np.array([[0], [2],[3],[3]])
    elif(exNum == 4):
      input_vals = np.array([[0], [4], [-3], [5], [-1.5]])
      output = np.array([[0], [2],[3],[3], [-1]])
    dimensionality = int(len(input_vals[0]) + len(output[0]))
    dimSmall = int(dimensionality - 1)
    first_dim = int(len(output)**(1/dimSmall))
    general = int((first_dim)**(dimensionality-1))

##################################################################################################

answers, vars = find_equation(first_dim, dimensionality, general, input_vals, output)
fin = ""
print(answers)
print(vars)
for i in range(general):
   if answers[i, 0] < 0:
      fin += str(round(answers[i, 0], 2)) + " " + vars[i, 0] + " "
   else:
      fin += "+ " + str(round(answers[i, 0], 2)) + " " + vars[i, 0] + " "
print(f"\n a = x, b = y, c = z, etc. \n\n {fin}")




def f(x, y):
    total = 0
    answers = find_equation(first_dim, dimensionality, general, input_vals, output)[0]
    for j in range(general):
        total = total + (answers[j]*y**(first_dim-(j//first_dim)%first_dim-1)*x**(first_dim-(j%first_dim)-1))
    return total

if dimensionality == 2:
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

    plt.show()

elif dimensionality == 3:
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
  
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, linewidth=1, cmap='hsv')
    ax.scatter3D(input_vals[:, 0], input_vals[:, 1], output[:], c=output[:], alpha=1)
    ax.set(xlim=(-10,10), ylim=(-10,10), zlim=(-10,10))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


    plt.show()
