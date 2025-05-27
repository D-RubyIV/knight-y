from typing import Optional

from PySide6 import QtTest, QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QTableWidgetItem
from selenium.webdriver.chrome.webdriver import WebDriver

from common.constant import TableHeaderLabel, Constants
from equipment.models import ShortRecord
from resources.untitled import Ui_MainWindow
from runnable.crawl import CrawlThread
from service.shortservice import ShortService
from utils.string import safe_string
from utils.table import TableUtil
from utils.time import time_relative


def setup_first_col_tg_table_widget(short_object: ShortRecord):
    # Create a QTableWidgetItem and set its name

    chk_box = QCheckBox()
    chk_box.setChecked(short_object.is_selected)

    # Thêm checkbox vào ô trong bảng

    # Tạo QTableWidgetItem cho tên
    name_item = QTableWidgetItem(short_object.url)
    name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

    chk_box_item = QTableWidgetItem(short_object.url)
    chk_box_item.setFlags(
        QtCore.Qt.ItemFlag.ItemIsUserCheckable |
        QtCore.Qt.ItemFlag.ItemIsEnabled |
        QtCore.Qt.ItemFlag.ItemIsSelectable
    )
    # Set the checkbox state based on tg_object's is_selected property
    if short_object.is_selected:
        chk_box_item.setCheckState(QtCore.Qt.CheckState.Checked)
    else:
        chk_box_item.setCheckState(QtCore.Qt.CheckState.Unchecked)

    # Attach custom data for tg_object
    chk_box_item.setData(256, short_object)  # 256 is a custom role
    chk_box_item.setData(Qt.ItemDataRole.DisplayRole, short_object.url)  # Correct DisplayRole value

    return chk_box_item


class YoutubePuzzle:
    driver_path = None
    _driver: Optional[WebDriver] = None

    def __init__(self, UI: Ui_MainWindow, ports: list[int], driver_path: str):
        self.driver_path = driver_path
        self.ports = ports
        self.UI = UI
        self.short_service = ShortService()
        self.tbObject = self.UI.tableWidget
        self.setup_table()

    def on_start_crawl(self):
        threads = {}
        for idx, port in enumerate(self.ports):
            threads[idx] = CrawlThread(
                driver_path=self.driver_path,
                port=port
            )
            threads[idx].start()
            QtTest.QTest.qWait(3000)

        for thread in threads:
            while threads[thread].isRunning():
                QtTest.QTest.qWait(100)

    def setup_table(self):
        table_util = TableUtil(table_object=self.UI.tableWidget)
        table_util.init_header_labels(TableHeaderLabel.header_labels_short)
        table_util.clear_table()
        list_account_record: list[ShortRecord] = self.short_service.get_entities()
        for index, account_object in enumerate(list_account_record):
            current_row = self.tbObject.rowCount()
            self.tbObject.insertRow(current_row)
            # @formatter:off
            like_count_item = QTableWidgetItem()
            like_count_item.setData(QtCore.Qt.ItemDataRole.DisplayRole, account_object.like_count)

            comment_count_item =  QTableWidgetItem()
            comment_count_item.setData(QtCore.Qt.ItemDataRole.DisplayRole, account_object.comment_count)
            fields = [
                (Constants.Short.lbTGTableUrl, setup_first_col_tg_table_widget(account_object)),
                (Constants.Short.lbTGTableLikeCount, like_count_item),
                (Constants.Short.lbTGTableCommentCount, comment_count_item),
                (Constants.Short.lbTGTableNote, QTableWidgetItem(safe_string(account_object.note))),
                (Constants.Short.lbTGTableDescription, QTableWidgetItem(safe_string(account_object.description))),
                (Constants.Short.lbTGTableHashtags, QTableWidgetItem(safe_string(account_object.hashtags))),
                (Constants.Short.lbTGTableCreatedAt, QTableWidgetItem(time_relative(safe_string(account_object.created_time)))),
                (Constants.Short.lbTGTableUpdatedAt, QTableWidgetItem(time_relative(safe_string(account_object.updated_time))))
            ]
            # @formatter:on
            for label, value in fields:
                self.tbObject.setItem(current_row, table_util.find_index_tbl(label), value)
