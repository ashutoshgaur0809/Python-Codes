if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=list()
    al = list()

for i in range (x+1):
    for j in range (y+1):
        for k in range (z+1):
            al.append([i,j,k])
            if(i+j+k!=n):
                l.append([i,j,k])
print("All possible combo: ",al)                
print("All conditional combo: ",l)                