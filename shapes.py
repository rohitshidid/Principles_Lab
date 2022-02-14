from abc import ABC, abstractmethod
 
class shapes(ABC):
 
    @abstractmethod
    def area(self):
        pass
 
class Polygons(shapes):
    def area(self, side1 , side2 = 0):
        if side1 > 0 and side2 == 0 or (side1 == side2 and side1 > 0):
            print("I am A square.")
            area = side1*side1
            print("My area is {0} \n\n ".format(area))
        elif side1 == 0 :
            print("0 cannot be a value\n\n")

        if side2 != side1 and side2 > 0 :
            print("I am a rectangle")
            area = (side2*side1)/2
            print("My area is {0}\n\n".format(area))

        

class NonPolygons(shapes):
    def area(self, r1,r2=0):
        if (r1 == r2 and r1>0)or (r1>0 and r2 ==0) :
            print("I am a circle")
            area= 3.14*r1*r1
            print("My Area is {0}\n\n".format(area))
        elif r1==0:
            print(" 0 cannot be an value\n\n")

        if ((r1 > 0 and r2>0)and r2 != r1 ):
            print("I am a Elipse")
            area = 3.14*r1*r2
            print("My area is {0} \n\n".format(area))

        
        

 
p = Polygons()
np = NonPolygons()

p.area(0)
p.area(2)
p.area(3,3)
p.area(4,9)
np.area(0)
np.area(2)
np.area(3,3)
np.area(4,9)

