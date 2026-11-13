from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QLabel, QPushButton
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea 
from PyQt6.QtGui import QMouseEvent, QKeyEvent











class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.my_frames = []
       
        
        
        

        self.WIDTH_WINDOW = 1024
        self.HEIGHT_WINDOW  = 800

        # получаем обьект экрана
        primary_screen = app.primaryScreen()
        # получаем размеры экрана
        screen_size = primary_screen.size()
        # получаем ширину экрана
        width_screen = screen_size.width()
        # получаем высоту экрана
        height_screen = screen_size.height()


        self.setGeometry(
        (width_screen // 2) - (self.WIDTH_WINDOW // 2), 
        (height_screen // 2) - (self.HEIGHT_WINDOW // 2), 
        self.WIDTH_WINDOW, 
        self.HEIGHT_WINDOW
    )
        
        self.main_frame = QFrame(parent = self)
        self.main_frame.setFixedSize(1024, 500)
        self.main_frame.setStyleSheet("background-color: #ffffff")
        
        

        

        self.counter_label = QLabel("Всего фреймов: 0", parent=self)
        self.counter_label.setStyleSheet("color: white; font-size: 12px")
        self.counter_label.resize(200, 30)
        self.counter_label.move(20, 520)
        
        

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            frame_click = QFrame(parent = self.main_frame)
            frame_click.setFixedSize(50, 50)
            frame_click.setStyleSheet("background-color: #008bc7")
            frame_click.move(event.pos())
            frame_click.show()
            self.my_frames.append(frame_click)
            self.counter_label.setText(f"Всего фреймов: {len(self.my_frames)}")
            
        
        return super().mousePressEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Backspace:
            for frame in self.my_frames:
                frame.deleteLater()
            self.my_frames.clear()
            self.counter_label.setText("Всего фреймов: 0")
        return super().keyPressEvent(event)
           

        

main_window = MainWindow()




    
    





    






    







