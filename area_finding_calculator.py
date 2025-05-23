# Area Calculator Code

find_area = input("Enter your need to find area of (rectangle, triangle, circle, square): ").lower()

if (find_area == "rectangle"):
# Area of Rectangle
  length = float(input("Enter length of rectangle in meters: "))
  width  = float(input("Enter width of rectangle in meters: "))
  area = length*width
  round_area = round(area,3)
  print("Area of rectangle: ",round_area,"m²")

elif (find_area == "triangle"):
# Area of Triangle
  height = float(input("Enter height of triangle in meters: "))
  base  = float(input("Enter base of triangle in meters: "))
  area = 0.5*base*height
  round_area = round(area,3)
  print("Area of triangle: ",round_area,"m²")

elif (find_area == "circle"):
  radius = float(input("Enter radius of circle in meters: "))
  area = 3.142*(pow(radius,2))
  round_area = round(area,3)
  print("Area of circle: ",round_area,"m²")

elif (find_area == "square"):
  side = float(input("Enter side of square in meters: "))
  area = pow(side,2)
  round_area = round(area,3)
  print("Area of square: ",round_area,"m²")

else:
  print("Something went wrong try it again. Check shape you enter!!!")
