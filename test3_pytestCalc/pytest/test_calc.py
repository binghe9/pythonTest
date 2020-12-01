import pytest
import yaml

from test3_pytestCalc.calc import Calc

# 获取yaml数据
with open('./data.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)

class TestCalc:
    # 开始计算
    def setup_class(self):
        self.calc = Calc()
        print("开始计算")
    # 结束计算
    def teardown_class(self):
        print("计算结束")

    # 加法测试用例
    @pytest.mark.parametrize('a,b,expect',datas['add'],ids=datas['addids'])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect

    # 减法测试用例
    @pytest.mark.parametrize('a,b,expect',datas['sub'],ids=datas['subids'])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect

    # 乘法测试用例
    @pytest.mark.parametrize('a,b,expect',datas['mul'],ids=datas['mulids'])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        if isinstance(result,float):
           result = round(result,2)
        assert result == expect

    # 除法测试用例
    @pytest.mark.parametrize('a,b,expect',datas['divi'],ids=datas['diviids'])
    def test_divi(self,a,b,expect):
        if (b != 0):
            result = self.calc.divi(a,b)
        else:
            print('除数不能为0!')
            result = '除数不能为0'
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect