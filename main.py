import math
import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")

        self.num_frames = 21
        self.frames = load_sprite('spriteImages', self.num_frames)

        self.current_frame = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_frame)
        self.is_animating = False
        self.current_fps = 30

        self.setupUI()

        self.update_label()

    def setupUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumSize(200, 200)
        self.image_label.setScaledContents(True)
        main_layout.addWidget(self.image_label)

        slider_layout = QHBoxLayout()
        fps_text_label = QLabel("Frames per second:")
        self.fps_value_label = QLabel(str(self.current_fps))
        slider_layout.addWidget(fps_text_label)
        slider_layout.addWidget(self.fps_value_label)
        slider_layout.addStretch()
        main_layout.addLayout(slider_layout)

        self.fps_slider = QSlider(Qt.Orientation.Horizontal)
        self.fps_slider.setRange(1, 100)
        self.fps_slider.setValue(self.current_fps)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.fps_slider.setTickInterval(10)
        self.fps_slider.valueChanged.connect(self.on_fps_changed)
        main_layout.addWidget(self.fps_slider)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.toggle_animation)
        main_layout.addWidget(self.start_stop_button)

        menubar = self.menuBar()
        control_menu = menubar.addMenu("Control")

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.pause_animation)
        control_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        control_menu.addAction(exit_action)


 def update_label(self):
     if self.frames and self.current_frame < len(self.frames):
         self.image_label.setPixmap(self.frames[self.current_frame])

    def next_frame(self):
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.update_label()

    def on_fps_changed(self, value):
        self.current_fps = value
        self.fps_value_label.setText(str(self.current_fps))
        if self.is_animating:
            delay_ms = int(1000 / self.current_fps)
            self.timer.setInterval(delay_ms)

    def toggle_animation(self):


    def pause_animation(self):


def main():
    app = QApplication(sys.argv)
    window = SpritePreview()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()