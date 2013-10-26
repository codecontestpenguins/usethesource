#! /usr/bin/env python

"""

Sudoku Solver

"""
import sys
import re
import itertools
import copy
import random

inp = 'SampleInput.txt'
outp = 'TestOutput.txt'

class Cell():
    def __init__(self):
        self.poss = range(1,10)
        self.done = False
        self.val = None
    def elvals(self, vals):
        for v in vals:
            self.eliminate(v)
    def eliminate(self, v):
        if not self.done:
            if v in self.poss:
                self.poss.remove(v)
            if len(self.poss)==1:
                self.val = self.poss[0]
                self.done = True
    def setval(self, v):
        self.poss = None
        self.done = True
        self.val = v
    def check(self):
        if not self.done:
            if len(self.poss) == 1:
                self.val = self.poss[0]
                self.done = True
    def show(self):
        if self.done:
            return str(self.val)
        else:
            return 'x'

class Grid():
    def __init__(self):
        self.grid = [[Cell() for i in range(9)] for j in range(9)]
    
    def populate(self, mat):
        for row in range(9):
            ints = mat[row].split()
            for i in range(9):
                if ints[i] != 'x':
                    self.grid[row][i].setval(int(ints[i]))
    def show(self):
        out = ''
        for r in self.grid:
            for i in r:
                out = out + i.show() + ' '
            out += "\r\n"
        return out
    def elimrow(self, row, val):
        for c in self.grid[row]:
            c.eliminate(val)
    def elimcol(self, col, val):
        for i in range(9):
            self.grid[i][col].eliminate(val)
    def rcloop(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].done:
                    self.elimrow(r, self.grid[r][c].val)
                    self.elimcol(c, self.grid[r][c].val)
    def elbx(self, cols, rows):
        vals = []
        for r in rows:
            for c in cols:
                if self.grid[r][c].done:
                    vals.append(self.grid[r][c].val)
        for r in rows:
            for c in cols:
                self.grid[r][c].elvals(vals)

    def elimbox(self):
        cols = [[0,1,2],[3,4,5],[6,7,8]]
        rows = [[0,1,2],[3,4,5],[6,7,8]]
        for col in cols:
            for row in rows:
                self.elbx(col, row)
    def check(self):
        for r in range(9):
            for c in range(9):
                self.grid[r][c].check()
    def arewethereyet(self):
        for r in range(9):
            for c in range(9):
                b = self.grid[r][c]
                if not b.done:
                    return False
    def takeaguess(self):
        ro = [0,1,2,3,4,5,6,7,8,9] 
        co = [0,1,2,3,4,5,6,7,8,9]
        for r in random.shuffle(ro):
            for c in random.shuffle(co):
                b = self.grid[r][c]
                if len(b.poss) == 2:
                    b.setval(b.poss[random.randint(0,1)])

def main():
    f = open(inp, 'r')
    boards = f.read()
    separated = re.split("\r\n\r\n", boards)
    for s in separated:
        g = Grid()
        g.populate(re.split("\r\n", s))
        print g.show()
        for i in range(20):
            g.rcloop()
            g.check()
            g.elimbox()
            g.check()
        """
        if not g.arewethereyet(): # oh shit, time for guessing games
            h = copy.deepcopy(g)
            while not g.arewethereyet():
                g = copy.deepcopy(h)
                g.takeaguess()
                for i in range(20):
                    g.rcloop()
                    g.elimbox()
                    g.check()
        """
        print g.show()

if __name__ == "__main__":
    main()
