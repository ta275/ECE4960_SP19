# Scientific Computing in Python

This directory contains the implementation of a sparse matrix representation data structure, numerical methods for calculating derivatives and definite integrals, numerical linear-equation solvers based on the Newton-Rhapson method, least-squares fitting, and ordinary-differential equation solvers to simulate electrical circuits.

Python 3.7 is used as the primary programming language for these implementations.

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

* Prof. Edwin Kan for providing the theoretical details and continuous guidance.
