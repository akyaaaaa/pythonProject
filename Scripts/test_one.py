import os
import time
import allure
import pytest

from uiautomator2 import Device
from Base.Base import Base


class TestDemo:

    def setUp(self):
        return 1
    def tearDown(self):
       return 1


    @allure.feature('打开vivo健康')
    def test3(self, RecordAVideoWhenFails, e):
        time.sleep(3)
        # 获取录屏路径
        # video_path = RecordAVideoWhenFails["video_path"]
        # 测试逻辑
        assert False, "This is a test failure."



if __name__ == '__main__':
    pytest.main()


