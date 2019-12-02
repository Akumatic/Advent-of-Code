""" https://adventofcode.com/2018/day/13 """

def readFile(test1 = False, test2 = False):
    if test1:
        lines = [
            [ "/", "-",  ">", "-", "\\", " ", " ",  " ", " ",  " ", " ", " ",  " ",],
            [ "|", " ",  " ", " ",  "|", " ", " ",  "/", "-",  "-", "-", "-", "\\",],
            [ "|", " ",  "/", "-",  "+", "-", "-",  "+", "-", "\\", " ", " ",  "|",],
            [ "|", " ",  "|", " ",  "|", " ", " ",  "|", " ",  "v", " ", " ",  "|",],
            ["\\", "-",  "+", "-",  "/", " ", " ", "\\", "-",  "+", "-", "-",  "/",],
            [ " ", " ", "\\", "-",  "-", "-", "-",  "-", "-",  "/", " ", " ",  " ",]
        ]
    elif test2:
        lines = [
            [ "/", ">",  "-", "<", "\\", " ",  " "],
            [ "|", " ",  " ", " ",  "|", " ",  " "],
            [ "|", " ",  "/", "<",  "+", "-", "\\"],
            [ "|", " ",  "|", " ",  "|", " ",  "v"],
            ["\\", ">",  "+", "<",  "/", " ",  "|"],
            [ " ", " ",  "|", " ",  " ", " ",  "^"],
            [ " ", " ", "\\", "<",  "-", ">",  "/"]
        ]
    else:
        with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
            lines = [list(line[:-1]) for line in f.readlines()]
            
    carts = []
    
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] in [">", "<", "^", "v"]:
                cart = Cart(lines[y][x], x, y)
                lines[y][x] = cart
                carts.append(cart)

    return (lines, carts)

def showField(grid):
        return "\n".join([("".join(str(ch) for ch in line)) for line in grid])

class Cart:
    def __str__(self):
        return self.symbol

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.id = (y, x)
        self.intersectionCnt = 0
        self.alive = True

        if symbol == ">":
            self.dirx = 1
            self.diry = 0
            self.store = "-"
        elif symbol == "<":
            self.dirx = -1
            self.diry = 0
            self.store = "-"
        elif symbol == "^":
            self.dirx = 0
            self.diry = 1
            self.store = "|"
        else: # v
            self.dirx = 0
            self.diry = -1
            self.store = "|"

    def move(self):
        self.x += self.dirx
        self.y -= self.diry
        self.id = (self.y, self.x)

    def turnLeft(self):
        if self.dirx:
            self.dirx, self.diry = self.diry, self.dirx
        else:
            self.dirx, self.diry = -self.diry, self.dirx
        self.update()

    def turnRight(self):
        if self.diry:
            self.dirx, self.diry = self.diry, self.dirx
        else:
            self.dirx, self.diry = self.diry, -self.dirx
        self.update()

    def update(self):
        if self.dirx == 1:
            self.symbol = ">"
        elif self.dirx == -1:
            self.symbol = "<"
        elif self.diry == 1:
            self.symbol = "^"
        else: # self.diry == -1
            self.symbol = "v"

def part1(vals):
    carts = vals[1]

    while True:
        carts = sorted(carts, key=lambda x: x.id)
        for cart in carts:
            vals[0][cart.y][cart.x] = cart.store
            cart.move()
            cur = vals[0][cart.y][cart.x]
            if isinstance(cur, Cart):
                vals[0][cart.y][cart.x] = "X"
                return f"{cart.x},{cart.y}"
            
            cart.store = cur
            
            if cart.store == "\\":
                if cart.dirx:
                    cart.turnRight()
                else:
                    cart.turnLeft()
            elif cart.store == "/":
                if cart.dirx:
                    cart.turnLeft()
                else:
                    cart.turnRight()
            elif cart.store == "+":
                if cart.intersectionCnt == 0:
                    cart.turnLeft()
                    cart.intersectionCnt = 1
                elif cart.intersectionCnt == 1:
                    cart.intersectionCnt = 2
                else:
                    cart.turnRight()
                    cart.intersectionCnt = 0

            vals[0][cart.y][cart.x] = cart

def part2(vals):
    carts = vals[1]

    while len(carts) > 1:
        carts = sorted(carts, key = lambda x: x.id)
        cartCopy = carts.copy()
        for cart in carts:
            if not cart.alive:
                continue
            vals[0][cart.y][cart.x] = cart.store
            cart.move()
            cur = vals[0][cart.y][cart.x]
            if isinstance(cur, Cart):
                vals[0][cart.y][cart.x] = cur.store
                cur.alive = False
                cart.alive = False
                cartCopy.remove(cur)
                cartCopy.remove(cart)
                continue

            cart.store = cur
            
            if cart.store == "\\":
                if cart.dirx:
                    cart.turnRight()
                else:
                    cart.turnLeft()
            elif cart.store == "/":
                if cart.dirx:
                    cart.turnLeft()
                else:
                    cart.turnRight()
            elif cart.store == "+":
                if cart.intersectionCnt == 0:
                    cart.turnLeft()
                    cart.intersectionCnt = 1
                elif cart.intersectionCnt == 1:
                    cart.intersectionCnt = 2
                else:
                    cart.turnRight()
                    cart.intersectionCnt = 0

            vals[0][cart.y][cart.x] = cart
        carts = cartCopy
    
    return f"{carts[0].x},{carts[0].y}"

if __name__ == "__main__":
    vals = readFile(test1=False)
    print(f"Part 1: {part1(vals)}")
    vals = readFile(test2=False)
    print(f"Part 2: {part2(vals)}")