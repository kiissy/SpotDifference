from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

Scene("틀린그림찾기", "images/problem.png")

problem = Object("images/problem.png")
problem.locate(scene, 0, 0)
problem.show()

def problem_onMouseAction(x, y, action):
    endGame()
problem.onMouseAction = problem_onMouseAction

showMessage("좌우에 틀린 곳을 찾아보세요.")
startGame(scene)
