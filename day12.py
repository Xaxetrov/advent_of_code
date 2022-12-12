from collections import defaultdict
import heapq
import os
from sys import maxsize as infinity


class Tile:
    def __init__(self, row, column, height) -> None:
        self.row, self.column = row, column
        self.height = height

    def __lt__(self, other):
        return self.height > other.height

    def __le__(self, other):
        return self.height >= other.height


def read_input(filename: str) -> 'tuple[list[list[Tile]], Tile, Tile]':
    tiles = []
    
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        for row, line in enumerate(f.read().splitlines()):
            tile_row = []
            for column, char in enumerate(line):
                if char == 'S':
                    start_tile = Tile(row, column, 1)
                    tile_row.append(start_tile)
                elif char == 'E':
                    end_tile = Tile(row, column, 26)
                    tile_row.append(end_tile)
                else:
                    tile_row.append(Tile(row, column, ord(char) - 96))
            tiles.append(tile_row)
    return tiles, start_tile, end_tile


def heuristic_score(tile: Tile, end_tile: Tile):
    return abs(tile.row - end_tile.row) + abs(tile.column - end_tile.column)


neighbor_couples = ((-1, 0), (1, 0), (0, -1), (0, 1))
def find_neighbors(tiles: 'list[list[Tile]]', tile: Tile) -> 'list[Tile]':
    neighbors = []
    for couple in neighbor_couples:
        if (0 <= tile.row + couple[0] < len(tiles) and
            0 <= tile.column + couple[1] < len(tiles[0]) and
            tiles[tile.row + couple[0]][tile.column + couple[1]].height <= tile.height + 1):
            neighbors.append(tiles[tile.row + couple[0]][tile.column + couple[1]])
    return neighbors


def a_star(tiles: 'list[list[Tile]]', start_tile: Tile, end_tile: Tile):
    to_explore = [(heuristic_score(start_tile, end_tile), start_tile)]
    explored = []
    score_from_start = defaultdict(lambda: infinity)
    score_from_start[start_tile] = 0

    while to_explore:
        current_score, current_tile = heapq.heappop(to_explore)

        if current_tile == end_tile:
            return current_score

        for neighbor in find_neighbors(tiles, current_tile):
            
            tentative_score_from_start = score_from_start[current_tile] + 1
            if tentative_score_from_start < score_from_start[neighbor]:
                score_from_start[neighbor] = tentative_score_from_start
                
                neighbor_score = tentative_score_from_start + heuristic_score(neighbor, end_tile)
                if (neighbor_score, neighbor) not in to_explore:
                    heapq.heappush(to_explore, (neighbor_score, neighbor))

    return infinity


if __name__ == '__main__':
    tiles, start_tile, end_tile = read_input('day12.txt')

    #Part 1
    print(a_star(tiles, start_tile, end_tile))

    # Part 2
    start_tiles = [tile for row in tiles for tile in row if tile.height == 1]
    # Definitely not optimal (still OK, 12s for 6000 tiles), A simpler BFS from the end would be better.
    # Did not do it because I used A* for the first part and did not want to spend time generalizing it or use another algorithm instead.
    print(min(a_star(tiles, start_tile_candidate, end_tile) for start_tile_candidate in start_tiles))