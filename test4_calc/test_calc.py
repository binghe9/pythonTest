import allure
import pytest

@allure.feature('测试计算器')
class TestCalc:

    # 加法测试用例
    @pytest.mark.run(order=1)
    @allure.story('测试加法')
    def test_add(self,get_calc,get_datas_add):
        result = get_calc.add(get_datas_add[0],get_datas_add[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_add[2]

    # 减法测试用例
    @pytest.mark.run(order=2)
    @allure.story('测试减法')
    def test_sub(self,get_calc,get_datas_sub):
        result = get_calc.sub(get_datas_sub[0],get_datas_sub[1])
        assert result == get_datas_sub[2]

    # 乘法测试用例
    @pytest.mark.run(order=3)
    @allure.story('测试乘法')
    def test_mul(self,get_calc,get_datas_mul):
        result = get_calc.mul(get_datas_mul[0],get_datas_mul[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_mul[2]

    # 除法测试用例
    @pytest.mark.run(order=4)
    @allure.story('测试除法')
    def test_divi(self,get_calc,get_datas_divi):
        if (get_datas_divi[1] != 0):
            result = get_calc.divi(get_datas_divi[0],get_datas_divi[1])
        else:
            print('除数不能为0!')
            result = '除数不能为0'
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_divi[2]
