# what is sparse data: Sparse data is the data that has a mostly unused elements .like teh elements that dont carry any information. [1,0,2,0,4,5,,6,9,2,4]
# sparse data example [1,0,2,0,0,0,3,0,0,0,4]
# Dense Array: [2,5,3,6,7,8,9,6,3,2,1]
# how to work with Sparse data. 
# Scipy has a module scipy.sparse function . there are two matrix in this sparse : CSC( compressed Sparse Colums), CSR(compressed Sparse Row)

# CSR Matrics: here we will  create a CSR matrics from an array 
import numpy as np
from scipy.sparse import csr_matrix
x=np.array([0,0,0,0,0,0,1,1,1,1,1,0,2])
print(csr_matrix(x))

# Sparse matrix Methods
from scipy.sparse import  csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(x).data)

# what is we want to count non zeors, we can do this via count_nonzero() method
from scipy.sparse import  csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(x).count_nonzero())

# for removing the zero elements from the matrix we will use eleminate_zeros().
from scipy.sparse import  csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
y=csr_matrix(x)
y.eliminate_zeros()
print(y)

# eliminating duplicate entries with the sum_duplicates() method :
from scipy.sparse import  csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
y=csr_matrix(x)
y.sum_duplicates()
print(y)

# here we will convert csr to csc with tocsc()
from scipy.sparse import  csr_matrix
x=np.array([[0,0,0],[0,0,1],[1,0,2]])
y=csr_matrix(x).tocsc()
print(y)
