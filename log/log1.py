import logging

logging.basicConfig(filename='mylog1.txt',filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s -%(pathname)s - %(process)d',
                    level=logging.DEBUG)
# 创建一个logger对象
logger = logging.getLogger("my logger")


# 日志信息
logger.debug("debug 日志")
logger.info("info 日志")
logger.warning("Some one delete the log file.",exc_info=True,stack_info=True,extra={'user':'Tom','ip':'192.168.1.1'})
logger.error("error 日志")
logger.critical("critical 日志")

