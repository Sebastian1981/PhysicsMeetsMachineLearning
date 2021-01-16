import math
import numpy as np

class MassPoint:
    def __init__(self, h, v_ab, alpha_deg):
        # initialize starting values
        self.h         = h
        self.v_ab      = v_ab
        self.alpha_deg = alpha_deg
        self.alpha_rad = math.radians(self.alpha_deg)
        self.r0        = np.array([0, self.h])
        self.v0        = np.array([self.v_ab*math.cos(self.alpha_rad), self.v_ab*math.sin(self.alpha_rad)])
        
class PhysicsModel(MassPoint):
    def __init__(self, h, v_ab, alpha_deg, g):
        MassPoint.__init__(self, h, v_ab, alpha_deg)
        self.g = g
        self.a = np.array([0, -self.g])
        
    def time_mp_hits_earth(self):
        t_e = self.v0[1] / self.g + math.sqrt((self.v0[1]/self.g)**2 + 2*self.r0[1]/self.g)
        return t_e
    
    def make_time_points(self, starting_time, stop_time, number_points):
        time_points = np.linspace(starting_time, stop_time, number_points).reshape(-1,1)
        return time_points
    
    def get_spacetime_vector_of_throw(self, time_points):
        r = self.r0 + self.v0*time_points + 0.5*self.a*time_points**2
        return r