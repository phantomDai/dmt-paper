#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/5
# @Anthor   : phantomDai
"""
一些蜕变关系实现过程中的工具接口
"""
import re
import os

class MyUtl(object):

    def get_range_charaters_MR1(self, source_test_case):
        """
        从一个字符串中获取一个范围字符集合，例如[1-3]
        :param aline: 一个ｐａｔｔｅｒｎ
        :return: 范围集合
        """
        target_str = re.findall(r'\[\w-\w\]', source_test_case)
        return target_str[0]

    def get_collection_characters_MR3(self, source_test_case):
        """
        从一个字符串中获取一个范围字符集合，例如[abc]
        :param aline: 一个ｐａｔｔｅｒｎ
        :return: 范围集合
        """
        target_str = re.findall(r'\[\w*\]', source_test_case)
        return target_str[0]





    def verify_equal(self, mutant_name, testing_index):

        """
        验证原始测试用例与衍生测试用例的执行结果
        :param mutant_name: 执行的变异体的名字
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        shell_command = 'diff ../testingResults/' + mutant_name + '/' + testing_index + '_source ../testingResults/' + \
                        mutant_name + '/' + testing_index + '_follow'

        result = os.popen(shell_command).read()

        if len(result) == 0:
            return False
        else:
            return True

    def verify_appertain(self, muant_name, testing_index):
        """
        验证原始测试用例的执行结果是否都出现在衍生测试用例的结果中
        :param muant_name: 执行的变异体的名字
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', muant_name, testing_index + '_source')
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', muant_name, testing_index + '_follow')

        flag = False

        with open(source_result_path, 'r') as source_file:
            for line in source_file:
                with open(follow_result_path, 'r') as follow_file:
                    if line.strip() not in follow_file.readlines():
                        flag = True
                        break
                follow_file.close()
        source_file.close()

        return flag


    def verify_includ(self, mutant_name, testing_index):
        """
        验证原始测试用例的执行结果是否包含衍生测试用例的结果
        :param muant_name: 执行的变异体的名字
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', muant_name,
                                          testing_index + '_source')
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', muant_name,
                                          testing_index + '_follow')
        flag = False

        with open(follow_result_path, 'r') as source_file:
            for line in source_file:
                with open(source_result_path, 'r') as follow_file:
                    if line.strip() not in follow_file.readlines():
                        flag = True
                        break
                source_file.close()
        follow_file.close()

        return flag


    def verify_result_MR9(self, mutant_name, testing_index):
        """
        验证MR9的执行结果：原始测试用例的执行结果出现在衍生测试用例的执行结果中，并且包含２１８１１１
        :param mutant_name:
        :param testing_index:
        :return:
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', muant_name,
                                          testing_index + '_source')
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', muant_name,
                                          testing_index + '_follow')

        flag = False

        with open(source_result_path, 'r') as source_file:
            for line in source_file:
                with open(follow_result_path, 'r') as follow_file:
                    if '218111' not in follow_file.readlines():
                        flag = True
                        break
                    if line.strip() not in follow_file.readlines():
                        flag = True
                        break
                follow_file.close()
        source_file.close()

        return flag


    def verify_MR10(self, mutant_name, testing_index):
        """
        验证ＭＲ１１的测试结果，该测试结果需要根据特殊的输入文件进行确定，特殊的输入文件存放在名为“ｔａｒｇｅｔFiles”
        的目录中，该目录包含两部分的内容：file.test和该ＭＲ用到的目标文件：

        :param mutant_name:
        :param testing_index:
        :return:
        """







if __name__ == '__main__':
    utl = MyUtl()
    print(utl.verify_appertain('mutant1', '1'))