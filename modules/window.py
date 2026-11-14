from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QLabel, QPushButton
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea 
from PyQt6.QtGui import QMouseEvent, QKeyEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.figures = []
        
        self.current_color = "red"

        self.current_size = 30

        self.WIDTH_WINDOW = 1024
        self.HEIGHT_WINDOW  = 800

        # получаем размеры экрана
        primary_screen = app.primaryScreen()
        screen_size = primary_screen.size()
        width_screen = screen_size.width()
        height_screen = screen_size.height()

        self.setGeometry(
            (width_screen // 2) - (self.WIDTH_WINDOW // 2), 
            (height_screen // 2) - (self.HEIGHT_WINDOW // 2), 
            self.WIDTH_WINDOW, 
            self.HEIGHT_WINDOW
        )
        
        self.setStyleSheet("background-color: white")

        
        self.main_frame = QFrame(parent=self)
        self.main_frame.setFixedSize(1024, 800)
        self.main_frame.setStyleSheet("background-color: white")

        
        self.stats_layout = QVBoxLayout(self.main_frame)
        self.stats_layout.setContentsMargins(20, 20, 20, 20)
        self.stats_layout.setSpacing(10)

        
        self.counter_label_size = self.create_counter_label(f"Размер: {self.current_size}")
        self.counter_label_colors = self.create_counter_label("Цвет: красный")
        self.counter_label_figures = self.create_counter_label("Фигур: 0")

        
        self.stats_layout.addWidget(self.counter_label_size)
        self.stats_layout.addWidget(self.counter_label_colors)
        self.stats_layout.addWidget(self.counter_label_figures)
        
        self.stats_layout.addStretch()

        
        

        
   
    def create_counter_label(self, default_text=""):
        label = QLabel(self.main_frame)
        label.setText(default_text)
        label.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        return label

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            frame_click = QFrame(parent=self.main_frame) 
            frame_click.setFixedSize(self.current_size, self.current_size)
            

            frame_click.setStyleSheet(f"background-color: {self.current_color}; border-radius: {self.current_size // 2}px; border: 2px solid black")
            frame_click.move(event.pos())
            frame_click.show()
            frame_click.raise_() 
            self.figures.append(frame_click)
            
            self.counter_label_size.setText(f"Размер: {self.current_size}")
            self.counter_label_figures.setText(f"Фигур: {len(self.figures)}")
            
        return super().mousePressEvent(event)

    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_C:
            for frame in self.figures:
                frame.deleteLater()
            self.figures.clear()
            self.counter_label_figures.setText("Всего фигур: 0")
        elif event.key() == Qt.Key.Key_1:
            self.current_color = "red"
            self.counter_label_colors.setText("Цвет: красный")

        elif event.key() == Qt.Key.Key_2:
            self.current_color = "green"
            self.counter_label_colors.setText("Цвет: зеленый")

        elif event.key() == Qt.Key.Key_3:
            self.current_color = "blue"
            self.counter_label_colors.setText("Цвет: синий")

        elif event.key() == Qt.Key.Key_Up:
            self.current_size += 2
            self.counter_label_size.setText(f"Размер: {self.current_size}")
            
        return super().keyPressEvent(event)
           

        

main_window = MainWindow()




    
    





    






    







