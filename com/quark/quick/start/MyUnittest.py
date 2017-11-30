import unittest


class Test(unittest.TestCase):
    # 重写父类setUp方法
    def setUp(self):
        print("Test.setUp")

    # 定义测试用例，以“test_”开头命名的方法
    def test_one(self):
        print("Test.test_One")

    # 重写父类tearDown方法
    def tearDown(self):
        print("Test.tearDown")


class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1.setUp")

    def test_one(self):
        print("Test1.test_One")

    def tearDown(self):
        print("Test1.tearDown")


if __name__ == '__main__':
    # 执行所有测试用例
    unittest.main()
    # 执行指定的测试用例
    suite = unittest.TestSuite()
    suite.addTest(Test('test_one'))
    # suite.addTest(Test1('test_one'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # 判断是否为数字
