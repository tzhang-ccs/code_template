from loguru import logger
import sys

logger.remove()
fmt = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{level}</cyan> | {message}"
logger.add(sys.stdout, format=fmt)
logger.add('log')

logger.info('hello')

