"""
ECE 4960 SPRING 2019
Programming Assignment 2
Generator Script
Authors: Tejas Advait (TA275)

Functionality: Uses sparse_generator to create matrices in the SparseMatrix format.
"""

import sparse_generator as sg

sg.from_csv_crs('mat1/rowPtr.csv',
				'mat1/colInd.csv',
				'mat1/value.csv',
				'mat1/sparse_mat1.bin')

assert(sg.from_csv_crs_valid('mat1/rowPtr.csv',
							'mat1/colInd.csv',
							'mat1/value.csv',
							'mat1/sparse_mat1.bin') == True)

print ("mat1 sparse matrix generated successfully.")

sg.from_mtx('memplus/memplus.mtx','memplus/memplus_sparse.bin')

assert(sg.from_mtx_valid('memplus/memplus.mtx','memplus/memplus_sparse.bin') == True)

print ("memplus sparse matrix generated successfully")