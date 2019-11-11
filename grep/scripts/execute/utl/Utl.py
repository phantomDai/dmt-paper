import numpy as np


class execute_utl(object):
	"""
	为执行测试提供常用的接口
	"""


	def generate_random_number(self, seed):
		"""
		根据指定的随机数种子生成一系列的随机数，并返回一个列表
		"""
		#设置随机数的种子
		np.random.seed(seed)
		random_list = [np.random.randint(1, 101194) for i in range(1000000)]

		return random_list



if __name__ == '__main__':
	utl = execute_utl()
	print(utl.generate_random_number(1))