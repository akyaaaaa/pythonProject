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
        # e.ClickByImage('jiangkang.jpg')
        print("哈哈哈哈")
        print(e.find_element_by_ocr(''))
        # f.goToDesAndCleanUpData(ad)

    def test4(self, ad):
        print(ad.is_locked())
        ad.reset()



if __name__ == '__main__':
    pytest.main()
