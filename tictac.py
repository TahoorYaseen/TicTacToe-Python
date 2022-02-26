matrix = [['0,0','0,1','0,2'],
        ['1,0','1,1','1,2'],
        ['2,0','2,1','2,2']]


def printMatrix(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end=' ')
        print()

printMatrix(matrix)
print('player 1 will play first and will mark with x')
player = 1


def forCol(i,j,matrix):
    
    lis=[]
    if i+1<3:
        lis.append(i+1)
    if i+2<3:
        lis.append(i+2)
    if i-1>=0:
        lis.append(i-1)
    if i-2>=0:
        lis.append(i-2)
    
    if matrix[i][j] == matrix[lis[0]][j] == matrix[lis[1]][j]:
        return True

    return False



def forRow(i,j,matrix):
    
    lis=[]
    if j+1<3:
        lis.append(j+1)
    if j+2<3:
        lis.append(j+2)
    if j-1>=0:
        lis.append(j-1)
    if j-2>=0:
        lis.append(j-2)
    if matrix[i][j] == matrix[i][lis[0]] == matrix [i][lis[1]]:
        return True 
    
    return False


def forDiagonal(i,j,matrix):
    lis = []
    if i-1 >=0 and j-1>=0:
        lis.append(i-1)
        lis.append(j-1)
    if i-2 >=0 and j-2>=0:
        lis.append(i-2)
        lis.append(j-2)
    if i+1 <3 and j+1<3:
        lis.append(i+1)
        lis.append(j+1)
    if i+2 <3 and j+2<3:
        lis.append(i+2)
        lis.append(j+2)
    if i-1>=0 and j+1<3:
        lis.append(i-1)
        lis.append(j+1)
    if i-2>=0 and j+2<3:
        lis.append(i-2)
        lis.append(j+2)
    if i+1<3 and j-1>=0:
        lis.append(i+1)
        lis.append(j-1)
    if i+2<3 and j-2>=0:
        lis.append(i+2)
        lis.append(j-2)


    if matrix[i][j] == matrix[lis[0]][lis[1]] == matrix[lis[2]][lis[3]]:
        return True

    return False
def checkForWin(i,j,matrix):
    win = False
    if forCol(i,j,matrix):
        win = True
    if forRow(i,j,matrix):
        win = True
    if forDiagonal(i,j,matrix):
        win= True
    return win 


ans = False
for k in range(9):
    if player==1:
        print('\nplayer 1 enter position')
        [i,j] = map(int,input().split(','))
        matrix[i][j] = ' X '
        ans = checkForWin(i,j,matrix)
        if ans == True:
            printMatrix(matrix)
            print()
            print('player 1 wins')
            break
        print()
        printMatrix(matrix)
        player = 2
    if player == 2:
        print('\nplayer 2 enter position')
        [i,j] = map(int,input().split(','))
        matrix[i][j] = ' O '
        ans = checkForWin(i,j,matrix)
        if ans == True:
            printMatrix(matrix)
            print()
            print('player 2 wins')
            break
        print()
        printMatrix(matrix)
        player = 1

if ans==False:
    print('game Draw')

