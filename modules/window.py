from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QLabel, QPushButton
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout
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
main_frame.setStyleSheet("background-color: #0F172A; border-radius: 15px")


grid_layout = QGridLayout(main_frame)
grid_layout.setContentsMargins(24, 24, 24, 24) 
grid_layout.setHorizontalSpacing(16)           
grid_layout.setVerticalSpacing(16)


cards = []

for frame in range(9):
    row = frame // 3 
    col = frame % 3
    card_frame = QFrame()
    card_frame.setFixedHeight(210)
    card_frame.setStyleSheet("background-color: #1E293B; border-radius: 14px;")
    grid_layout.addWidget(card_frame, row, col)

    cards.append(card_frame)


card_content_1 = cards[0]
card_content_1.setStyleSheet("background-color: #FF4500; border-radius: 14px;")
card_layout = QVBoxLayout(card_content_1)
card_layout.setContentsMargins(20, 20, 20, 20)

text_label = QLabel("Температура")
text_label.setStyleSheet("color: white; font-size: 16px;")
card_layout.addWidget(text_label)


card_layout.addStretch()

val_label = QLabel("24°C")
val_label.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout.addWidget(val_label)

val_label = QLabel("Сонячно")
val_label.setStyleSheet("color: white; font-size: 16px;")
card_layout.addWidget(val_label)





card_content_2 = cards[1]
card_content_2.setStyleSheet("background-color: #007BFF; border-radius: 14px;")
card_layout_1 = QVBoxLayout(card_content_2)
card_layout_1.setContentsMargins(20, 20, 20, 20)

text_label_1 = QLabel("Вологість")
text_label_1.setStyleSheet("color: white; font-size: 16px;")
card_layout_1.addWidget(text_label_1)


card_layout_1.addStretch()

val_label_1 = QLabel("65%")
val_label_1.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout_1.addWidget(val_label_1)

val_label_1 = QLabel("Комфортно")
val_label_1.setStyleSheet("color: white; font-size: 16px;")
card_layout_1.addWidget(val_label_1)



card_content_3 = cards[2]
card_content_3.setStyleSheet("background-color: #7C4DFF; border-radius: 14px;")
card_layout_2 = QVBoxLayout(card_content_3)
card_layout_2.setContentsMargins(20, 20, 20, 20)

text_label_2 = QLabel("Швидкість вітру")
text_label_2.setStyleSheet("color: white; font-size: 16px;")
card_layout_2.addWidget(text_label_2)

card_layout_2.addStretch()

val_label_2 = QLabel("12 км/год")
val_label_2.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout_2.addWidget(val_label_2)

val_label_2 = QLabel("Слабкий вiтер")
val_label_2.setStyleSheet("color: white; font-size: 16px;")
card_layout_2.addWidget(val_label_2)







card_content_4 = cards[3]
card_content_4.setStyleSheet("background-color: #E91E63; border-radius: 14px;")
card_layout_3 = QVBoxLayout(card_content_4)
card_layout_3.setContentsMargins(20, 20, 20, 20)

text_label_3 = QLabel("Відчувається як")
text_label_3.setStyleSheet("color: white; font-size: 16px;")
card_layout_3.addWidget(text_label_3)

card_layout_3.addStretch()

val_label_3 = QLabel("27°C")
val_label_3.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout_3.addWidget(val_label_3)

val_label_3 = QLabel("Теплiше, нiж зазвичай")
val_label_3.setStyleSheet("color: white; font-size: 16px;")
card_layout_3.addWidget(val_label_3)





card_content_5 = cards[4]
card_content_5.setStyleSheet("background-color: #00838F; border-radius: 14px;")
card_layout_4 = QVBoxLayout(card_content_5)
card_layout_4.setContentsMargins(20, 20, 20, 20)

text_label_4 = QLabel("Атмосферний тиск")
text_label_4.setStyleSheet("color: white; font-size: 16px;")
card_layout_4.addWidget(text_label_4)

card_layout_4.addStretch()

val_label_4 = QLabel("760")
val_label_4.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout_4.addWidget(val_label_4)

val_label_4 = QLabel("мм рт. ст.")
val_label_4.setStyleSheet("color: white; font-size: 16px;")
card_layout_4.addWidget(val_label_4)





card_content_6 = cards[5]
card_content_6.setStyleSheet("background-color: #00A86B; border-radius: 14px;")
card_layout_5 = QVBoxLayout(card_content_6)
card_layout_5.setContentsMargins(20, 20, 20, 20)

text_label_5 = QLabel("Ймовірність дощу")
text_label_5.setStyleSheet("color: white; font-size: 16px;")
card_layout_5.addWidget(text_label_5)

card_layout_5.addStretch()

val_label_5 = QLabel("20%")
val_label_5.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout_5.addWidget(val_label_5)

val_label_5 = QLabel("Невелика")
val_label_5.setStyleSheet("color: white; font-size: 16px;")
card_layout_5.addWidget(val_label_5)






card_content_7 = cards[6]
card_content_7.setStyleSheet("background-color: #1E293B; border-radius: 14px;")
card_layout_6 = QVBoxLayout(card_content_7)
card_layout_6.setContentsMargins(20, 20, 20, 20)
card_layout_6.addStretch()
text_label_6 = QLabel("Керування погодою")
text_label_6.setStyleSheet("color: white; font-size: 20px;")
card_layout_6.addWidget(text_label_6)


text_label_6.setAlignment(Qt.AlignmentFlag.AlignHCenter)
card_layout_6.addStretch()

btn_update = QPushButton("Оновити")
btn_update.setFixedHeight(40)
btn_update.setStyleSheet("background-color: #5865F2; color: white;border-radius: 10px; font-weight: bold; border: none;")

card_layout_6.addWidget(btn_update)



card_content_8 = cards[7]
card_content_8.setStyleSheet("background-color: #2D3748; border-radius: 14px;")
card_layout_7 = QVBoxLayout(card_content_8)
card_layout_7.setContentsMargins(20, 20, 20, 20)
text_label_7 = QLabel("Мiсто")
text_label_7.setStyleSheet("color: white; font-size: 20px;")
card_layout_7.addWidget(text_label_7)

card_layout_7.addStretch()


val_label_7 = QLabel("Днiпро")
val_label_7.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
card_layout_7.addWidget(val_label_7)

val_label_7 = QLabel("Україна")
val_label_7.setStyleSheet("color: white; font-size: 16px;")
card_layout_7.addWidget(val_label_7)








card_content_9 = cards[8]
card_content_9.setStyleSheet("background-color: #1E293B; border-radius: 14px;")
card_layout_8 = QVBoxLayout(card_content_9)
card_layout_8.setContentsMargins(20, 20, 20, 20)
card_layout_8.addStretch()
text_label_8 = QLabel("Стан погоди")
text_label_8.setStyleSheet("color: white; font-size: 20px;")
card_layout_8.addWidget(text_label_8)


text_label_8.setAlignment(Qt.AlignmentFlag.AlignHCenter)
card_layout_8.addStretch()

btn_change_color = QPushButton("Змiнити колiр")
btn_change_color.setFixedHeight(40)
btn_change_color.setStyleSheet("background-color: #00C853; color: white;border-radius: 10px; font-weight: bold; border: none;")

card_layout_8.addWidget(btn_change_color)


