#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/4
# @Anthor   : phantomDai
"""
传统的蜕变测试技术：随机选择测试用例随机选择蜕变关系
"""
from myutl.Utl import Utl
from utl.Utl import execute_utl

import random
import time


class MT_random_random(object):

    #获得测试用例的具体信息，索引是行号
    test_cases = []

    #获取测试用例与蜕变关系的映射关系,键是测试用例的编号，值是可以作用的蜕变关系列表
    test_case_2_MRs = {}

    exec_utl = execute_utl()

    def __init__(self):
        """
        初始化测试信息
        """
        tool = Utl()
        self.test_cases = tool.get_concrete_test_case()
        self.test_case_2_MRs = tool.get_test_case_2_MRs()

    def execute(self, seed):
        """
        执行测试用例
        :param seed:　指定的随机数种子
        :return:
        """

        started_selecting_all_time = int(round(time.time() * 1000))
        #获取由指定种子产生的一系列随机值，作为选择的测试用例的编号
        random_list = exec_utl.generate_random_number(seed)
        ended_selecting_all_time = int(round(time.time() * 1000))

        # 选择测试用例需要的总时间
        selecting_all_test_cases_time = ended_selecting_all_time - started_selecting_all_time


        #开始遍历测试用例
        for test_case_index in random_list:

            # 获取正则表达式
            source_pattern = test_cases[test_case_index]

            # 获取该正则表达式可以作用的蜕变关系的集合，然后随机选择一个蜕变关系
            MRs = self.exec_utl.get_test_case_MR_list(test_case_index)

            #randomly select a MR
            selected_MR = self.exec_utl.random_select_MR(MRs)

            # 获取衍生测试用例
            follow_pattern = self.exec_utl.generate_follow_test_case(selected_MR,
                                                                     source_pattern, test_case_index)

            




        












