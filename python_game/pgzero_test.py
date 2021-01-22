
import pgzrun

WIDTH = 600
HEIGHT = 800

car = Actor("car.png")
car.pos = (100 , 200)


def draw():
    screen.clear()
    car.draw()

def update():
  if keyboard.right:
    car.x += 1
  elif keyboard.left:
   car.x -= 1

def update():
  move_car(car)

pgzrun.go() 

