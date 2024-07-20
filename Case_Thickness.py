import math

class motor:
    def __init__(self, r, P_motor, P_atm=1.013*10**5, breaking_stress=3*10**8, safety_factor=1.5):
        # Every quanitity is in SI units!
        self.P_atm = P_atm
        self.P_motor = P_motor
        self.r = r
        self.safety_factor = safety_factor
        self.breaking_stress = breaking_stress
        self.thickness = 0.000
        self.longitudinal_constraint = 0.000
        self.hoop_constraint = 0.000

    def constrained_thickness(self):
        # Calculating the constrainted thickness:
        self.hoop_constraint = self.r/(self.breaking_stress/(self.P_motor-self.P_atm)-1)
        self.longitudinal_constraint = self.r*(math.sqrt((self.breaking_stress+self.P_motor)/(self.breaking_stress+self.P_atm))-1)

        if self.longitudinal_constraint > self.hoop_constraint:
            self.thickness = self.longitudinal_constraint
        else:
            self.thickness = self.hoop_constraint
        
        return self.thickness

# test run:    
M1 = motor(0.1, 5.516*10**6)
print(M1.constrained_thickness())

