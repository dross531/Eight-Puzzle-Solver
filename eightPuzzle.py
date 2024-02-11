start = (2, 4, 3,
         5, 8, 6,
         7, 1, 0)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def print_state(puzzle):
  for i in range(9):
    if i%3==0 and i>0:
      print("")
    print(str(puzzle[i])+" ", end = "")

def count_misplaced(state, goal):
  count = 0
  for i in range(9):
    if state[i]!=0 and state[i]!=goal[i]:
      count+=1
  return count

def next_moves(state):
  pos = int(state.index(0))
  if pos==0:
    return (1, 3)
  elif pos==1:
    return (0, 2, 4)
  elif pos==2:
    return (1, 5)
  elif pos==3:
    return (0, 4, 6)
  elif pos==4:
    return (1, 3, 5, 7)
  elif pos==5:
    return (2, 4, 8)
  elif pos==6:
    return (3, 7)
  elif pos==7:
    return (4, 6, 8)
  else:
    return (5, 7)

def move(state, pos):
  new_state = [tile for tile in state]
  new_state[state.index(0)] = state[pos]
  new_state[pos] = 0
  return tuple(new_state)