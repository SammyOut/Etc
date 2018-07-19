import copy


class Coil:
    def __init__(self, map_str='..........X........X...X....X.....XX.X..X..XX.X................', x=9, y=7):
        self.map_list = [[1 if a == '.' else 0 for a in map_str[i * x:(i + 1) * x]] for i in range(y)]
        self.map = copy.deepcopy(self.map_list)

        self.size_x = x
        self.size_y = y

        self.x = 0
        self.y = 0

    def up(self, check=False):
        x, y = self.x, self.y

        if y < 1 or not self.map[y - 1][x]:
            return False

        while check and y > 0 and self.map[y - 1][x]:
            self.map[y][x] = 0
            y -= 1

        self.y = y
        return True

    def down(self, check=False):
        x, y = self.x, self.y

        if y > self.size_y - 1 or not self.map[y + 1][x]:
            return False

        while check and y < self.size_y - 1 and self.map[y + 1][x]:
            self.map[y][x] = 0
            y -= 1

        self.y = y
        return True

    def left(self, check=False):
        x, y = self.x, self.y

        if x < 1 or not self.map[y][x - 1]:
            return False

        while check and x > 0 and self.map[y][x - 1]:
            self.map[y][x] = 0
            x -= 1

        self.x = x
        return True

    def right(self, check=False):
        x, y = self.x, self.y

        if x > self.size_x - 1 or not self.map[y][x + 1]:
            return False

        while check and x < self.size_x - 1 and self.map[y][x + 1]:
            self.map[y][x] = 0
            x -= 1

        self.x = x
        return True

    def check_way(self):
        self.up(check=True)
        self.down(check=True)
        self.left(check=True)
        self.right(check=True)

    def check_complete(self):
        return not any([any([a for a in b]) for b in self.map])

    def solve(self):
        for start_x in range(self.size_x):
            for start_y in range(self.size_y):
                if not self.map_list:
                    continue


Coil()
