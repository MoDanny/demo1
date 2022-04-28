1
2
3

When comparing two files, diff finds sequences of lines common to both files, interspersed with groups of differing lines called hunks. Comparing two identical files yields one sequence of common lines and no hunks, because no lines differ. Comparing two entirely different files yields no common lines and one large hunk that contains all lines of both files. In general, there are many ways to match up lines between two given files. diff tries to minimize the total hunk size by finding large sequences of common lines interspersed with small hunks of differing lines. 


5
6
7
8
9
10

New Block
New Block

Stuff
Stuff
Stuff
