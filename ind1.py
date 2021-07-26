import math
print("Координаты четырехугольника:")
Ax = int(input("Ax= "))
Ay = int(input("Ay= "))
Bx = int(input("Bx= "))
By = int(input("By= "))
Cx = int(input("Cx= "))
Cy = int(input("Cy= "))
Dx = int(input("Dx= "))
Dy = int(input("Dy= "))
s1 = math.fabs((Bx-Ax)*(Cy-Ay)-(Cx-Ax)*(By-Ay))/2
s2 = math.fabs((Dx-Ax)*(Cy-Ay)-(Cx-Ax)*(Dy-Ay))/2
print("s= ", s1+s2)
