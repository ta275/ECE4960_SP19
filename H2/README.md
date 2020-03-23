# Homework 4: Applying the Wilkinson principle to sparse-matrix computation

This directory contains the implementation of matrix in full format and compressed-row storage format.

* Part I - The sparse matrix and the full matrix is used for validation of the implementations using the Wilkinson principle when the ground truth is known. A known, small matrix of rank 5 is represented in the full matrix format as well as the compressed row storage format. Three methods which implement row permutation, row scaling, and vector product calculation are called for both formats and the resulting vector product calculated from both the formats are compared for validation.

* Part II - Once the sparse matrix implementation is verified in Part I, the sparse matrix  methods are applied to a large matrix of rank 17,758. Two different calculation methods using this large matrix is carried out which should theoretically yield the same answer. These two results are compared to further validate the sparse matrix implementation. This is another illustration of the Wilkinson principle.

The memory usage and runtime for Part II is reported.

## Author

**Tejas Advait**



## Acknowledgments

* Prof. Edwin Kan for providing the theoretical details and guidance.