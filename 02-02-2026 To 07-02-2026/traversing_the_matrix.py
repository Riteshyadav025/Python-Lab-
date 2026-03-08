def spiralOrder(mat):
    result = []
    
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    
    while top <= bottom and left <= right:
        
        # Traverse top row
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        
        # Traverse right column
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse bottom row
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse left column
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
            
    return result


mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

print(spiralOrder(mat))
