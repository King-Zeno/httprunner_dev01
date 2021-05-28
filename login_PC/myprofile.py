
from httprunner.api import HttpRunner

obj = HttpRunner(log_level="DEBUG")

obj.run(r'D:\Work\APITest\engineering\httprunner_dev01\login_PC\myprofile.yml')
res = obj.summary
