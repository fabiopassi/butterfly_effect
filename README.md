# butterfly_effect

This repo contains the necessary files to perform the simulation of a chaotic system.

## Physics background

A chaotic system is a dynamical system described by deterministic laws that presents a huge sensitivity to the initial conditions.

In this simulation, an exaple of chaotic system is presented, i.e. a particle bouncing in a circular guide: the system is composed by many identical non-interacting particles. Each of them starts from an initial position that is slightly different compared to the others. The only type of interaction that a ball can experience is an elastic collision with a circular guide, which inverts the radial component of its velocity.

As one can see, despite starting from almost indistinguishable initial positions, after some time the particles may follow entirely different trajectories, as it is expected in a chaotic system (see butterfly effect page on Wikipedia).

Other chaotic systems in physics are, for example, the double pendulum, the atmosphere and some particular electronic circuits.

> NOTE: the fact that the atmosphere is a chaotic system is the reason for which the weather forecast is reliable only for a couple of subsequent days.

## Technical details: python version

The scripts are written in python. The only additional packages required to run the simulation are `numpy`, `numba` and `matplotlib`; if you have conda installed, the command:

```bash
conda create -n butterfly numba matplotlib
```

should create an environment with all the necessary packages.

After this, you can start the simulation with the commands:

```bash
conda activate butterfly
python main.py
```

## Contact

If you have any doubt or if you spot mistakes/bugs, feel free to contact [fabio.passi24@gmail.com](fabio.passi24@gmail.com)
