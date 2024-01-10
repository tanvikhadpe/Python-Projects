SIZE = 5
#maze problem
maze = [
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,0]    
]
solution = [[0]*SIZE for i in range(SIZE)]

count = 0
def solvemaze(r, c):
    global count
    count+=1
    if (r==SIZE-1) and (c==SIZE-1):
        solution[r][c] = 1;
        return True;
    if r>=0 and c>=0 and r<SIZE and c<SIZE and solution[r][c] == 0 and maze[r][c] == 0:
        solution[r][c] = 1
        for d in solution:
            print (d)
        print ("-------------",count)
        if solvemaze(r+1, c):
            return True
        if solvemaze(r, c+1):
            return True
        if solvemaze(r-1, c):
            return True
        if solvemaze(r, c-1):
            return True
        solution[r][c] = 0;
        for d in solution:
            print (d)
        print ("-------------",count)
        return False;
    return 0;
if(solvemaze(0,0)):
    for i in solution:
        print (i)
else:
    print ("No solution")



