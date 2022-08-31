import sys


def part1(raw: str) -> int:
    """
    --- Day 3: Perfectly Spherical Houses in a Vacuum ---
    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls
    him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v),
    east (>), or west (<). After each move, he delivers another present to the house at his new location.

    However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
    and Santa ends up visiting some houses more than once. How many houses receive at least one present?

    For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

    :param raw:
    :return:
    """
    def calc(raw: str) -> int:
        visited = {"00"}
        coord = [0, 0]
        mapping = {'^': [0, 1], 'v': [0, -1], '>': [1, 0], '<': [-1, 0]}
        for each in raw:
            coord = [x + y for x, y in zip(coord, mapping[each])]
            visited.add(f"{coord[0]}{coord[1]}")
        return len(visited)

    count = 0
    for each in raw:
        count += calc(each.strip())
    print(f"{raw} {count}")
    return count



# TODO does not work, result too high. Need to start from scratch based on part 1
#
def part2(raw: str) -> int:
    def calc(raw: str) -> int:
        visited = {"00"}
        coord = [[0, 0], [0, 0]]
        mapping = {'^': [0, 1], 'v': [0, -1], '>': [1, 0], '<': [-1, 0]}
        for index, each in enumerate(raw):
            print(f"{each} {visited}")
            if index % 2:
                coord[0] = [x + y for x, y in zip(coord[0], mapping[each])]
                visited.add(f"{coord[0][0]}{coord[0][1]}")
            else:
                coord[1] = [x + y for x, y in zip(coord[1], mapping[each])]
                visited.add(f"{coord[1][0]}{coord[1][1]}")
        return len(visited)

    count = 0
    for each in raw:
        count += calc(each.strip())
    print(count)
    return count -1

def test():
    # assert part1('>') == 2
    # assert part1('^>v<') == 4
    # assert part1('^v^v^v^v^v') == 2
    assert part2('^v') == 3
    assert part2('^>v<') == 3
    assert part2('^v^v^v^v^v') == 11

# print(part1(sys.stdin.readlines()))
# print(part2(sys.stdin.readlines()))
test()