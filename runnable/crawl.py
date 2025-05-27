import asyncio
import time
import traceback

from PySide6.QtCore import QObject, QThread, Signal
from selenium.common import TimeoutException

from automation.automation import Automation, StepAction
from config.config import setup
from equipment.alchemy import transactional
from equipment.models import ShortRecord
from logger.logger import my_logger


class CrawlSignal(QObject):
    finished = Signal(ShortRecord, str)


class CrawlThread(QThread):
    def __init__(self, port: int, driver_path: str):
        super().__init__()
        self.signal = CrawlSignal()
        self.port = port
        self.driver_path = driver_path
        self.automation = Automation(
            port=port,
            driver_path=driver_path
        )

    @transactional
    def run(self):
        setup.semaphore.acquire()
        my_logger.info(f"[Crawling]: Starting")
        try:
            asyncio.run(self.boot())
        except asyncio.TimeoutError:
            my_logger.error("[Crawling]: attempt timed out after 10 seconds.")
        except Exception as e:
            my_logger.error(f"[Crawling]: Error occurred: {str(e)}")
        finally:
            self.signal.finished.emit(ShortRecord(), "Note")  # Giả định bạn sẽ truyền AccountRecord
            print("[Crawling]: Done")
            setup.semaphore.release()

    async def boot(self):
        self.automation.automate(
            actions=[
                StepAction(
                    xpath='(//button[@class="style-scope yt-icon-button" and .//yt-icon[@id="guide-icon"]])[1]',
                    timeout=10,
                    required=True,
                    delay_before=0,
                    note="Click trang chủ",
                    key=None
                ),
                StepAction(
                    xpath='(//*[text()="Shorts"])[1]',
                    timeout=10,
                    required=True,
                    delay_before=0,
                    note="Click shorts",
                    key=None
                ),
            ]
        )
        time.sleep(2)
        while True:
            try:
                self.automation.scroll_down_one_video()
            except Exception as e:
                traceback.print_exc()
                raise e
            time.sleep(2)

