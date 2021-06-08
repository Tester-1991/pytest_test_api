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

    def get_test_data(self, test_data_path):
        case = []  # 存储测试用例名称
        http = []  # 存储请求对象
        expected = []  # 存储预期结果
        dat = yaml.safe_load(open(test_data_path, encoding='utf-8'))
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
        parameters = zip(case, http, expected)
        return case, parameters
