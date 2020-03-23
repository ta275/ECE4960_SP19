# PA5: Expansion of PA4

This directory contains an extension of PA4. An implementation of TR-BDF2 (without time-adaptation) to solve the generic ODE in the form of dx/dt = f(t,x) is provided in addition to the previous methods (Forward Euler and Runge-Kutta with and without time adaptation). In order to implement TR-BDF2, the Newton-Raphson method is used to solve the non-linear equation obtained during the trapezoidal Euler formulation and backward differentiation. This Newton-Raphson solver is implemented in nr_solver.py. The ODE solvers are implemented in ode_solver.py and verified by the script ode_verification.py. Simple RC-circuit simulation and common-source amplifier circuit simulation is performed as in programming assignment 4. However, this time, the delayed amplifier response of the common-source amplifier circuit can be observed from the graph. In addition, circuits involving inductors are used to demonstrate the increased functionality of the ODE solvers. Natural response of parallel RLC circuit is simulated. Low-pass, high-pass, and band-pass RLC filters are also simulated to demonstrate this functionality. The scripts simple_rc.py, cs_amplifier.py, parallel_rlc.py, low_pass.py, high_pass.py, band_pass.py can be run to perform these simulations and generate plots and execution time reports in the reports directory.


# Author

**Tejas Advait**



## Acknowledgments

* Prof. Edwin Kan for providing the assignment details and continuous guidance.