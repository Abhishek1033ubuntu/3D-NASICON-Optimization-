import pybamm
import numpy as np
import matplotlib.pyplot as plt

# 1. Initialize the baseline physical model
model = pybamm.lithium_ion.SPM()
param = pybamm.ParameterValues("Marquis2019")

# 2. Update with optimized NASICON/3D parameters
param.update({
    "Electrolyte conductivity [S.m-1]": 0.22,
    "Electrode height [m]": 0.1 * 3.0,          # 3x baseline area factor
    "Electrode width [m]": 0.1,
    "Negative electrode exchange-current density [A.m-2]": 5,
    "Positive electrode exchange-current density [A.m-2]": 2,
}, check_already_exists=False)

# 3. Solve the time-domain initial state
sim = pybamm.Simulation(model, parameter_values=param)
sol = sim.solve(t_eval=[0, 3600])

print("Electrochemical initial time-domain simulation complete.")