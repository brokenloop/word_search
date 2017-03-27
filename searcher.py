from pprint import *

class Grid:
    def __init__(self, fname, dictname):
        self.searchspace = self.build_space(fname)
        self.words, self.prefixes = self.make_dict(dictname)
        self.foundwords = set()


    def make_dict(self, fname):
        words = set(x.strip() for x in open(fname))
        prefixes = set()
        for word in words:
            for i in range(len(word)):
                prefixes.add(word[:i])

        return words, prefixes


    def build_space(self, fname):
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


    def recursive_test(self, sequence, location):
        if sequence in self.prefixes:
            if sequence in self.words and len(sequence) > 3:
                self.foundwords.add(sequence)
            north = [location[0], location[1] + 1]
            south = [location[0], location[1] - 1]
            east = [location[0] + 1, location[1]]
            west = [location[0] - 1, location[1]]

            directions = [north, south, east, west]

            for dir in directions:
                if self.isvalid(dir[0], dir[1]):
                    newsequence = sequence
                    newsequence += self.searchspace[dir[0]][dir[1]]
                    self.recursive_test(newsequence, dir)
            return False

        else:
            return False


    def search(self):
        for i in range(len(self.searchspace)):
            for j in range(len(self.searchspace[i])):
                self.recursive_test(self.searchspace[i][j], [i, j])


    def isvalid(self, x, y):
        if x >= len(self.searchspace[0]) or x < 0:
            return False
        if y >= len(self.searchspace[0]) or y < 0:
            return False
        else:
            return True







if __name__=="__main__":

    grid = Grid("test.txt", "dictionary.txt")
    print(grid.searchspace)
    grid.search()
    print(grid.foundwords)


