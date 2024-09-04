import random
def start_game():
    mat=[[0 for _ in range(4)]for _ in range(4)]
    return mat
def add_new_two(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'GAME NOT OVER'
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'GAME NOT OVER'
    return 'LOST'
def compress(mat):
    new_mat=[[0 for _ in range(4)]for _ in range(4)]
    c=False
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    c=True
                pos+=1
    return new_mat,c
def merge(new_mat):
    c=False
    for i in range(4):
        for j in range(3):
            if new_mat[i][j]==new_mat[i][j+1] and new_mat[i][j]!=0:
                new_mat[i][j]=new_mat[i][j]*2
                new_mat[i][j+1]=0
                c=True
    return new_mat,c
def reverse(mat):
    new_mat=[[] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat
def transpose(mat):
    new_mat=[[] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
def left_move(mat):
    mat1,c1=compress(mat)
    mat1,c2=merge(mat1)
    c=c1 or c2
    mat1,n=compress(mat1)
    return mat1,c
def right_move(mat):
    mat1=reverse(mat)
    mat1,c=left_move(mat1)
    mat1=reverse(mat1)
    return mat1,c
def up_move(mat):
    mat1=transpose(mat)
    mat1,c=left_move(mat1)
    mat1=transpose(mat1)
    return mat1,c
def down_move(mat):
    mat1=transpose(mat)
    mat1=reverse(mat1)
    mat1,c=left_move(mat1)
    mat1=reverse(mat1)
    mat1=transpose(mat1)
    return mat1,c