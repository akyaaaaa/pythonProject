import allure
import pytest


class TestDemo:

    def setUp(self):
        return 1

    def tearDown(self):
        return 1

    # @allure.feature('打开vivo健康')
    # def test3(self, e, ad):
    #     # e.few('text', 'vivo健康').click()
    #     # e.ClickByImage('jiangkang.jpg')
    #     print("哈哈哈哈")
    #     print(e.find_element_by_ocr(''))
    #     # f.goToDesAndCleanUpData(ad)

    @allure.feature('测试看看')
    def test4(self, ad, e, RecordAVideoWhenFails):
        print(1)
        e.ClickByImage('jiangkang.jpg')
        # ad.tap([(135, 2118)],100)
        # # ad.long_press_keycode(26)
        # f.goToDesAndCleanUpData(ad)



if __name__ == '__main__':
    pytest.main()
