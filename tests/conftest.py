#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: conftest.py
@time: 2021/6/8 11:13
"""
import os.path

import allure
import pytest
import yaml


@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir, "config", request.config.getoption("environment"), "config.yaml")
    print(config_path)
    with open(config_path, encoding='utf-8') as f:
        env_config = yaml.load(f, Loader=yaml.SafeLoader)
    return env_config


@pytest.fixture(scope='function')
def save_report():
    yield
    # allure.attach.file('./report.html', attachment_type=allure.attachment_type.HTML)


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")
