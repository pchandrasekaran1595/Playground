UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Ant(object):
    def __init__(self, x, y, w, h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dir = UP
    
    def turnRight(self):
        self.dir += 1
        if (self.dir > LEFT):
            self.dir = UP
        
    def turnLeft(self):
        self.dir -= 1
        if (self.dir < UP):
            self.dir = LEFT
        
    def forward(self):
        if self.dir == UP:
            self.y -= 1
        elif self.dir == RIGHT:
            self.x += 1
        elif self.dir == DOWN: 
            self.y += 1
        elif self.dir == LEFT:
            self.x -= 1

        if self.x > self.w-1:
            self.x = 0
        elif self.x < 0:
            self.x = self.w-1
        if self.y > self.h-1:
            self.y = 0
        elif self.y < 0:
            self.y = self.h-1
    
    def update(self, image, animate=None):
        if not animate:
            for _ in range(11001):
                if image[self.y][self.x] == 255:
                    self.turnRight()
                    image[self.y][self.x] = 0
                elif image[self.y][self.x] == 0:
                    self.turnLeft()
                    image[self.y][self.x] = 255
                self.forward()
        else:
            if image[self.y][self.x] == 255:
                self.turnRight()
                image[self.y][self.x] = 0
            elif image[self.y][self.x] == 0:
                self.turnLeft()
                image[self.y][self.x] = 255
            self.forward()
        return image
