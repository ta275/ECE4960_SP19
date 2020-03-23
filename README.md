# Scientific Computing in Python

## Introduction

Welcome to my repository on Scientific Computing in Python. This repository is still under construction so I apologize for any incomplete documentation, although all of the code is complete and present in the sub-directories.

My final goal is very ambitious: I want to see this repository to be able to justify the use of Python for scientific research, which is still dominated by Fortran and MATLAB.

To achieve this goal I aim to do the following two main things:

** Theoretical Concepts: I wish to explain some fundamental and intermediate concepts of scientific computing such as error analysis, digital representation of real numbers, numerical differentiation and integration, iterative and direct matrix solvers, least-squares, and ODE solvers.

** Software: Along with the theoretical concepts, I want to emphasize good coding practices and extensive software development. I aim to instill modular thinking among the readers. The most fundamental skill possessed by any good programmer is the ability to break down large problems into smaller sub-problems, preferably independent of each other. We will see how Python can be used to achieve modularity efficiently and swiftly, and after a point, almost effortlessly! 


## Why Python?

Python was chosen as the language for this repository due to its ever-increasing popularity, ease of use, versatality, and existence of packages such as NumPy, SciPy, and Matplotlib - which makes it ideal for Scientific Computing applications.

Compared to MATLAB, Python is completely free and there are many open-source packages available which provide similar functionality as MATLAB packages. I believe Python wrapped around C/C++ is the future of Scientific Computing.

If you follow the code closely, you will observe highly modularized design, and strong object-oriented programming done in Python. The code could be a good starting point for novice (and even some advanced) Python users to learn OOP. Although Python lacks certain OOP features such as *encapsulation*, it does possess all the necessary tools required to develop highly modularized software which is easy to write, and simple to understand.

I encourage you to read [this](https://developer.ibm.com/dwblog/2018/use-python-for-scientific-research/) article by [Vinay Rao](https://developer.ibm.com/author/vinay.rao/)from the IBM developerWorks blog for further motivation for using Python for scientific computing.

## What is already here?

This repository contains the implementation of a sparse matrix data structure, numerical methods for calculating derivatives and definite integrals, numerical linear-equation solvers based on the Newton-Rhapson method, least-squares fitting, and ordinary-differential equation solvers to simulate electrical circuits.

You are free to use any code as long as you acknowledge the source.

Python 3.7 is used as the primary programming language for these implementations. You can find a "reports" directory in each of the following sub-directories which contains all the generated reports and plots.

* **PA1: Arithmetic Exception Handling:** This directory contains the implementation of a utility program that can observe and validate the exception handling of the integer and floating-point arithmetic in Python 3.7. The exception is validated against IEEE 754 standard for integer and floating-point representation by binary bits.


* **PA2:  Modular Testing in Sparse Matrix Solvers:** This directory contains the implementation of matrix in full format and compressed-row storage format and an implementation of the Jacobi iterative solver. The implementation is thoroughly tested against a sparse matrices of varying sizes. The largest sparse matrix has **rank 5000** and **253677 nonzero** entries. Computational runtime and memory usage checks are reported.

* **PA3:  Parameter Extraction from Least-Squares Fitting:** This directory contains an implementation of least-square fitting and parameter extraction with simple graphical visualization.

* **PA4:  Simple Ordinary Differential Equation Solver:** This directory contains an implementation of forward Euler and Runge-Kutta method (RK34 with and without adaptive steps) to solve the generic ODE of the form of dx/dt = f(t,x). These solvers are implemented in ode_solver.py and verified by the script ode_verification.py. Simple RC-circuit simulation and common-source amplifier circuit simulation is performed as described by tasks 4 and 5 of the assignment, repectively. The scripts simple_rc.py and cs_amplifier.py can be run to perform these simulations and generate plots and execution time reports in the reports directory.


* **PA5:  Extended ODE Solver:** This directory contains an extension of PA4. An implementation of TR-BDF2 (without time-adaptation) to solve the generic ODE in the form of dx/dt = f(t,x) is provided in addition to the previous methods (Forward Euler and Runge-Kutta with and without time adaptation). In order to implement TR-BDF2, the Newton-Raphson method is used to solve the non-linear equation obtained during the trapezoidal Euler formulation and backward differentiation. This Newton-Raphson solver is implemented in nr_solver.py. 

* **H1: Differentiation in Local Analysis:** This directory contains the implementation of differentiation of a quadratic function and a cubic function.


* **H2: Applying the Wilkinson Principle to Sparse Matrix Computation:** This directory contains the implementation of matrix in full format and compressed-row storage format.


## Author

**Tejas Advait**

## Acknowledgments

* Prof. Edwin Kan at Cornell University for providing the theoretical details and continuous guidance.
