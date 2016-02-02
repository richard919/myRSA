#from numpy import matrix
#from numpy import linalg
#A = matrix( [[1,2,3],[11,12,13],[21,22,23]]) # Creates a matrix.
#x = matrix( [[1],[2],[3]] )                  # Creates a matrix (like a column vector).
#y = matrix( [[1,2,3]] )                      # Creates a matrix (like a row vector).
#print A.T                                    # Transpose of A.
#print A*x                                    # Matrix multiplication of A and x.
#print A.I                                    # Inverse of A.
#print linalg.solve(A, x)     # Solve the linear equation system.

def mult(A, B):
    C = [[0,0],[0,0]]
    fill(A, C)
    for i in range(2):
        for j in range (2):
            C[i][j] = ((A[i][0] * B[0][j] + A[i][1] * B[1][j]) % 5)
    return C

def fill(H,N):
    for i in range(2):
        for j in range(2):
            N[i][j] = H[i][j]
    return N

def equal(D, V):
    for i in range(2):
        for j in range(2):
            if (D[i][j] != V[i][j]):
                return False
    return True

def detone(L):
        return (1 == (L[0][0] * L[1][1] - L[1][0] * L[0][1]) % 5)

def copy(B):
        C = [[0,0],[0,0]]
        fill(B, C)
        return C

e = [0,0,0,0]

A = [[e[0], e[1]], [e[2], e[2]]]

Mthrees = []
Mfours = []

counter = 1

I = [[1,0],[0,1]]

for a in range(5):
    A[0][0] = a
    for b in range(5):
        A[0][1] = b
        for c in range(5):
            A[1][0] = c
            for d in range(5):
                A[1][1] = d
                #Q = A
                F = mult(A, mult(A, mult(A, A)))
                T = mult(A, mult(A, A))
                Fh = mult(A, A)
                

                if(equal(I, T) and detone(A) and (not equal(I, A))):
                                        Mthrees.append(copy(A))
                                        #print(A)

                if(equal(I, F) and detone(A) and (not equal(I, A)) and (not equal(I, Fh))):
                                        Mfours.append(copy(A))
                                        #print(A)

                #R = A 
                #if(not equal(Q,R)):
                #   print("Q does not equal R")
                #   print(Q, R)
                #   print('')
                #if(equal(T, A) and detone(A)):
                #   counter += 1
                #   print(counter)
                #   print(A[0])
                #   print(A[1])
                #   #print(M[0])
                #   #print(M[1])
                #   print('')

#print("Matrices of order 3:")
#print('')
#
#for matrix in Mthrees:
#        print(counter)
#        print(matrix[0])
#        print(matrix[1])
#        print('')
#        counter += 1
#print('------------------------------------------')
#print('')
#        
#counter = 1
#
#print('Matrices of order 4:')
#print('')
#
#for matrix in Mfours:
#        print(counter)
#        print(matrix[0])
#        print(matrix[1])
#        print('')
#        counter += 1
#
gold = []
#
for X in Mfours:
        for Y in Mthrees:
                leftsideofequation = mult(X, Y)
                rightsideofequation =  mult( mult(Y, Y),X)
                if (equal(leftsideofequation,rightsideofequation)):
                        #print(leftsideofequation, '=', rightsideofequation)
                        gold.append([X,Y,leftsideofequation])

for printline in gold:
        print(counter)
        print('')
        print "X = " + str(printline[0][0]) + " and Y = " + str(printline[1][0]) + " and XY = Y^2X = " + str(printline[2][0])
        print "    " + 3 * ' ' + str(printline[0][1]) + "         " + 6 * ' ' + str(printline[1][1]) + "                 " + 15 * ' ' + str(printline[2][1])
        print('')
        counter += 1
                
                
