# Programming Assignment 5: Expansion of Programming Assignment 4

This directory contains an extension of programming assignment 4. An implementation of TR-BDF2 (with and without time-adaptation) to solve the generic ODE in the form of dx/dt = f(t,x) is provided in addition to the previous methods (Forward Euler and Runge-Kutta with and without time adaptation). In order to implement TR-BDF2, the Newton-Raphson method is used to solve the non-linear equation obtained during the trapezoidal Euler formulation and backward differentiation. This Newton-Raphson solver is implemented in nr_solver.py. The ODE solvers are implemented in ode_solver.py and verified by the script ode_verification.py. Simple RC-circuit simulation and common-source amplifier circuit simulation is performed as in programming assignment 4. However, this time, the delayed amplifier response of the common-source amplifier circuit can be observed from the graphs. In addition, circuits involving inductors are used to increase the functionality of the SPICE simulator. RF resonator with RLC in parallel and low-pass, high-pass, and band-pass RLC filters are simulated to demonstrate this functionality. The scripts simple_rc.py, cs_amplifier.py, resonator.py, and filters.py can be run to perform these simulations and generate plots and execution time reports in the reports directory.


# Author

**Tejas Advait**



## Acknowledgments

* Prof. Edwin Kan for providing the assignment details and continuous guidance.