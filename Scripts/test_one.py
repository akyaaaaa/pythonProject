import allure
import pytest


class TestDemo:

    def setUp(self):
        return 1

    def tearDown(self):
        return 1

    @allure.feature('打开vivo健康')
    def test3(self, e, ad):
        # e.few('text', 'vivo健康').click()
        # # 等待弹出窗口出现
        # time.sleep(1)
        # e.few('text', '每日活动').click()
        # # assert False, "This is a test failure."
        e.ClickByImage('jiangkang.jpg')
        print("哈哈哈哈")

if __name__ == '__main__':
    pytest.main()
