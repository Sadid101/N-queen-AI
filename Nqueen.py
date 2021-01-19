import sys
def check(c,row,col,w):
    if(row>w-1):
        col=col-1
        for j in range(w):
            if(c[j][col]=="q"):
                c[j][col]=0
                check(c,j+1,col,w)
    if(col>w-1):
        for i in range(w):
            for j in range(w):
                print(c[i][j], end =" ")
            print()
        sys.exit()               
    c[row][col]="q"
    #this is where i am checking sideways
    for j in range(w):
        if(c[row][j]=="q" and j!=col):
            c[row][col]=0
            row=row+1
            check(c,row,col,w)
    #this is where i am checking downwards
    for j in range(w):                
        if(c[j][col]=="q" and j!=row):
            c[row][col]=0
            row=row+1
            check(c,row,col,w)
    #this is where i am checking diagonally
    for i in range(w):
        #downright
        if(row+i+1<w and col+i+1<w and c[row+i+1][col+i+1]=="q"):
            c[row][col]=0
            row=row+1
            check(c,row,col,w)
        #upleft
        if(row-i-1>-1 and col-i-1>-1 and c[row-i-1][col-i-1]=="q"):
            c[row][col]=0
            row=row+1
            check(c,row,col,w)
        #downleft            
        if(row+i+1<w and col-i-1>-1 and c[row+i+1][col-i-1]=="q"):
            c[row][col]=0
            row=row+1
            check(c,row,col,w)
        #upright
        if(row-i-1>-1 and col+i+1<w and c[row-i-1][col+i+1]=="q"):
            c[row][col]=0
            row=row+1
            check(c,row,col,w)
    col=col+1
    check(c,0,col,w)    
            
            
            
w=8 #this is the n of n queen
Matrix = [[0 for x in range(w)] for y in range(w)]
n=0 
m=0
check(Matrix,n,m,w)

