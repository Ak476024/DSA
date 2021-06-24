def rotateTheBox(box):
    row = len(box[0])
    column= len(box)
    
    rotatedBox= [[0]*column for _ in range(row)]
    column-=1
    row-=1
    print(rotatedBox)
    print(ro, column)
    for i in range(column,-1,-1):
        for j in range(row-1,-1,-1):
            print(i,j,rotatedBox)
            if box[i][j+1]=="." and box[i][j]=="#":
                rotatedBox[j+1][len(box)-i-1]="#"
                rotatedBox[j][len(box)-i-1]="."
            elif box[i][j+1]=="#" and box[i][j]=="#":
                rotatedBox[j][len(box)-i-1]="#"
            elif box[i][j+1]=="." and box[i][j]=="*":
                rotatedBox[j][len(box)-i-1]="*"
                rotatedBox[j+1][len(box)-i-1]="."
            elif box[i][j+1]=="*" and box[i][j]=="#":
                rotatedBox[j+1][len(box)-i-1]="*"
                rotatedBox[j][len(box)-i-1]="#"               

            elif box[i][j]=="*":
                rotatedBox[j][len(box)-j-1]="*"
    
    return rotatedBox
box=[["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
print(rotateTheBox(box))
hmac-sha1, hmac-sha2-25,  hmac-sha2-51,  umac-64@openssh.co,  umac-128@openssh.co, hmac-sha1-etm@openssh.co,  hmac-sha2-256-etm@openssh.co,  hmac-sha2-512-etm@openssh.co, umac-64-etm@openssh.co, umac-128-etm@openssh.com