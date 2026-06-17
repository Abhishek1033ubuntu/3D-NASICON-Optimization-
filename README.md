# 3D-Architected NASICON Solid-State Unit: Interfacial & Techno-Economic Optimization

An open-source multiphysics modeling framework utilizing **PyBaMM** and a custom **Techno-Economic Analysis (TEA)** optimizer to design an ultra-low resistance, financially viable 3D solid-state sodium-ion battery interface.

## 🚀 Executive Summary
Standard 2D flat-plate ceramic solid-state interfaces suffer from low-temperature "thermal walls" and rapid space-charge degradation. This project introduces a **3D Zigzag Interface with Logarithmic Junction Grading** to dilute local current density, lowering Area-Specific Resistance (ASR) while maximizing factory profit margins.

### 📊 Key Performance Metrics Achieved:
* **Area-Specific Resistance ($ASR$):** Reduced by **67.6%** ($68.0 \Omega \cdot cm^2$ vs $210.0 \Omega \cdot cm^2$ baseline).
* **Critical Current Density ($CCD$):** Validated at **$2.6 \text{ mA/cm}^2$** ($3.25\times$ safety margin against dendrites).
* **Optimal Structural Complexity:** Identfied a geometric sweet spot of **$2.21\times$ Area Enhancement**, balancing cell performance with factory yields to maximize net annual profits.
* **Production Cost Vector:** Target cost optimized to **$\approx \$74$/kWh**, safely under the $\$110$/kWh commercial target marker.

## 📁 Repository Structure
* `/models/01_pybamm_eis_simulation.ipynb`: Time-domain and Frequency-domain (EIS) electrochemical simulation code.
* `/models/02_techno_economic_optimizer.ipynb`: Parametric complexity vs. yield optimizer loop.

## 📈 Validated Simulation Frontier
| Nyquist Response Baseline vs 3D | Financial Optimization Sweet Spot |
|---|---|
| ![](/assets/nyquist_plot.png) | ![](/assets/optimization_frontier.png) |

## 🛠️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/Abhishek1033ubuntu/3D-NASICON-Optimization.git](https://github.com/Abhishek1033ubuntu/3D-NASICON-Optimization.git)
