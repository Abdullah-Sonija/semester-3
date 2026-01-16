def addMatrix(a,b):
    return [ [ a[i][j]+b[i][j] for j in range(len(a[0])) ] for i in range(len(a)) ]

def multiplyMatrix(a,b):
    result=[ [ 0] *len(b[0]) for _ in range(len(a[0])) ]
    for i in range(len(a[0])):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j]+=a[i][j]*b[i][j]
    return result


A=[[1,2],[3,4]]
B=[[7,8],[5,9]]
print(f"Addition of A and B: {addMatrix(A,B)}")
print(f"Multiplication of A and B: {multiplyMatrix(A,B)}")