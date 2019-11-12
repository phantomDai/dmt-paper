import numpy as np
import os
from myutl.Utl import Utl
from MRs.MR import *

class execute_utl(object):
	"""
	为执行测试提供常用的接口
	"""

	mapping_relation_path = os.path.join(os.path.abspath('../..'), 'mapping relation')

	tool = Utl()

	def generate_random_number(self, seed):
		"""
		根据指定的随机数种子生成一系列的随机数，并返回一个列表
		"""
		#设置随机数的种子
		# start_time = int(round(time.time() * 1000))
		np.random.seed(seed)
		random_list = [np.random.randint(1, 101194) for i in range(1000000)]

		# ended_time = int(round(time.time() * 1000))
		return random_list


	def get_test_case_MR_list(self, test_case_index):
		"""
		获取测试用例所有可能作用的蜕变关系
		:test_case_index是测试用例的编号
		"""
		test_cases_2_mrs_path = os.path.join(self.mapping_relation_path, 'testcase_2_MRs')

		#读取一行的内容
		line_content = self.tool.get_line_content(test_cases_2_mrs_path, int(test_case_index))

		#将MR的信息存入list中

		return line_content.split(':')[1].replace('[', '').replace(']', '').split(', ')


	def random_select_MR(self, MR_list):
		"""
		randomly select a MR from the MR list
		:param MR_list:
		:return: the name of selected MR
		"""
		return MR_list[np.random.randint(0, len(MR_list))]

	def generate_follow_test_case(self, MR_name, source_test_case, source_test_case_index):
		"""
		根据选择的蜕变关系以及原始测试用例生成衍生测试用例
		:param MR_name: 　选择的蜕变关系的名称
		:param source_test_case: 原始测试用例
		:return: 衍生测试用例
		"""
		factory = MR_factory()
		MR_obj = factory.choose_MR(MR_name)
		return MR_obj.generate_follow_test_case(source_test_case, source_test_case_index)














if __name__ == '__main__':
	utl = execute_utl()
	print(utl.get_test_case_MR_list('1'))
	# utl.generate_random_number(1)