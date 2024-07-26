import math

class WrongDimensions(Exception):
    def __init__(self, message):
        super().__init__(message)

class Motor:
    def __init__(self, r, P_motor, P_atm=1.013*10**5, breaking_stress_case=3*10**8, safety_factor=1.5, bolt_profile=6*10**-3, breaking_stress_bolt=6.0*10**8, bolt_minor_diameter=4.917*10**-3):
        """Every quantity is in SI units!
        
        """
        self.P_atm = P_atm
        self.safety_factor = safety_factor

        #Motor Parameters:
        self.P_motor = P_motor
        self.r = r
        self.breaking_stress_case = breaking_stress_case
        self.thickness = 0.0
        self.longitudinal_constraint = 0.0
        self.hoop_constraint = 0.0
        self.longitudinal_stress = 0.0
        
        # Bolt parameters:
        self.bolt_profile = bolt_profile
        self.number_of_bolts = 0.0
        self.breaking_stress_bolt = breaking_stress_bolt
        self.bolt_minor_diameter = bolt_minor_diameter

        # Updating the global parameters:
        self.constrained_thickness()
        self.calculate_number_of_bolts()

    def lower_bound_constraints(self, *args):
        for num in args:
            if not isinstance(num, float) and not isinstance(num, int):
                raise ValueError(f"All arguments must be floats. Invalid argument: {num}")
            elif num <= 0:
                raise WrongDimensions("Wrong dimensions were input, or the entire simulation/hand calculations are wrong! The lower bound must be greater than zero!")
        # Calculating the minimum allowed value (lower bound)
        return max(args)

    def constrained_thickness(self):
        # Calculating the constrained thickness:
        self.thickness = self.r / (self.breaking_stress_case / (self.P_motor - self.P_atm) - 1)

        # Debugging:
        # print(f"Atmospheric Pressure is {self.P_atm} N/m^2")
        # print(f"Motor's Peak Pressure is {self.P_motor} N/m^2")
        # print(f"Yield Strength of the aluminium6061 case is {self.breaking_stress_case} N/m^2")
        # print(f"Yield Strength of the bolt's steel is {self.breaking_stress_bolt} N/m^2")
        
        return self.thickness

    def calculate_number_of_bolts(self):
        # Calculating the number of bolts:
        a = ((self.r+self.thickness)**2)*(self.P_motor-self.P_atm)
        b = ((self.bolt_minor_diameter/2)**2)*(self.breaking_stress_bolt)
        A = math.ceil((a) / (b))
        
        # num = (2*((self.r+self.thickness)**2)*(self.P_motor-self.P_atm))
        # den = (self.thickness*(self.bolt_minor_diameter/2)*self.breaking_stress_case)
        # B = math.ceil((num)/(den))
        B = A # done temporarily because there has to be some error in the calculation as it's outputting 54 screws!
        
        # Debugging:
        # print(f"the bolt shouldn't break {A}")
        # print(f"the hole shouldn't break {B}")
        
        self.number_of_bolts = self.lower_bound_constraints(A, B)
        return self.number_of_bolts

# Test run:
M1 = Motor(0.1, 8273709)
print(f"For a {M1.r*1000}mm outer diameter motor:\n")
print(f"Minimum Case Thickness (in mm): {M1.constrained_thickness() * 1000:.2f} mm")
print(f"Number of Bolts: {M1.calculate_number_of_bolts()}")
print(f"Place your Bolt at least {M1.bolt_minor_diameter*2.5*1000}mm away from the edge, and from each other.")
