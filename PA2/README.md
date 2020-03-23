# Programming Assignment 2: Modular Testing in Sparse Matrix Solvers

This directory contains the implementation of matrix in full format and compressed-row storage format and an implementation of the Jacobi iterative solver.

Modular testing of different matrix operations is performed using the Wilkinson Principle. Furthermore, direct testing of the sparse matrix implementation is done using the compressed-row storage format provided in the Scipy library.

The Jacobi solver is tested by applying it to a very large linear system of rank 5000 and reporting the normalized residual norm.

Computational time and memory usage is reported to validate the efficiency of the implementation.

A short report documenting the modular design, testing strategies and the results achieved is also provided.

# Author

**Tejas Advait**



## Acknowledgments

* Prof. Edwin Kan for providing the assignment details and continuous guidance.