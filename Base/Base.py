import base64
import logging
import os
import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 创建一个logger对象
logger = logging.getLogger("my logger")
black_list = [
    (AppiumBy.ID, "com.vivo.health:id/positiveButton")
]


# 黑名单装饰器
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

    def black_wrapper(func):
        def run(*args, **kwargs):
            self = args[0]
            try:
                logger.info(f"开始查找元素{args[2]}")
                # 调用原来的函数并返回结果
                return func(*args, **kwargs)
            # 此处的e,代表只捕获e这一种类型的exception
            except Exception as e:
                for black in black_list:
                    # 查找黑名单中的每一个元素
                    logger.warning(f"处理黑名单:{black}")
                    elements = self.driver.find_elements(*black)
                    if len(elements) > 0:
                        elements[0].click()
                        return func(*args, **kwargs)
                # 遍历完黑名单之后，如果仍然没有找到元素，就抛出异常
                self.add_screenshot_to_allure("错误截图")
                logger.error(f"遍历黑名单，仍然未找到元素信息————>>{e}")
                raise e

        return run

    @black_wrapper
    def few(self, strategy, value):

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
