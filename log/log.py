import logging

# 创建一个logger对象
logger = logging.getLogger("my logger")
logger.setLevel(40)
handle = logging.FileHandler("mylog.txt")

fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s -%(pathname)s - %(process)d')
handle.setFormatter(fmt)
# 将handle加入到logger中
logger.addHandler(handle)

# 日志信息
logger.debug("debug 日志")
logger.info("info 日志")
logger.warning("warning 日志")
logger.error("error 日志")
logger.critical("critical 日志")
