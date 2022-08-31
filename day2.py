import sys


def part1(raw: list) -> int:
    """
    The elves are running low on wrapping paper, and so they need to submit an order for more.
    They have a list of the dimensions (length l, width w, and height h) of each present,
    and only want to order exactly as much as they need.

    Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
    wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    The elves also need a little extra paper for each present: the area of the smallest side.

    For example:

        A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square
        feet of slack, for a total of 58 square feet.
        A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square
        foot of slack, for a total of 43 square feet.

    All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
    :param raw:
    :return:
    """
    def calc(a: int, b: int, c: int) -> int:
        x, y, z = a * b, b * c, c * a
        slack = min([x, y, z])
        area = 2 * sum([x, y, z])
        return slack + area

    result = 0
    for each in raw:
        each = each.strip().split('x')
        if '' not in each:
            each = list(map(int, each))
            result += calc(*each)
    return result


def part2(raw: list) -> int:
    """
    The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the
    length they need to order, which they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any
    one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect
    bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

    For example:

        A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet
        of ribbon for the bow, for a total of 34 feet.
        A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet
        of ribbon for the bow, for a total of 14 feet.

    How many total feet of ribbon should they order?
    :param raw:
    :return:
    """
    def calc(a: int, b: int, c: int) -> int:
        return (2 * (a + b)) + (a * b * c)

    result = 0
    for each in raw:
        each = each.strip().split('x')
        if '' not in each:
            each = sorted(list(map(int, each)))
            result += calc(*each)
    return result



def p1(r,c=lambda a,b,c:min([a*b,b*c,c*a])+2*sum([a*b,b*c,c*a])):
    return sum([c(*e)if''not in e else 0for e in[list(map(int,_.strip().split('x')))for _ in r]])


def p2(r,c=lambda a,b,c:2*(a+b)+a*b*c):
    return sum([c(*e)if''not in e else 0for e in sorted([int(_.strip().split('x'))for _ in r])])


def test():
    assert part1(['2x3x4']) == 58
    assert part1(['1x1x10']) == 43
    assert p1(['2x3x4']) == 58
    assert p1(['1x1x10']) == 43
    assert part2(['2x3x4']) == 34
    assert part2(['4x2x3']) == 34
    assert part2(['1x1x10']) == 14
    print("Passed!")


# print(part1(sys.stdin.readlines()))
# print(part2(sys.stdin.readlines()))
test()
