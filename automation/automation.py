import time
from dataclasses import dataclass
from typing import Optional, Tuple

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from equipment.alchemy import transactional
from equipment.models import ShortRecord
from logger.logger import my_logger
from service.shortservice import ShortService
from utils.converter import convert_to_number


@dataclass
class StepAction:
    xpath: str
    key: Optional[str]
    required: bool
    timeout: int
    note: Optional[str]
    delay_before: float = 0


class Automation:
    _driver: Optional[WebDriver] = None

    def __init__(self, port, driver_path):
        self.url = "https://www.youtube.com"
        self.options = webdriver.ChromeOptions()
        self.driver_path = driver_path
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:{}".format(port))
        self._driver = webdriver.Chrome(options=self.options, service=Service(self.driver_path))
        self._short_service = ShortService()

        self._actions_chain = ActionChains(self._driver)

    def _find_element(self, xpath: str, timeout: int = 3) -> Tuple[Optional[WebElement], bool]:
        element: Optional[WebElement] = None
        self._wait = WebDriverWait(self._driver, timeout)
        try:
            element = self._wait.until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath))
            )
            return element, True
        except TimeoutException:
            my_logger.error(f"TimeoutException: {xpath}")
        return element, False

    @transactional
    def get_information_of_video(self):
        like_count = 0
        comment_count = 0
        hashtags = ""
        description = ""

        def extract_description_and_tags():
            nonlocal description, hashtags
            xpath = '//span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--link-inherit-color"]'
            element, _ = self._find_element(xpath=xpath)

            html = element.get_attribute("outerHTML")

            soup = BeautifulSoup(html, 'html.parser')

            full_text = soup.get_text(strip=True)

            description = full_text.split("#")[0].strip()

            hashtags = [a.get_text(strip=True) for a in soup.find_all('a')]

            print("Mô tả:", description)
            print("Hashtags:", hashtags)

        def extract_like_and_comment():
            nonlocal like_count, comment_count
            like_xpath = '(//span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--text-alignment-center yt-core-attributed-string--word-wrapping"])[1]'
            comment_xpath = '(//span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--text-alignment-center yt-core-attributed-string--word-wrapping"])[3]'

            like_element, _ = self._find_element(xpath=like_xpath)
            if like_element and _:
                like_count = like_element.text

            comment_element, _ = self._find_element(xpath=comment_xpath)
            if comment_element and _:
                comment_count = comment_element.text

        extract_like_and_comment()
        extract_description_and_tags()
        video_url = self._driver.current_url
        print(
            f"Video url: {video_url}| Like: {like_count}| Comment: {comment_count}| Description: {description}| Hashtags: {hashtags}"
        )
        short_record = ShortRecord(
            url=video_url,
            like_count=convert_to_number(str(like_count)),
            comment_count=convert_to_number(str(comment_count)),
            description=description,
            note="",
            is_selected=False,
            hashtags=", ".join(hashtags)
        )
        self._short_service.create_entity(
            entity=short_record
        )

    def click_element_by_js(self, xpath: str, timeout: int = 10, duration: int = 500, required: bool = False):
        element, _ = self._find_element(xpath=xpath, timeout=timeout)
        if _:
            js_code = f"""
            setTimeout(() => {{
                arguments[0].click();
            }}, {duration});
            """
            self._driver.execute_script(js_code, element)
        if not _ and required == True:
            raise RuntimeError(f"{xpath} is required")

    def scroll_down_one_video(self):
        self._actions_chain.send_keys(Keys.ARROW_DOWN).perform()
        self.get_information_of_video()

    def automate(self, actions: list[StepAction], delay: float = 0.1):
        for action in actions:
            time.sleep(action.delay_before)
            my_logger.info(
                f"[XPATH]: {action.xpath} - [KEY]: {action.key} - [TIMEOUT]: {action.timeout} - [REQUIRED]: {action.required} - [NOTE]: {action.note} "
            )
            element, available = self._find_element(xpath=action.xpath, timeout=action.timeout)
            if not available and action.required:
                raise RuntimeError(F"Yêu cầu nhập mục {action.xpath}")
            if available and element:
                self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                actions_chain = ActionChains(self._driver)
                element.click()
                if action.key:
                    element.clear()
                    for key in str(action.key):
                        actions_chain.send_keys(key)
                        time.sleep(0.05)
                    actions_chain.perform()
                time.sleep(delay)
