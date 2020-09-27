from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("틀린그림찾기", "images/problem.png")

problem = Object("images/problem.png")
problem.locate(scene, 0, 0)
problem.show()

class Rect:
    def __init__(self, cx, cy, r):
        self.centerX = cx
        self.centerY = cy
        self.radius = r

    def checkIn(self, x, y):
        return self.centerX - self.radius < x < self.centerX + self.radius and self.centerY - self.radius < y < self.centerY + self.radius

check_margin = 25
class DifferencePoint:
    def __init__(self, lcx, rcx, cy, r):
        self.left_rect = Rect(lcx, cy, r)
        self.right_rect = Rect(rcx, cy, r)
        self.left_check = Object("images/check.png")
        self.left_check.locate(scene, lcx - check_margin, cy - check_margin)
        self.right_check = Object("images/check.png")
        self.right_check.locate(scene, rcx - check_margin, cy - check_margin)

    def checkIn(self, x, y):
        return self.left_rect.checkIn(x, y) or self.right_rect.checkIn(x, y)

    def show(self):
        self.left_check.show()
        self.right_check.show()

# 첫번째 틀린 위치 (568, 594), (1186, 594) - 54
point1 = DifferencePoint(568, 1186, 594, 54)

#rect1_left = Rect(568, 594, 54)
#rect1_right = Rect(1186, 594, 54)

#check1_left = Object("images/check.png")
#check1_left.locate(scene, rect1_left.centerX - check_margin, rect1_left.centerY - check_margin)

#check1_right = Object("images/check.png")
#check1_right.locate(scene, rect1_right.centerX - check_margin, rect1_right.centerY - check_margin)

#def checkIn(x, y, cx, cy, r):
#    return cx - r < x < cx + r and cy - r < y < cy + r

def problem_onMouseAction(x, y, action):
    #if rect1_left.checkIn(x, y) or rect1_right.checkIn(x, y):
    #    check1_left.show()
    #    check1_right.show()
    if point1.checkIn(x, y):
        point1.show()

    else:
        endGame()
problem.onMouseAction = problem_onMouseAction

showMessage("좌우에 틀린 곳을 찾아보세요.")
startGame(scene)
