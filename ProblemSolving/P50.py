def rotateTheBox(box):
        row = len(box[0])
        column= len(box)
        
        rotatedBox= [[0]*column for _ in range(row)]
        # column-=1
        # row=-
        print(rotatedBox,row,column)
        
        for i in range(column,-1,-1):
            print(i)
            for j in range(row-2,-1,-1):
                if box[i][j+1]=="." and box[i][j]=="#":
                    rotatedBox[i][j+1]="#"
                    rotatedBox[i][j]="."
        
        return rotatedBox
box=[["#",".","#"]]
print(rotateTheBox(box))