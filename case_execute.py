#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: case_execute.py
@time: 2021/6/9 16:11
"""
import subprocess

allure_cmd = "pytest"
subprocess.call(allure_cmd, shell=True)
print("--------------------")
allure_cmd = "allure generate ./result/ -o ./report/ --clean"
subprocess.call(allure_cmd, shell=True)
