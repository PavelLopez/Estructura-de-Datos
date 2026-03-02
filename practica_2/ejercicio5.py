#[5 6 13]   [1 2 17]
#[3 10 1] X [6 5 12]
#[2 11 3]   [3 11 12]

A = [[5,6,13],[3,10,1],[2,11,3]]
B = [[1,2,17],[6,5,12],[3,11,12]]
C = [[0,0,0],[0,0,0],[0,0,0]]
sumatoria = 0

for i in range(len(A[0])):

    for j in range(len(B[0])):

        for k in range(len(A[0])):
            sumatoria+= A[i][k]*B[k][j]
            C[i][j]=sumatoria
            sumatorias=0

print(C)