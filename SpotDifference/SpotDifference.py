from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("틀린그림찾기", "images/problem.png")

problem = Object("images/problem.png")
problem.locate(scene, 0, 0)
problem.show()

check1_left = Object("images/check.png")
check1_left.locate(scene, 568 - 25, 594 - 25)

check1_right = Object("images/check.png")
check1_right.locate(scene, 1186 - 25, 594 - 25)

def checkIn(x, y, cx, cy, r):
    return cx - r < x < cx + r and cy - r < y < cy + r

def problem_onMouseAction(x, y, action):
    if checkIn(x, y, 568, 594, 54) or checkIn(x, y, 1186, 594, 54):
        check1_left.show()
        check1_right.show()
    
    else:
        endGame()
problem.onMouseAction = problem_onMouseAction

showMessage("좌우에 틀린 곳을 찾아보세요.")
startGame(scene)
