#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: test_in_post.py
@time: 2021/6/7 18:41
"""
import pytest
import requests

from utils.yaml_util import YamlUtil

cases, list_params = YamlUtil().get_test_data("./data/test_in_post.yaml")


class TestInPost(object):

    @pytest.mark.skip("")
    def test_in_post(self):
        host = 'http://jsonplaceholder.typicode.com'
        path = '/posts'
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        headers = {
            "Content-Type": "application/json"
        }

        r = requests.request("POST", url=host + path, headers=headers, json=body)
        response = r.json()
        print(response)
        # 返回的response ={'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
        assert response["userId"] == body["userId"]
        assert response["title"] == body["title"]
        assert response["body"] == body["body"]

    @pytest.mark.skip("")
    def test_in_post2(self):
        host = 'http://jsonplaceholder.typicode.com'
        request_data = YamlUtil().read("../data/test_in_post.yaml")
        print(request_data)
        path = request_data['tests'][0]['http']['path']
        body = request_data['tests'][0]['http']['body']
        headers = request_data['tests'][0]['http']['headers']
        r = requests.request("POST", url=host + path, headers=headers, json=body)
        response = r.json()
        print(response)
        # 返回的response ={'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
        assert response["userId"] == body["userId"]
        assert response["title"] == body["title"]
        assert response["body"] == body["body"]

    @pytest.mark.parametrize("case,http,expected", list_params, ids=cases)
    def test_in_post3(self, case, http, expected):
        # print(case)
        print(http)
        print(expected)
