#!/usr/bin/env python

"""
This function calculates inverse of a matrix
First it checks if matrix is square and then recursively uses itself to
drill down to 2nd level matrix
Then math comes in.
"""
from __future__ import division

def det(a):

    detValue = 0

    #check if matrix is ok
    for i in xrange(len(a)):
        if len(a[i]) != len(a):
            print "Matrix isnt square. Can not calculate determinant."
            exit()



        #start det calc
    if len(a) == 2:
        return (a[0][0]*a[1][1] - a[0][1]*a[1][0])

    elif len(a) > 2:
        #init -1 size matrix
        aMod = [0]*(len(a)-1)
        for i in range(len(a)-1):
            aMod[i] = [0] * (len(a[i]) -1)


        # Calculate minors and lower the rank of matrix
        # this might be not the easiest way but that how I made my way
        # We can optimise it to look for zeroes in a row but that can cause
        # more complications with iterators


        for k in xrange(len(a)):
            for i in xrange(len(a)):
                #fix j postition
                j1 = 0
                for j in xrange(len(a)):
                    if (k == j) or (i == 0 ):
                        #print ("skip" ,k,i,j,a[i][j])
                        continue;
                    else :
                        #print ("put" ,k,i,j, a[i][j])
                        aMod[i-1][j1] = a[i][j]
                        j1+=1

                        # UP can not easily match the iterators so using
                        # another one to count j iterator for new array
                        # in case if value is acceptable


            # call det function recursively
            #print aMod, a[0][k]
            if k % 2 == 0:
                detValue += a[0][k]*det(aMod)
            else:
                detValue -= a[0][k]*det(aMod)



    # take element and * to A(minor)  - pass aMod list
    # formula j = const =1 and row number is 0
    # for i in xrange(len(a)):

    #print detValue
    return detValue

def obr(a):

    detValue = 0
    result = 0

    globaDetValue = det(a)
    detValue = 0

    if globaDetValue == 0 :
        print "Cant calculate inversed matrix. Matrix is singular "
        exit()
    else:
        print "determinant is ", globaDetValue

    #marix for det calc
    aMod = [0]*(len(a)-1)
    for i in range(len(a)-1):
        aMod[i] = [0] * (len(a[i]) -1)

    #Additions marix
    aM = [0]*(len(a))
    for i in range(len(a)):
        aM[i] = [0] * (len(a[i]))

    #Transposed marix (and later inversed)
    aT = [0]*(len(a))
    for i in range(len(a)):
        aT[i] = [0] * (len(a[i]))




    # Calculate additions

    i1 =0
    j1 =0

    for iM in xrange(len(a)):
        for jM in xrange(len(a)):
            for i in xrange(len(a)):
                j1 =0
                for j in xrange(len(a)):
                    if (i == iM) or (j == jM):
                        print ("skip" ,i,j,a[i][j], "to", i1,j1,  "on cycle", iM,jM)
                        continue;
                    else :
                        aMod[i1][j1] = a[i][j]
                        print ("put " ,i,j,a[i][j], "to ", i1,j1, aMod[i1][j1], "on cycle", iM, jM, aMod)
                        j1+=1
                if i != iM:
                    i1+=1

            # assign signs acccordingly
            detValue = det(aMod)
            print ("det for ", aMod, "is",detValue)
            print iM,jM
            if (iM+jM) % 2 == 0:
                sign = 1
            else:
                sign =-1
            # temporary put items here
            aM[iM][jM] = sign * detValue
            i1 = 0

            # transpose and multiply at the same time
            aT[jM][iM] = float((aM[iM][jM])/globaDetValue)





    print aM
    print aT
    return aT

def matrixMultiply(a,b):
        """ Returns product of two matrices
            Also checks if matrices are allowed to be multiplied
        """

#size check
# a[i][m] - size ob matrix a
# b[m][j] - size of matrix b
# so 'm' should be equal

        if len(a[0]) != len(b):
            print "Matrices can not be multiplied"
            exit()



        #initialization of  result matrix
        print "multiplying matrices",a,b
        c = [0]*len(a)
        for i in xrange(len(a)):
            c[i] = [0] * len(a[i])
        # taking 1st item list length (there should be at least one item)
        for i in xrange(len(a[0])):
            for j in xrange(len(a)):
                for m in xrange(len(a[j])):
                    #print a[i][m],b[m][i]
                    c[i][j] += a[i][m]*b[m][j]

        print "multiplying result is",c
        return c



a  = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]

b = [[1,2,3],
    [4,5,6],
    [7,8,7]]

c = [[1,2,3],
    [2,3,1],
    [3,1,2]]

#print  det(b)
#k = obr(b)
print "--------------------------------checking"
print matrixMultiply(b,obr(b))
