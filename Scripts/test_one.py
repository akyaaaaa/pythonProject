import allure
import pytest

from userFunctions.Functions import Functions as f


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
        # output,_ = f.cmd(['adb', 'devices'])
        # ad.start_activity('air.tv.douyu.android','com.douyu.module.home.pages.main.MainActivity')
        f.call('10086')
        # print(ad.current_activity)



if __name__ == '__main__':
    pytest.main()
