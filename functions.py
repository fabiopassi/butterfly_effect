""" This module contains all the functions for butterfly effect script """

# Importing modules
import numpy as np
from numba import njit


# Functions

@njit
def velocity_verlet (balls, dt) :
    """ This function upgrades positions and velocities of the particles using the velocity
        verlet algorithm. This function makes use of calculate_forces """

    v_dt_2 = balls[:,1,:] + 0.5 * balls[:,2,:] * dt                 # Update velocities pt.1
    balls[:,0,:] = balls[:,0,:] + v_dt_2 * dt                       # Update position
    balls[:,1,:] = v_dt_2 + 0.5 * balls[:,2,:] * dt                 # Update velocities pt.2
    
    return balls



@njit
def eval_contact_list(balls, R, r, skin) :

    contact_list = np.zeros(balls.shape[0])

    for i in range(balls.shape[0]) :
        # Distance from the center
        dist = np.sqrt(balls[i,0,0]*balls[i,0,0] + balls[i,0,1]*balls[i,0,1])
        # If the particle is closer than "skin" to the guide, then it must be considered for contacts
        if R - r - dist < skin :
            contact_list[i] = 1

    return contact_list



@njit
def check_rebound(balls, contact_list, r, R, g) :
    """ This function calculates the rebound with the circular guide """

    for i in range(balls.shape[0]) :
        # I consider only particles in the contact list
        if contact_list[i] > 0.5 :
            dist = np.sqrt(balls[i,0,0]*balls[i,0,0] + balls[i,0,1]*balls[i,0,1])
            # If the particle is closer than R to the guide, I must reflect it
            if dist + r > R :
                # I evaluate the versor perpendicular to the guide
                theta = np.arctan(balls[i,0,1]/balls[i,0,0])
                if theta > 0 :
                    versor = np.array([np.cos(theta), np.sin(theta)])
                else :
                    versor = (-1) * np.array([np.cos(theta), np.sin(theta)])
                # Correct position for excessive penetration in the guide
                penetration_length = dist + r - R
                balls[i,0,:] += 2 * penetration_length * versor
                # Reflect the velocity component along the radial direction (i.e. versor)
                v_perp = (balls[i,1,:] * versor).sum() * versor
                balls[i,1,:] -= 2 * v_perp

    return balls

