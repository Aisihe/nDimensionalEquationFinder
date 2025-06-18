import numpy as np
import matplotlib.pyplot as plt
import math
import random

class FindPolynomial:
    def find_equation_Human(input_vals, output):
        '''
        input_vals = inputs (nx2; nx4):: output = output (always nx1 array)
        '''
        numVars = input_vals.shape[1]
        degree = int(math.pow(input_vals.shape[0],1/(numVars)))
        general = degree**(numVars)
        
        main = np.ones([general, general])

        for i in range(general): #equation number
            for j in range(general): #equation element
                main[i, j] = np.prod(input_vals[i, :]**(np.array(FindPolynomial.numberToBase(general-j-1, degree, numVars))))
        
        sup = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]          
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        var = np.empty([general, 1], dtype='U100')
        for j in range(general): #equation element
            temp = ""
        for coNum in range(numVars):
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
        input_vals = inputs (nx2; nx4):: output = output (always nx1 array)
        '''
        numVars = input_vals.shape[1]
        degree = int(math.pow(input_vals.shape[0],1/(numVars))) - 1
        general = degree**(numVars)
        
        main = np.ones([general, general])

        for i in range(general): #equation number
            for j in range(general): #equation element
                main[i, j] = np.prod(input_vals[i, :]**(np.array(FindPolynomial.numberToBase(general-j-1, degree + 1, numVars))))

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
    
    def plot1(input_vals, output, polynomial):
        x = np.arange(-20, 20, .1)
        y = FindPolynomial.evaluateFunction(polynomial, x)
        
        x1 = np.arange(-20, 20, .1)
        y1 = FindPolynomial.evaluateLoss2D1(x1)

        fig, ax = plt.subplots(figsize=(10,10), constrained_layout=False)
        ax.plot(x1, y1)
        ax.plot(x, y)
        ax.set_aspect('equal')
        ax.set(xlim=(-100,100), ylim=(-100,100))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.scatter(input_vals[:, 0], output[:], c=output[:])
            
        plt.ion()
        plt.show()

    def plot2(input_vals, output, polynomial):
        x = np.arange(-20, 20, .1)
        y = FindPolynomial.evaluateFunction(polynomial, x)
        
        x1 = np.arange(-20, 1, .1)
        x2 = np.arange(1, 2, .1)
        x3 = np.arange(2, 4, .1)
        x4 = np.arange(4, 20, .1)
        y1 = FindPolynomial.evaluateLoss2D2(x1)
        y2 = FindPolynomial.evaluateLoss2D2(x2)
        y3 = FindPolynomial.evaluateLoss2D2(x3)
        y4 = FindPolynomial.evaluateLoss2D2(x4)

        fig, ax = plt.subplots(figsize=(10,10), constrained_layout=False)
        ax.plot(x1, y1, 'y')
        ax.plot(x2, y2, 'y')
        ax.plot(x3, y3, 'y')
        ax.plot(x4, y4, 'y')
        ax.plot(x, y)
        ax.set_aspect('equal')
        ax.set(xlim=(-20, 20), ylim=(-20, 20))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.scatter(input_vals[:, 0], output[:], c=output[:])
            
        plt.ion()
        plt.show()
    def diffrentiate(input_vals, degree, numVars):
        reordered_input_vals = np.zeros((input_vals.shape[0], numVars))
        general = (degree+1)**(numVars)
        for i in range(numVars):
            for j in range(general):
                baseArr = FindPolynomial.numberToBase(j, degree+1, numVars)
                temp = baseArr[0]
                baseArr[0] = baseArr[i]
                baseArr[i] = temp #represents swapped index
                reordered_input_vals[j][i] = input_vals[FindPolynomial.baseToNumber(baseArr, degree+1)][0] #normal index to swapped index

        derivativeMatrix = np.zeros((general, general))
        for i in range(general-(degree+1)**(numVars-1)):
            derivativeMatrix[i + (degree+1)**(numVars-1)][i] = degree - ( (i) // ((degree+1)**(numVars-1)))
        reordered_input_vals = derivativeMatrix @ reordered_input_vals

        for i in range(numVars):
            swapped = []
            for j in range(general):
                swapped.append((j, i))
                baseArr = FindPolynomial.numberToBase(j, degree+1, numVars)
                temp = baseArr[0]
                baseArr[0] = baseArr[i]
                baseArr[i] = temp #represents swapped index
                if not (FindPolynomial.baseToNumber(baseArr, degree+1), i) in swapped:
                    temp = reordered_input_vals[j][i]
                    reordered_input_vals[j][i] = reordered_input_vals[FindPolynomial.baseToNumber(baseArr, degree+1)][i] 
                    reordered_input_vals[FindPolynomial.baseToNumber(baseArr, degree+1)][i] = temp
        return reordered_input_vals

    def numberToBase(n, b, dim):
        if n == 0:
            return [0]*dim
        digits = [0] * dim
        counter = 0
        while n:
            digits[counter] = int(n % b)
            n //= b
            counter += 1
        return digits[::-1]
    
    def baseToNumber(n, b):
        sum = 0
        for i in range(len(n)-1, 0, -1):
            sum = sum + n[len(n)-i-1] * b**i
        return sum + n[-1]
   
    def newtonsMethod(polynomialArr): #find zeros of a function
        derivative = FindPolynomial.diffrentiate(polynomialArr, len(polynomialArr) - 1, 1)
        n = 100
        extrema = []
        xprev = 200

        for j in range(len(derivative)): #to make sure we run it a few times and find the zeros
            x = random.randint(-n, n) #the starting point. the range for it gets smaller and smaller each iteration (these polynomials are centered at 0)
            while abs(x-xprev) > 0.1: #find zeros of derivative => extrema
                fPrimeOfX = FindPolynomial.evaluateFunction(FindPolynomial.diffrentiate(derivative, len(derivative) - 1, 1), x)
                if not fPrimeOfX == 0:
                    xprev = x
                    x = x - FindPolynomial.evaluateFunction(derivative, x)/fPrimeOfX
                else: 
                    break

            if (x, (FindPolynomial.evaluateFunction(polynomialArr, x))) not in extrema: 
                extrema.append( (x, (FindPolynomial.evaluateFunction(polynomialArr, x))) )
            n = math.ceil(n / n**(1/(len(polynomialArr)))) #on the premise that after j iterations, n should be pretty small 
            # n/(c^j) = 1 (n divided by some constant equals 10) => n = c^j => c = n**1/j (j is num iterations and c is our constant we divide by)
        
        xprev = 200
        #above finds extrema, this just finds zeros. to make this work for odd functions too. 
        for j in range(len(polynomialArr)): 
            x = random.randint(-n, n)
            while abs(x-xprev) > 0.1: 
                fPrimeOfX = FindPolynomial.evaluateFunction(derivative, x)
                if not fPrimeOfX == 0:
                    xprev = x
                    x = x - FindPolynomial.evaluateFunction(polynomialArr, x)/fPrimeOfX
                else: 
                    break
            if (x, FindPolynomial.evaluateFunction(polynomialArr, x)) not in extrema: 
                extrema.append( (x , FindPolynomial.evaluateFunction(polynomialArr, x)) )
            n = math.ceil(n / n**(1/(len(polynomialArr))))

        return FindPolynomial.bubbleSortCustom(extrema) #sorted! 
    
    def bubbleSortCustom(arr):
        for n in range(len(arr) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if arr[i][1] > arr[i + 1][1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break
        return arr
    
    def evaluateFunction(func, x):
        sum = 0
        for i in range(len(func)):
            sum = sum + func[i][0] * x**(len(func)-i-1)
        return sum

    def evaluateLoss2D1(x):
        return 0.5 * x**2 + 20 * np.sin(x)
    
    def iterativeMinimize2DExample1():
        input_vals = [[random.randint(-10, 10)], [random.randint(-10,10)], [random.randint(-10,10)]]
        output_vals = [[FindPolynomial.evaluateLoss2D1(input_vals[0][0])], [FindPolynomial.evaluateLoss2D1(input_vals[1][0])], [FindPolynomial.evaluateLoss2D1(input_vals[2][0])]] #start off the process
        

        for iterations in range(10): #don't know what my convergence condition is so i just run it a bunch
            #print(f"inputs: {input_vals}")
            #print(f"outputs: {output_vals}")
            interpolatingPolynomial = FindPolynomial.find_equation(np.array(input_vals), np.array(output_vals)) #find it's mins or its zeros (account for odd and even functions)

            extrema = FindPolynomial.newtonsMethod(interpolatingPolynomial)

            FindPolynomial.plot1(np.array(input_vals), np.array(output_vals), interpolatingPolynomial)

            #print(f"interpolatingPolynomial: {interpolatingPolynomial}")
            #print(f" minima: {extrema}")
            randomval = [extrema[0][0]]
            for i in range(len(extrema)):
                if randomval in input_vals:
                    randomval = [extrema[i][0]]
            input_vals.append(randomval)
            output_vals.append([FindPolynomial.evaluateLoss2D1(randomval[0])])

        return f" minimum value found: {min(output_vals)}"

    def evaluateFunction(func, x):
        sum = 0
        for i in range(len(func)):
            sum = sum + func[i][0] * x**(len(func)-i-1)
        return sum

    def evaluateLoss2D2(x):
        return x**6 - 2*x**4 + x**3 - x**2 - x + 2*np.sin(5*x)
        
    
    def iterativeMinimize2DExample2():
        input_vals = [[random.randint(-10, 10)], [random.randint(-10,10)], [random.randint(-10,10)]]
        output_vals = [[FindPolynomial.evaluateLoss2D2(input_vals[0][0])], [FindPolynomial.evaluateLoss2D2(input_vals[1][0])], [FindPolynomial.evaluateLoss2D2(input_vals[2][0])]] #start off the process
        

        for iterations in range(10): #don't know what my convergence condition is so i just run it a bunch
            #print(f"inputs: {input_vals}")
            #print(f"outputs: {output_vals}")
            interpolatingPolynomial = FindPolynomial.find_equation(np.array(input_vals), np.array(output_vals)) #find it's mins or its zeros (account for odd and even functions)

            extrema = FindPolynomial.newtonsMethod(interpolatingPolynomial)

            FindPolynomial.plot2(np.array(input_vals), np.array(output_vals), interpolatingPolynomial)

            #print(f"interpolatingPolynomial: {interpolatingPolynomial}")
            #print(f" minima: {extrema}")
            randomval = [extrema[0][0]]
            for i in range(len(extrema)):
                if randomval in input_vals:
                    randomval = [extrema[i][0]]
            input_vals.append(randomval)
            output_vals.append([FindPolynomial.evaluateLoss2D2(randomval[0])])

        return f" minimum value found: {min(output_vals)}"
            
 
