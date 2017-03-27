from pprint import *

class Grid:
    def __init__(self, fname, dictname):
        self.matrix = self.build_matrix(fname)
        self.words, self.prefixes = self.make_dict(dictname)
        self.foundwords = set()


    def make_dict(self, fname):
        """ Takes a filename (fname), and returns a set of words and prefixes to these words
        """
        words = set(x.strip() for x in open(fname))
        prefixes = set()
        for word in words:
            for i in range(len(word) + 1):
                prefixes.add(word[:i])

        return words, prefixes


    def build_matrix(self, fname):
        """ Takes a filename (fname), and returns a list of lists containing the contents
        """
        txt = open(fname).read()
        lines = txt.replace("\t", "")
        lines = lines.split("\n")
        space = []
        for i in range(len(lines)):
            temp = []
            for j in range(len(lines[i])):
                temp.append(lines[i][j])
            space.append(temp)

        return space


    def recursive_test(self, sequence, location, direction):
        """ Recursively searches the matrix for valid words
            starts at a root location, and advances in a specific direction
            continues until no valid prefix is found, or it reaches the end of the matrix
        """
        if sequence in self.prefixes:
            if sequence in self.words and len(sequence) > 3:
                print("Word found! root:", location, "word:", sequence)
                self.foundwords.add(sequence)
            next_tile = [location[0] + direction[0], location[1] + direction[1]]

            if self.isvalid(next_tile[0], next_tile[1]):
                newsequence = sequence
                newsequence += self.matrix[next_tile[0]][next_tile[1]]
                self.recursive_test(newsequence, next_tile, direction)
        else:
            return False


    def search(self):
        """ Calls the recursive testing function from every position in the matrix
        """

        n = [1, 0]
        s = [-1, 0]
        e = [0, 1]
        w = [0, -1]
        nw = [1, 1]
        ne = [1, -1]
        sw = [-1, 1]
        se = [-1, -1]

        directions = [n, s, e, w, nw, ne, sw, se]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for dir in directions:
                    self.recursive_test(self.matrix[i][j], [i, j], dir)


    def isvalid(self, x, y):
        """ Takes coordinates x and y, and checks that they are within the grid
        """
        if x >= len(self.matrix) or x < 0:
            return False
        if y >= len(self.matrix[0]) or y < 0:
            return False
        else:
            return True


def main(fname, dictname):
    """ Main function
        Takes a puzzle file (fname) and dictionary file (dictname)
        prints list of words in the puzzle matrix
    """
    grid = Grid(fname, dictname)
    pprint(grid.matrix)
    grid.search()
    print("Words found:", sorted(grid.foundwords))


if __name__=="__main__":
    main("butterfly.txt", "dictionary.txt")




