class User:

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, num):
        if num == 0 or num < -8 or num > 8:
            raise Exception('Invalid rank')

        if num == self.rank and self.rank < 8:
            self.progress += 3

        elif self.rank == 1 and num == -1:
            self.progress += 1

        elif self.rank - 1 == num and self.rank < 8:
            self.progress += 1

        elif num > self.rank and self.rank < 8:

            d = len(range(self.rank, num))

            if self.rank < 0 < num:
                d -= 1

            product = 10 * d * d
            self.progress += product

        while self.progress >= 100 and self.rank <= 8:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank = 1
            elif self.rank == 8:
                self.progress = 0
                break

