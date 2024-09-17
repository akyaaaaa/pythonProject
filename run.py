import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=./temp', '--clean-alluredir'])
    # 生成allure临时文件
    os.system('allure generate ./temp -o ./allure-report --clean')
    # 打开allure报告
    os.system('allure open ./allure-report')
