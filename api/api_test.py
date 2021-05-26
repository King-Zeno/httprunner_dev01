
from httprunner.api import HttpRunner

obj = HttpRunner(log_level="DEBUG")

obj.run('D:/Work/APITest/engineering/httprunner_dev01/api/login.yml')
res = obj.summary
