#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/4
# @Anthor   : phantomDai
"""
传统的蜕变测试技术：随机选择测试用例随机选择蜕变关系
"""
from myutl.Utl import Utl

import random


class MT_random_random(object):

    #获得测试用例的具体信息，索引是行号
    test_cases = []

    #获取测试用例与蜕变关系的映射关系,键是测试用例的编号，值是可以作用的蜕变关系列表
    test_case_2_MRs = {}

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

        #　产生分区编号的候选序列
        self.generate_random_partition_index(seed)

        # record the times of chosing partitions
        counter = 0

        # the flag
        flag = True

        while flag:
            # chose a partition
            partition_index = self.sequence_partition_indexs[counter]

            # chose a test case
            sub_set_chosed_partition = self.partition_info[str(partition_index)]
            test_case_index = sub_set_chosed_partition[random.randint(len(sub_set_chosed_partition))]

            # get concrete test case
            pattern = self.test_cases[test_case_index]

            #


        












