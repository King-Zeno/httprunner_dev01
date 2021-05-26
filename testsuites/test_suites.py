
from httprunner.api import HttpRunner

obj = HttpRunner(log_level="DEBUG")

obj.run(r'D:\Work\APITest\engineering\httprunner_dev01\test_suites\demo_testsuite.yml')
res = obj.summary