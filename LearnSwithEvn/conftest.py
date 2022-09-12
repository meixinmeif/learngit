global_env = {}
#添加命令行参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='设置接口自动化测试默认的环境')

#获取设置的命令行参数
def pytest_configure(config):
    default_ev = config.getoption("--env")
    tmp = {"env": default_ev}
    global_env.update(tmp)