#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/5
# @Anthor   : phantomDai
"""
the abstract class
"""
import abc
import os
from random import shuffle
import random

from myutl.MR_Utl import MyUtl
from myutl.Utl import Utl


class MR(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        raise Exception('You must reimplement this method!')


    @abc.abstractmethod
    def verify_results(self, mutant_name, testing_index):
        raise Exception('You must reimplement this method')

"""
the implemention of MR1
"""
class MR1(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR1
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        range_character_set = self.mr_utl.get_range_charaters_MR1(source_test_case)
        min_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[0])
        max_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[1])
        valid_characters = shuffle([chr(asc) for asc in range(min_value, max_value + 1)])
        modified_character_set = ''.join(ele for ele in valid_characters)
        modified_character_set = '[' + modified_character_set + ']'
        follow_up_test_case = source_test_case.replace(range_character_set, modified_character_set)
        return follow_up_test_case

    def verify_results(self, mutant_name, testing_index):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param mutant_name: 执行的变异体的名字
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.verify_results(mutant_name, testing_index)

"""
the implemention of MR2
"""
class MR2(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR2
        :param source_test_case:
        :return: follow-up test case
        """

        # 获取范围集合
        range_character_set = self.mr_utl.get_range_charaters_MR1(source_test_case)
        min_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[0])
        max_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[1])

        valid_characters = shuffle([chr(asc) for asc in range(min_value, max_value + 1)])

        modified_character_set = '|'.join(ele for ele in valid_characters)
        follow_up_test_case = source_test_case.replace(range_character_set, modified_character_set)

        return follow_up_test_case


    def verify_results(self, mutant_name, testing_index):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param mutant_name: 执行的变异体的名字
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.verify_results(mutant_name, testing_index)

"""
the implemention of MR3
"""
class MR3(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        range_character_set = self.mr_utl.get_collection_characters_MR3(source_test_case)

        new_character = ['[' + ele + ']' for ele in range_character_set.replace('[', '').replace(']', '')]
        new_case = '|'.join(ele for ele in new_character)

        follow_up_test_case = source_test_case.replace(range_character_set, new_case)
        return follow_up_test_case

    def verify_results(self, mutant_name, testing_index):

        return self.mr_utl.verify_equal(mutant_name, testing_index)

"""
the implemention of MR4
"""
class MR4(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合字符串
        old_range_character_set_str = self.mr_utl.get_range_charaters_MR1(source_test_case)

        # 获得最小、中间和最大的ＡＳＣＩＩ码值
        min_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[0])
        middle_asc = min_asc + 1
        max_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[1])
        new_range_character_set_str = '[' + chr(min_asc) + '-' + chr(middle_asc) + ']|[' + \
                                      chr(middle_asc + 1) + '-' + chr(max_asc) + ']'

        return source_test_case.replace(old_range_character_set_str, new_range_character_set_str)


    def verify_results(self, mutant_name, testing_index):

        return self.mr_utl.verify_equal(mutant_name, testing_index)



"""
the implemention of MR5
"""
class MR5(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        new_order = [c1 for c1 in source_test_case]
        shuffle(new_order)
        return '[' + ''.join(c for c in new_order) + ']'


    def verify_results(self, mutant_name, testing_index):

        return self.mr_utl.verify_appertain(mutant_name, testing_index)


"""
the implemention of MR6
"""
class MR6(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        new_order = [c1 for c1 in source_test_case]
        shuffle(new_order)
        return '|'.join(c for c in new_order)


    def verify_results(self, mutant_name, testing_index):

        return self.mr_utl.verify_appertain(mutant_name, testing_index)


"""
the implemention of MR7
"""
class MR7(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        old_range_character_set_str = self.mr_utl.get_range_charaters_MR1(source_test_case)
        # 获得最大和最小的ａｓｃＩＩ码值
        min_asc = ord(old_range_character_set_str.replace('[','').replace(']','').split('-')[0])
        max_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[1])
        middle_asc = max_asc - 1
        new_range_character_set_str = '[' + chr(min_asc) + '-' + chr(middle_asc) + ']'

        return source_test_case.replace(old_range_character_set_str, new_range_character_set_str)

    def verify_results(self, mutant_name, testing_index):
        return self.mr_utl.verify_includ(mutant_name, testing_index)


"""
the implemention of MR8
"""
class MR8(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        old_range_character_set_str = self.mr_utl.get_range_charaters_MR1(source_test_case)
        # 获得最大和最小的ａｓｃＩＩ码值
        min_asc = ord(old_range_character_set_str.replace('[','').replace(']','').split('-')[0])
        max_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[1])
        new_max_asc = max_asc + 1
        new_range_character_set_str = '[' + chr(min_asc) + '-' + chr(new_max_asc) + ']'

        return source_test_case.replace(old_range_character_set_str, new_range_character_set_str)

    def verify_results(self, mutant_name, testing_index):
        return self.mr_utl.verify_appertain(mutant_name, testing_index)


"""
the implemention of MR9
"""
class MR9(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case: 在source_test_case的基础上增加"|[[:digit:]]"
        """
        return source_test_case + "|[[:digit:]]"

    def verify_results(self, mutant_name, testing_index):
        return self.mr_utl.verify_result_MR9(mutant_name, testing_index)


"""
the implemention of MR10
"""
class MR10(MR):
    mr_utl = MyUtl()
    tool = Utl()
    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case: 在source_test_case的基础上增加"|[[:digit:]]"
        """
        candidate_literals = ['{1}', '+']

        normal_literals_path = os.path.join(parent_path, 'MR10Relation', 'normal_literals')

        normal_literals = tool.get_line_content(normal_literals_path, int(source_test_case_index))

        new_normal_literals = normal_literals + candidate_literals[random.randint(0, 1)]

        return  source_test_case.replace(normal_literals, new_normal_literals)

    def verify_results(self, mutant_name, testing_index):
        return self.mr_utl.verify_equal(mutant_name, testing_index)


"""
the implemention of MR11
"""
class MR11(MR):
    mr_utl = MyUtl()
    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR11
        :param source_test_case:
        :return:
        """
        a_dict = dict()
        a_dict['\w'] = '\W'
        a_dict['\W'] = '\w'
        a_dict['\s'] = '\S'
        a_dict['\S'] = '\s'
        a_dict['[[:digit:]]'] = '[^[:digit:]]'
        a_dict['[^[:digit:]]'] = '[[:digit:]]'
        a_dict['[[:alnum:]]'] = '[^[:alnum:]]'
        a_dict['[^[:alnum:]]'] = '[[:alnum:]]'
        valid_choices = ['\w', '\W', '\s', '\S', '[[:digit:]]', '[^[:digit:]]', '[[:alnum:]]', '[^[:alnum:]]']

        old_value = ''
        new_value = ''

        for index in range(0, len(valid_choices)):
            if valid_choices[index] in source_test_case:
                old_value = valid_choices[index]
                new_value = a_dict[valid_choices[index]]

        return source_test_case.replace(old_value, new_value)


    def verify_results(self, mutant_name, testing_index):
        return self.mr_utl.verify_result_MR9(mutant_name, testing_index)

"""
the implemention of MR12
"""
class MR12(MR):
    mr_utl = MyUtl()
    tool = Utl()
    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        将source_test_case中的正常字符添加...，本文为了方便将所有的正常字符转化为"..."
        ＠source_test_case: 原始测试用例
        ＠source_test_case_index原始测试用例的编号，在ＭＲＸ文件中对应一行测试用例的最前面的数字，例如：
        1:only：１就是source_test_case_index的编号，only为实际的测试用例
        @return: 衍生测试用例
        """
        #获取原始测试用例中的正常字符
        normal_literals_path = os.path.join(parent_path, 'MR12Relation', 'normal_literals')
        normal_literal = tool.get_line_content(normal_literals_path, int(source_test_case_index))

        new_normal_literal = ''
        for i in range(0, len(normal_literal)):
            new_normal_literal += '.'

        return source_test_case.replace(normal_literal, new_normal_literal)


    def verify_results(self, mutant_name, testing_index):
        return mr_utl.verify_appertain(mutant_name, testing_index)




if __name__ == '__main__':
    mr = MR7()
    print(mr.generate_follow_test_case(r"\<[1-3]\>"))
    # print(mr.verify_results('mutant1', '1'))

