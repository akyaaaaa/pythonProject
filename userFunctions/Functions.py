from Base.Base import Base
class Functions:
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
    # 回到桌面并清理数据
    @staticmethod
    def goToDesAndCleanUpData(d):
        # # 模拟按下 home 键
        # d.press_keycode(3)
        # # 模拟按下 Recent 键
        # d.press_keycode(187)
        Functions.press(d, 'home')
        Functions.press(d, 'recent')
        Base(d).few('xpath', '//*[@content-desc="清除全部-按钮"]').click()

    # 创建按键名称到键码的映射表

    @staticmethod
    def press(d, kname):
        if kname in Functions.keycode_map:
            d.press_keycode(Functions.keycode_map[kname])


        else:
            raise ValueError("Invalid key name")
