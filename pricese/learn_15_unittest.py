import unittest
import sys

print("当前地址{}".format(sys.path))

class demo(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(1, 2, "判断相等")

    @unittest.skipIf(1 + 1 == 2, "SKIP")
    def test_case02(self):
        print("test_case01")
        self.assertEqual(3, 4, "判断相等")

    @unittest.skip
    def test_case03(self):
        print("test_case01")
        self.assertEqual(4, 5, "判断相等")


class demo1(unittest.TestCase):
    def test_case01(self):
        print("test_case01")
        self.assertEqual(1, 2, "判断相等")

    def test_case02(self):
        print("test_case01")
        self.assertEqual(3, 3, "判断相等")


class demo2(unittest.TestCase):
    def test_case01(self):
        print("demo2 test_case01")
        self.assertEqual(1, 2, "判断相等")

    def test_case02(self):
        print("demo2 test_case01")
        self.assertEqual(3, 3, "判断相等")


if __name__ == '__main__':
    # unittest.main()
    # 可以测试多个方法
    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_case02"))
    # unittest.TextTestRunner.run(suite)

    # 可以测试多个类
    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suiteall)

    # 路径下所有以test开头的py文件
    discovery = unittest.defaultTestLoader.discover("./", "test*.py")
    unittest.TextTestRunner().run(discovery)

    # HTMLTestRunner报告
