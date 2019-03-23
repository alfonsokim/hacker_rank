

class Interval():

    def __init__(self, start, end):
        if start > end:
            raise Exception('Invalid [%i, %i) ' % (start, end))
        self.start = start
        self.end = end

    def extend(self, other):
        lower = (self.start <= other.start and self.end >= other.start) or (other.start <= self.start and other.end >= self.start)
        upper = (self.end <= other.end and self.start >= other.end) or (other.end <= self.end and other.start >= self.end)
        if lower or upper:
            return Interval(min(self.start, other.start), max(self.end, other.end))
        else:
            return None

    def __str__(self):
        return '[%i, %i)' % (self.start, self.end)


def intervals(I1, I2):
    interval0 = Interval(30, 40)
    interval1 = Interval(1, 50)
    print interval0, interval1
    extended = interval0.extend(interval1)


if __name__ == '__main__':
    print intervals(
        [(2, 4), (6, 8), (1, 3)], 
        [(7, 9), (2, 5)]
    )
