import os
import signal
import subprocess
import sys
import time

import win32con
import win32gui
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication

from config.config import settings
from equipment.alchemy import engine
from equipment.models import BaseModel
from puzzle.youtubepuzzle import YoutubePuzzle
from utils.embed import find_handle, get_pid_from_handle
from utils.port import PortFinder

ROOTPATH = os.getcwd()
os.system(
    f"pyside6-uic {os.path.join(ROOTPATH, 'resources/untitled.ui')} -o {os.path.join(ROOTPATH, 'resources/untitled.py')}"
)
from resources.untitled import Ui_MainWindow

BaseModel.metadata.create_all(engine)


class Application(QtWidgets.QMainWindow, Ui_MainWindow):
    dragPos = None
    register_threads = {}

    def __init__(self):
        super(Application, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.setWindowTitle("Ghost")
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.settings = QSettings("Setting", "MyApp")

        free_port_list = self._embed_browser()
        print(free_port_list)

        self.youtube_puzzle = YoutubePuzzle(ports=free_port_list, driver_path="chromedriver.exe", UI=self.UI)
        self.UI.start_scroll_page.clicked.connect(self.youtube_puzzle.on_start_crawl)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            if hasattr(self, 'dragPos'):
                self.move(event.globalPosition().toPoint() - self.dragPos)
                event.accept()

    def closeEvent(self, event):
        event.accept()

    @staticmethod
    def get_handle_from_pid(browser_pid):
        handles = find_handle()
        for data in handles:
            title, handle = data.split("|")

            pid = get_pid_from_handle(int(handle))
            if pid == browser_pid:
                return handle
        return 0

    def _embed_browser(self):
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        user_data = r'C:\Users\pha4h\Documents\knight-y\data'
        browser_frames = [
            self.UI.frame_browser_1,
            self.UI.frame_browser_2,
            self.UI.frame_browser_3,
            self.UI.frame_browser_4
        ]
        free_port_list = PortFinder.get_free_ports(len(browser_frames))
        print(free_port_list)
        for idx in range(settings.WORKER):
            print(f"Connecting to port: {free_port_list[idx]}")
            profile = rf'Profile {idx + 1}'
            user_data_dir = fr'{user_data}\UserData_{idx + 1}'
            cmd = rf'"{chrome_path}" --remote-debugging-port={free_port_list[idx]} --mute-audio --disable-notifications --force-device-scale-factor=0.6 --user-data-dir="{user_data_dir}" --profile-directory="{profile}" --restore-last-session=true https://www.youtube.com/'
            subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(1)

        time.sleep(5)
        for index, data in enumerate(find_handle("Youtube")):
            hwnd_chrome, title = data
            print(hwnd_chrome, title)
            if "Youtube" in title:
                # Gán vào frame tương ứng
                frame = browser_frames[index]
                hwnd_qt = int(frame.winId())
                win32gui.SetParent(hwnd_chrome, hwnd_qt)

                style = win32gui.GetWindowLong(hwnd_chrome, win32con.GWL_STYLE)
                win32gui.SetWindowLong(hwnd_chrome, win32con.GWL_STYLE,
                                       style & ~win32con.WS_CAPTION & ~win32con.WS_THICKFRAME)

                rect = frame.rect()
                win32gui.MoveWindow(hwnd_chrome, 0, 0, rect.width(), rect.height(), True)

                # Resize event riêng cho từng frame
                def make_resize_event(hwnd):
                    return lambda event: win32gui.MoveWindow(
                        hwnd, 0, 0,
                        event.size().width(),
                        event.size().height(),
                        True
                    )

                frame.resizeEvent = make_resize_event(hwnd_chrome)
        return free_port_list


if __name__ == "__main__":
    app = QApplication([])
    screen = app.primaryScreen()
    try:
        window = Application()
        window.show()
        sys.exit(app.exec())
    except SystemExit:
        os.kill(os.getpid(), signal.SIGTERM)
