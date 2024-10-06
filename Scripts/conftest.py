import os
import time

import allure
import pytest
from appium import webdriver
from uiautomator2 import connect

from Base.Base import Base

# 创建 FailureVideo 目录
failure_video_dir = "FailureVideo"
if not os.path.exists(failure_video_dir):
    os.makedirs(failure_video_dir)


# UIAutomator2 驱动
@pytest.fixture(scope="session")
def d():
    print("Connecting to device...")
    d = connect('aeada375')
    yield d
    print("Disconnecting from device...")


# Appium 驱动
@pytest.fixture(scope="session")
def ad():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        # "deviceName": "aeada375",
        "deviceName": "emulator-5554",
        # 'noReset': True,
        # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        # 'resetKeyboard': True,  # 执行完程序恢复原来输入法
    }

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print(f"连接成功 --> {desired_caps['deviceName']}")
    yield driver
    driver.quit()


# 录屏功能
@pytest.fixture(scope="function")
def RecordAVideoWhenFails(e, request):
    # 确保路径是一一致的
    video_path = os.path.join(failure_video_dir, f"{request.cls.__name__}_{time.strftime('%Y%m%d_%H%M%S')}.mp4")

    # 开始录屏
    e.start_recording_screen()

    try:
        yield {"video_path": video_path}
    finally:
        # 停止录屏
        video_data = e.stop_recording_screen()
        request.node.video_data = video_data  # 保存录制的数据供后续使用


# 自定义hook来捕获测试结果
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


# 自定义hook在测试结束时保存视频
@pytest.fixture(autouse=True)
def hook_finalization(request, tmp_path):
    yield
    if hasattr(request.node, 'video_data'):
        if request.node.rep_call.failed:
            video_path = os.path.join(failure_video_dir,
                                      f"{request.node.originalname}_{time.strftime('%Y%m%d_%H%M%S')}.mp4")
            with open(video_path, "wb") as video_file:
                video_file.write(request.node.video_data)
            print(f"视频已保存到: {video_path}")
            # 尝试附加到 Allure 报告
            try:
                with open(video_path, 'rb') as f:
                    allure.attach(f.read(), video_path, allure.attachment_type.MP4)
                print("视频已附加到 Allure 报告")
            except Exception as e:
                print(f"Failed to attach video to Allure report: {e}")


# Base 类实例化
@pytest.fixture(scope="session")
def e(ad):
    yield Base(ad)
