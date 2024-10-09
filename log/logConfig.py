import logging
import os

from userConf.config import PROJECT_ROOT


def setup_logger():
    # 确保日志目录存在
    log_path = os.path.join(PROJECT_ROOT, 'log')

    os.makedirs(log_path, exist_ok=True)

    # 创建一个logger
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logFile_path = log_path
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(logFile_path)
    fh.setLevel(logging.DEBUG)  # 也可以为handler单独设置日志级别

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # 只输出DEBUG及以上级别的日志到控制台

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(process)d')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


# 在模块加载时立即配置logger

logger = setup_logger()
