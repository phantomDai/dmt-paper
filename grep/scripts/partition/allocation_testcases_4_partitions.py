#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/10/29
# @Anthor   : phantomDai
"""
为分区模式分配测试用例
"""



def allocation_testcases():
    """
    为每一个分区模式分配测试用例
    :return:
    """
    partition_testcases = {}
    partition_scheme = []

    with open('partition_scheme', 'r') as temp_file:
        for temp_line in temp_file:
            temp_list = temp_line.strip().split(';')
            temp_set = set(ele for ele in temp_list)
            partition_scheme.append(temp_set)
    temp_file.close()

    data_dict = {}

    for ascheme in partition_scheme:
        indexs = []
        with open('partition_scheme_testframes_1.2', 'r') as file:
            counter = 1
            for line in file:
                temp_list = line.strip().split(';')
                filtration_temp_list = [ele for ele in temp_list if ele != '#']
                flag = True
                if len(filtration_temp_list) != len(ascheme):
                    flag = False
                    counter = counter + 1
                    continue

                for ele in filtration_temp_list:
                    if ele not in ascheme:
                        flag = False

                if flag:
                    indexs.append(counter)
                counter = counter + 1
        temp_str = ';'.join(ele for ele in ascheme)
        data_dict[temp_str] = indexs
    partition_scheme_testcases_file = open('partition_scheme_testcases_file', 'w+')
    for ele in data_dict.items():
        partition_scheme_testcases_file.write(str(ele) + '\n')
    partition_scheme_testcases_file.close()






allocation_testcases()












