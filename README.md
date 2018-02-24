# N-queens-problem
Solving the N-queen or N-rooks problem using BFS and DFS


# How to Run 
```
python nqueen/nrook board_size row col
```
where row, col represents the place in board where you don't want to put queen or rook
Value 0 for row and col represent the default case where you don't care about keeping 
the row and column free. For example:
```
python nqueen.py  nqueen 8 0 0
```
Either unavailable row or col as input is zero. Treating this as a (0,0) case
Starting from initial board:
```
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
```

Looking for solution...
```
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ Q _ _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ _ Q
```

```
python nqueen.py  nqueen 8 1 1
```
Starting from initial board:
```
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
```
Looking for solution...
```
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _
_ _ Q _ _ _ _ _
X _ _ _ Q _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
```
