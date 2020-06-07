#-*- coding:utf-8 -*-
#  __author__:qiang
#  2020/4/21

# 导入模块
import unittest

# 定义继承自 unittest.TestCase的测试类
class CalculaateTestCase(unittest.TestCase):

	# 定义以 test 开头的测试方法，这个方法就是测试用例
	def testAdd(self):
		# 断言操作
		self.assertEqual(1+1, 2, msg="断言1+1=2")

	#可以在一个类里边定义N 个测试用例
	def testSubtraction(self):
		self.assertEqual(1-1, 0, msg="断言1-1=0")

# 定义继承自 unittest.TestCase的测试类
class UserTestCase(unittest.TestCase):

	# 定义以 test 开头的测试方法，这个方法就是测试用例
	def testUser(self):
		# 断言操作
		self.assertEqual("zhangsan", "zhangsan", msg="断言1+1=2")

# 创建一个测试加载器
loader =unittest.TestLoader()
# 创建测试套件
suite = unittest.TestSuite()
# 从测试类中加载测试用例
tests = loader.loadTestsFromTestCase(UserTestCase)
# 将测试用例加载到测试组
suite.addTests(tests)

# if __name__ == '__main__':
# 	# 执行测试用例
# 	unittest.main()

