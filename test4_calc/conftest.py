import os

import pytest
import yaml

# 获取文件路径
from test4_calc.calc import Calc

file_path = os.path.dirname(__file__) + "\\data.yml"
# 获取yaml数据
with open(file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    datas_addids = datas['addids']
    datas_sub = datas['sub']
    datas_subids = datas['subids']
    datas_mul = datas['mul']
    datas_mulids = datas['mulids']
    datas_divi = datas['divi']
    datas_diviids = datas['diviids']


@pytest.fixture(autouse='true')
def testcalc():
    # 开始计算
    print("开始计算")
    yield
    # 结束计算
    print("计算结束")


@pytest.fixture()
def get_calc():
    # 获取计算器实例
    calc = Calc()
    return calc

# 获取add的值
@pytest.fixture(params=datas_add,ids=datas_addids)
def get_datas_add(request):
    datas_add = request.param
    yield datas_add

# 获取sub的值
@pytest.fixture(params=datas_sub,ids=datas_subids)
def get_datas_sub(request):
    datas_sub = request.param
    yield datas_sub

# 获取mul的值
@pytest.fixture(params=datas_mul,ids=datas_mulids)
def get_datas_mul(request):
    datas_mul = request.param
    yield datas_mul

# 获取divi的值
@pytest.fixture(params=datas_divi,ids=datas_diviids)
def get_datas_divi(request):
    datas_divi = request.param
    yield datas_divi