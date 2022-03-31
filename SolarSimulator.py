import turtle
import random

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        output = ("<" + str(self.x) + "," + str(self.y) + ">")
        return output

    def get_values(self):
        pair = [self.x,self.y]
        return pair

    def set_values(self, pair):
        self.x = pair[0]
        self.y = pair[1]

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_vector = Vec2(new_x, new_y)
        return new_vector

    def __mul__(self, other):
        new_x = self.x * other
        new_y = self.y * other
        new_vector = Vec2(new_x, new_y)
        return new_vector

    def __truediv__(self, other):
        new_x = self.x / other
        new_y = self.y / other
        new_vector = Vec2(new_x, new_y)
        return new_vector

class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.Maturin = turtle.Turtle()
        background = turtle.getscreen()
        background.bgcolor("black")
        background.colormode(255)
        self.Maturin.shape("circle")
        self.Maturin.resizemode("user")
        self.Maturin.turtlesize(mass/2, mass/2)
        self.Maturin.pencolor(random.randint(1,255), random.randint(1,255), random.randint(1,255)) #random color, display size based on mass of object
        self.Maturin.speed(0)
        self.Maturin.penup()
        self.move()
        self.Maturin.pendown()

    def __str__(self):
        output = ("mass: " + str(self.mass) + ", pos: <" + str(self.position.x) + "," + str(self.position.y) + ">, vel:<" + str(self.velocity.x) + "," + str(self.velocity.y) + ">")
        return output

    def move(self):
        turtle.tracer(0,0)
        self.Maturin.setpos(self.position.x, self.position.y)

    def accelerate(self, a, t):
        self.position += self.velocity * t
        self.position += (a * 0.5 * (t**2))
        self.velocity += a * t
        self.move()

    def __eq__(self, other):
        same = False
        if (self.mass == other.mass) & (self.velocity == other.velocity):
            same = True
        return same

    def sum_of_forces(self, objects): #Gravity constant =4
        final = Vec2(0,0)
        for i in range(len(objects)):
            if objects[i] != self:
                force = ((4 * self.mass * objects[i].mass) / (((objects[i].position.x - self.position.x)**2 + (objects[i].position.y - self.position.y)**2)**0.5))
                direction = Vec2(objects[i].position.x - self.position.x, objects[i].position.y - self.position.y)
                direction *= force
                direction /= self.mass
                final += direction

        return final



particle_list = []
for i in range(10): #10 planets, planets' masses from 1-5, placed from (-400,400) to (400,400), with initial velocities from (-50,-50) to (50,50)
    particle_list.append(Particle(random.randint(1,5), Vec2(random.randint(-400, 400), random.randint(-400, 400)), Vec2(random.randint(-50, 50), random.randint(-50, 50))))

for j in range(500): #controls length of simulation
    for i in range(len(particle_list)):
        particle_list[i].accelerate(particle_list[i].sum_of_forces(particle_list), 0.1) #controls speed of simulation
        turtle.update()