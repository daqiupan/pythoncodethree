import HTMLTestRunner
import unittest

testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite())
filename=r'D:/'
fp=open(filename,'wb')
runner=fp
title=u'大邱.com测试报告'
description=u'用例执行情况'

runner.run(testunit)