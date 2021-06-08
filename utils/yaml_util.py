#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: yaml_util.py
@time: 2021/6/8 09:55
"""
import yaml


class YamlUtil(object):

    def read(self, path):
        data = yaml.safe_load(open(path, encoding='utf-8'))
        return data
