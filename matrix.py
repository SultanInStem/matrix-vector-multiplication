import math
class Matrix: 
    def __init__(self, start_t, end_t, dt): 
        self.start_t = start_t 
        self.end_t = end_t 
        self.t = start_t
        self.dt = dt




class RotationMatrix(Matrix): 
    def __init__(self,start_t, end_t, dt): 
        super().__init__(start_t, end_t, dt)
        self.A = [ 
            [math.cos(self.t), -math.sin(self.t)], 
            [math.sin(self.t), math.cos(self.t)]    
        ]
    def update(self): 
        print(self.t)
        if self.t >= self.end_t: return
        self.t += self.dt 
        self.A = [
            [math.cos(self.t), -math.sin(self.t)], 
            [math.sin(self.t), math.cos(self.t)]  
        ]

    def get_matrix(self): 
        return self.A
    

class ShearMatrix(Matrix): 
    def __init__(self, start_t, end_t, dt):
        super().__init__(start_t, end_t, dt)
        self.A = [
            [1, self.t], 
            [0, 1]
        ]
    def update(self): 
        if self.t >= self.end_t: return 
        self.t += self.dt
        self.A = [
            [1, self.t], 
            [0, 1]
        ]

    def get_matrix(self): 
        return self.A

    
        