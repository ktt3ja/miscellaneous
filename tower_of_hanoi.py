# Tower of Hanoi solver
#
# Sample output:
# solve(5)
#    1 to 3
#    1 to 2
#    3 to 2
#    1 to 3
#    2 to 1
#    2 to 3
#    1 to 3
#    1 to 2
#    3 to 2
#    3 to 1
#    2 to 1
#    3 to 2
#    1 to 3
#    1 to 2
#    3 to 2
#    1 to 3
#    2 to 1
#    2 to 3
#    1 to 3
#    2 to 1
#    3 to 2
#    3 to 1
#    2 to 1
#    2 to 3
#    1 to 3
#    1 to 2
#    3 to 2
#    1 to 3
#    2 to 1
#    2 to 3
#    1 to 3

class Tower(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.ident = None

def solve(n):
    def solve(source, other, dest, length):
        if length == 0: return
        solve(source, dest, other, length-1)
        dest.append(source.pop())
        print('%d to %d' % (source.ident, dest.ident))
        solve(other, source, dest, length-1)

    source, other, dest = map(Tower, [list(range(n,0,-1)), [], []])
    source.ident, other.ident, dest.ident = 1, 2, 3
    solve(source, other, dest, len(source))

if __name__ == '__main__':
    solve(5)
