# Lagrangian Equations Pendulum Simulator

## Overview
The **Lagrangian Equations Pendulum Simulator** is a Python-based tool that simulates the motion of a pendulum using Lagrangian mechanics. The simulation animates the pendulum's motion in 3D, complete with real-time rendering of its trace (path) to visualize the beautiful patterns it creates.

## Features
- **3D Animation**: Real-time visualization of the pendulum's motion.
- **Path Tracing**: Displays the trajectory of the pendulum bob as it swings.
- **Lagrangian Mechanics**: Uses precise mathematical modeling for realistic motion.

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- SciPy

Install the dependencies using pip:
```bash
pip install numpy matplotlib scipy
```

## Usage
1. Clone or download the repository.
2. Run the simulation script:
   ```bash
   python lagrangian_pendulum_simulator.py
   ```
3. Watch the pendulum swing and trace its path in the animated 3D plot.

## How It Works
- The simulation uses Lagrangian mechanics to derive the equations of motion for a pendulum.
- A numerical solver computes the pendulum's trajectory over time.
- The animation displays both the pendulum's motion and its trace in a 3D plot.

## Customization
You can modify key parameters in the script:
- **Radius (`R`)**: Size of the circular base.
- **Length (`L`)**: Length of the pendulum string.
- **Angular Velocity (`omega`)**: Speed of the circular motion.
- **Simulation Time (`tmax`)**: Total duration of the simulation.

