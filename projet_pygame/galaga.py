import pgzrun

WIDTH = 1200
HEIGHT = 1200


ship = Actor('ship')
ship.pos = (200 , 460)

def update():
  if keyboard.left:
    ship.x-=2
  elif keyboard.right:
    ship.x+=2


def draw():
  screen.clear()
  ship.draw()



pgzrun.go()
