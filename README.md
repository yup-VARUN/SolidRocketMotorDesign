# SolidRocketMotorDesign

- The file ProjectRock.ric is the OpenMotor File. It includes critical simulation values but not the entire simulation data.
### Open Motor Design:
<img width="1101" alt="image" src="https://github.com/user-attachments/assets/f8aad005-85ff-464d-8616-c96fb593d802">

- Internal Pressure Simulation:
<img width="822" alt="image" src="https://github.com/user-attachments/assets/7d0c0f03-4899-42ae-b5a4-44228dd83c28">

- The pressure peaks at around 360 psi, which in N/m^2 is $5.516*10^6 N/{m}^2 $. The atmospheric pressure is $1.013*10^5 N/{m}^2$.

# Thickness of the Cylinder:
- This creates stress in longitudinal and hoop direction on the motor which the case has to withstand. In no direction should the stress exceed the material's yield strength(maximum stress in the elastic region).
  - Hoop Stress is nearly twice(exactly two, if neglecting the thickness from calculations) as large as the longitudinal stress in all cylindrical pressure vessels.
  - ![image](image.png)

# Spacing and Number of Screws:
There could be different faliures in screws:
- One of them is when the bolt hole tear out from the edge of material. For not letting that happen it's emperically evident that we should place the bolts at least 1 bolt diameter away from any edge. For some materials this factor could also be 1.5 to 2 dimaters away from the edge.
<br>
Specifics could be seen in the following source:
![alt text](image-1.png)
- 
