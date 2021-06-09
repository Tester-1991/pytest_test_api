#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: czb_util.py
@time: 2020/11/24 10:09
"""
import logging
import sys

from loguru import logger

logger.remove()

logger_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>[线程id:{thread}]</red> <blue>{level}</blue> <cyan>名称:{name}</cyan> <green>方法:{function}</green> {line}:<red>{message}</red>"

# 控制台输出
logger.add(sys.stdout, colorize=True, level='DEBUG', format=logger_format)


class PropogateHandler(logging.Handler):

    def emit(self, record):
        logging.getLogger(record.name).handle(record)


# Allure2输出
logger.add(PropogateHandler(), format=logger_format)
