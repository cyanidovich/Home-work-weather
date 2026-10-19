from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QLabel, QPushButton
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea


main_window = QMainWindow()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW  = 800

# получаем обьект экрана
primary_screen = app.primaryScreen()
# получаем размеры экрана
screen_size = primary_screen.size()
# получаем ширину экрана
width_screen = screen_size.width()
# получаем высоту экрана
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

main_frame = QFrame(parent = main_window)
main_frame.setFixedSize(1024, 800)
main_frame.setStyleSheet("background-color: #696969	; border-radius: 15px")


state = {"count": 0}

main_layout = QVBoxLayout() 


label_count = QLabel(str(state["count"]))
label_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_count.setStyleSheet("font-size: 44px; font-weight: bold")


btn_minus = QPushButton("-")
btn_minus.setStyleSheet("background-color: #333333; color: white; border-radius: 8px; padding: 10px; font-weight: bold")

btn_reset = QPushButton("Reset")
btn_reset.setStyleSheet("background-color: #333333; color: white; border-radius: 8px; padding: 10px; font-weight: bold")

btn_plus = QPushButton("+")
btn_plus.setStyleSheet("background-color: #333333; color: white; border-radius: 8px; padding: 10px; font-weight: bold")

btn_plus.setFixedHeight(50)
btn_minus.setFixedHeight(50)
btn_reset.setFixedHeight(50)

buttons_layout = QVBoxLayout()
buttons_layout.addWidget(btn_plus)

buttons_layout.addWidget(btn_minus)
buttons_layout.addWidget(btn_reset)

main_layout.addWidget(label_count)
main_layout.addLayout(buttons_layout)
main_frame.setLayout(main_layout)



def button_plus():
    state["count"] += 1
    label_count.setText(str(state["count"]))

def button_minus():
    state["count"] -= 1
    label_count.setText(str(state["count"]))

def button_reset():
    state["count"] = 0
    label_count.setText(str(state["count"]))

btn_plus.clicked.connect(button_plus)
btn_minus.clicked.connect(button_minus)
btn_reset.clicked.connect(button_reset)        







