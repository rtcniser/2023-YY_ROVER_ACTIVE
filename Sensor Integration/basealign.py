import math

class alignbase:
    def __init__(self,x,z):
        self.x=x
        self.z=z

    # calculate angle from x and z coordinates
    def calculate_angle(self, x2, z2):
        dx = x2 - self.x
        dz = z2 - self.z
        return (math.atan2(dz, dx)) * (180 / math.pi)
    
    # Convert angle to the range [0, 360)
    def align_robot(self,target_x, target_z):
        angle = self.calculate_angle(target_x, target_z)
        angle = (angle + 360) % 360
        return angle
    
    # calculate the relative angle to be rotated from the current x and z coordinates
    def align_robot_arm(self,arm_x, arm_z):
        relative_angle = self.calculate_angle(arm_x, arm_z)
        return relative_angle

hello=alignbase(20,30)
print(hello.calculate_angle(-30,40))
print(hello.align_robot(-30,40))
print(hello.align_robot_arm(10,-30))

        
