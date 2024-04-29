# ***********************************************
# *         SCRIPT TO SHOW BUTTERFLY EFFECT     *
# ***********************************************

# Importing modules
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import random


# Variables
R = 5                                               # Radius of the circular guide
r = 0.05                                            # Radius of the particles
N = 100                                             # Number of balls
dx = 0.001                                          # Uncertainty in the initial position
balls = np.zeros((N, 3, 2))                         # For all the balls (dimension 0) I store position, velocity and acceleration (dimension 1) in both x and y (dimension 2)
dt = 0.001                                          # Timestep
md_steps = 75000                                    # Total number of steps for the MD procedure
t_sample = 15                                       # Steps every which I take a snapshot
traj = []                                           # Trajectory
skin = R/5                                          # Sort of "skin" parameter for contact list calculation
update_contact_list = 20                            # Steps every which I update the contact list
contact_list = np.zeros(N)                          # Array that tells me who is near the guide: 1 = near; 0 = far
g = -1                                              # Gravitational acceleration

# Initialize positions with slightly different x
x_0 = R * (np.random.rand(1) - 0.5)
balls[:,0,0] = x_0 * np.ones(N) + dx * (np.random.rand(N) - 0.5)

# Initialize acceleration along y as g (gravity)
balls[:,2,1] = g * np.ones(N)

# Time evolution
for i in range(md_steps) :

    # Time evolution
    balls = velocity_verlet(balls, dt)

    # Evaluate contact list, i.e. list of particles which are closer than "skin" to the wall
    if i % update_contact_list == 0 :
        contact_list = eval_contact_list(balls, R, r, skin)

    # Check rebound
    balls = check_rebound(balls, contact_list, r, R, g)

    # Save coordinates
    if i % t_sample == 0:
        traj.append(balls[:,0,:].copy())


# Plot
plt.ion()

fig,ax = plt.subplots(1, 1, figsize=(10,6))
ax.set_xlim((-R - R/10, R + R/10))
ax.set_ylim((-R-R/10, R/10))
colors = [ ( "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) ) for i in range(N) ]

x_guide = np.linspace(-R, R, 2000)
y_guide = - np.sqrt( R*R - np.square(x_guide) )
ax.plot(x_guide, y_guide, color="red", lw=2)

curr = ax.scatter(traj[0][:,0], traj[0][:,1], c=colors, s= (r * 60)**2 * np.ones(balls.shape[0]))

for k in range(1, len(traj)) :

    # Remove and reprint particles
    curr.remove()
    curr = ax.scatter(traj[k][:,0], traj[k][:,1], c=colors, s= (r * 60)**2 * np.ones(balls.shape[0]))

    fig.canvas.flush_events()

