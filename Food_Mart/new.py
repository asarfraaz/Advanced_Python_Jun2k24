'''
'''

def main(args):
    x = 10

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == "__main__":
    import sys
    main(sys.argv)
