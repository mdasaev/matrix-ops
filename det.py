#!/usr/bin/env python

"""
This function calculates determinant of a matrix
First it checks if matrix is square and then recursively uses itself to
drill down to 2nd level matrix
Then math comes in.
"""


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
                        print ("skip" ,k,i,j,a[i][j])
                        continue;
                    else :
                        print ("put" ,k,i,j, a[i][j])
                        aMod[i-1][j1] = a[i][j]
                        j1+=1

                        # UP can not easily match the iterators so using
                        # another one to count j iterator for new array
                        # in case if value is acceptable


            # call det function recursively
            print aMod, a[0][k]
            if k % 2 == 0:
                detValue += a[0][k]*det(aMod)
            else:
                detValue -= a[0][k]*det(aMod)



    # take element and * to A(minor)  - pass aMod list
    # formula j = const =1 and row number is 0
    # for i in xrange(len(a)):


    return detValue




a  = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]

b = [[1,2,3],
    [4,5,6],
    [7,8,9]]

c = [[1,2,3],
    [2,3,1],
    [3,1,2]]

print  det(b)
