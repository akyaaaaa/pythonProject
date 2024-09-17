import base64
import os
import re
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver
    # 截图并返回路径
    def take_screenshot(self, filename):
        # 从当前时间获取一个格式化的数字
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        filepath = os.path.join(screenshot_dir, f"{filename}_{timestamp}.png")
        self.driver.save_screenshot(filepath)
        return filepath

        # 显示等待查找
    def few(self, strategy, value):
        try:
            if strategy == 'text':
                # 使用普通文本匹配
                element = WebDriverWait(self.driver, 10).until(
                    self.find_by_text(value)
                )
            elif strategy == 'regex_text':
                # 使用正则表达式匹配文本
                element = WebDriverWait(self.driver, 10).until(
                    self.find_by_regex_text(value)
                )
            else:
                # 使用通用查找策略。BY.xxx之类的
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((strategy, value))
                )
            return element
        except TimeoutException:
            # 如果找不到元素，则截图
            print("开始截图")
            self.add_screenshot_to_allure("错误截图")
            raise

    def find_by_text(self, value):
        return EC.presence_of_element_located((By.XPATH, f"//*[@text='{value}']"))

    def find_by_regex_text(self, regex):
        return EC.presence_of_element_located((By.XPATH, f"//*[matches(@text,'{regex}')]"))

    def add_screenshot_to_allure(self, name, attachment_type=allure.attachment_type.PNG):
        """将截图添加到 Allure 报告中"""
        screenshot_path = self.take_screenshot(name)
        with open(screenshot_path, "rb") as screenshot:
            allure.attach(screenshot.read(), name=name, attachment_type=attachment_type)

    def start_recording_screen(self):
        self.driver.start_recording_screen()

    def stop_recording_screen(self):
        video_data = self.driver.stop_recording_screen()

        if isinstance(video_data, str):
            # 尝试解码 Base64 字符串
            video_data = base64.b64decode(video_data)
        assert isinstance(video_data, bytes), "The video data should be of type bytes."
        return video_data


if __name__ == '__main__':
    print()
