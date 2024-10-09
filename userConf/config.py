import os
from datetime import datetime

# C:\\Users\\Administrator\\pythonProject\\userConf
CUREE_DIR = os.path.abspath(os.path.dirname(__file__))
# 获取项目根目录  C:\\Users\\Administrator\\pythonProject\\
PROJECT_ROOT = os.path.dirname(CUREE_DIR)
# 获取当前时间并格式化
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
# 截图路径join意思就是用分号把变量拼接起来
OCR_SCREENSHOT_PATH = os.path.join(PROJECT_ROOT, 'BaiDuOCR', 'ocr_screenshots', f'screenshot{timestamp}.png')
JOSN_ROOT_PATH = os.path.join(PROJECT_ROOT, 'TestData')
FailureVideo = os.path.join(PROJECT_ROOT, 'Resources', 'FailureVideo')
screenshots = os.path.join(PROJECT_ROOT, 'Resources', 'screenshots')
picture = os.path.join(PROJECT_ROOT, 'Resources', 'picture')
allure_path = os.path.join(PROJECT_ROOT, 'allure-report')
