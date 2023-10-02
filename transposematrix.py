def transposeMatrix(matrix):
    new_matrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        new_matrix.append(newRow)
    return new_matrix
    
    
# The provided code defines a function named transposeMatrix that transposes a matrix.
# It uses nested loops to iterate over the rows and columns of the original matrix and constructs 
# the transposed matrix element by element.

# The function creates an empty list called new_matrix to store the transposed matrix. 
# It then iterates over the columns of the original matrix using the outer loop and the rows using the inner loop.

# Within the inner loop, the code retrieves the element at the current row and column in the 
# original matrix and appends it to a new row list called newRow. This effectively swaps the 
# row and column indices, transposing the matrix.

# After the inner loop completes for a column, newRow is appended to new_matrix to 
# form a row in the transposed matrix. This process continues until all columns in the original matrix are processed.

# Finally, the function returns the new_matrix, representing the transposed matrix.

# This method is applicable to matrices of any shape and provides a simple and 
# straightforward way to transpose a matrix using nested loops.