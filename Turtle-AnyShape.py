import turtle

side =0
angle =0
side = int(input('Enter number of sides of polygon '))
angle = 360/side

turtle.color('Red')
turtle.speed(10000)
while (side > 0)  :
    turtle.backward(100)
    turtle.right(angle)
    side -= 1


