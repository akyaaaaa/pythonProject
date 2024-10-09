import subprocess

from Base.Base import Base
from log.logConfig import logger


class Functions:

    # 回到桌面并清理数据
    @staticmethod
    def goToDesAndCleanUpData(d):
        # # 模拟按下 home 键
        # d.press_keycode(3)
        # # 模拟按下 Recent 键
        # d.press_keycode(187)
        logger.info("Clean up data")
        Functions.Press(d, 'home')
        Functions.Press(d, 'recent')
        Base(d).few('xpath', '//*[@content-desc="清除全部-按钮"]').click()

    # 创建按键名称到键码的映射表，可以自己添加
    keycode_map = {
        "home": 3,
        "recent": 187,
        "back": 4,
        "meun": 82,
        # 音量+
        "VOLUME_UP": 24,
        # 音量-
        "VOLUME_DOWN": 25,
        "power": 26,
        # 相机
        "CAMERA": 27,

        # 添加更多按键映射
    }
    @staticmethod
    def Press(d, kname):
        if kname in Functions.keycode_map:
            d.press_keycode(Functions.keycode_map[kname])

    @staticmethod
    def LongPress(d, kname):
        if kname in Functions.keycode_map:
            d.long_press_keycode(Functions.keycode_map[kname])

        else:
            raise ValueError("Invalid key name")

    @staticmethod
    def cmd(command):
        """
        使用subprocess.run执行命令行命令，这是在Python程序中执行外部命令的一种常用方式。
        capture_output=True表示子进程的输出将被捕获并返回，text=True表示输出和错误输出将作为文本而不是字节返回，这使得处理结果更加直观和方便
           运行 adb 命令
           :param command: 命令列表，例如 ['adb', 'devices']
           :return: 命令的输出
        """

        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout, result.stderr

    '''
    appuim提供了start_activity()
    @staticmethod
    def start_app(package_name, activity_name):
        """
        使用 adb 命令启动应用
        :param package_name: 应用包名
        :param activity_name: 应用主 Activity 名称
        uiautomator2 current 查看当前包名和activity_name，前提得安装ui2
        """
        command = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']
        Functions.cmd(command)
    '''

    @staticmethod
    def stop_app(package_name):
        """
        使用 adb 命令停止应用
        :param package_name: 应用包名
        """
        command = ['adb', 'shell', 'am', 'force-stop', package_name]
        Functions.cmd(command)

    @staticmethod
    def call(number, device='aeada375'):
        # adb shell am start -a android.intent.action.CALL -d tel:1234567890
        command = ['adb', '-s', f'{device}', 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d',
                   f'tel:{number}']
        Functions.cmd(command)

    @staticmethod
    def end_call(device='aeada375'):
        command = ['adb', '-s', f'{device}', 'shell', 'input', 'keyevent', '6']
        Functions.cmd(command)
