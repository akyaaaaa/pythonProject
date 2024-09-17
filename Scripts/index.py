import pandas as pd


def sanitize_class_name(name):
    # 清洗类名，使其符合 Python 的命名规则
    return ''.join([part.capitalize() for part in name.split()])


def format_attribute_value(value):
    # 将属性值格式化为有效的 Python 表达式
    if isinstance(value, str):
        # 如果值已经是字符串，则直接返回
        return value
    else:
        # 如果不是字符串，则尝试将其转换为字符串
        return repr(value)


def create_python_class_file(class_name, buzhou, jieguo,mudi):
    # 清洗类名
    class_name = sanitize_class_name(class_name)

    # 格式化属性值
    buzhou = format_attribute_value(buzhou)
    jieguo = format_attribute_value(jieguo)
    mudi = format_attribute_value(mudi)

    # 创建类的基本结构
    class_content = f"""\
\"\"\"\
测试目的:
{mudi}
操作步骤:
{buzhou}
------------------------------
预期结果:
{jieguo}
\"\"\"\

import pytest


class {class_name}:
    def setup_class(self):
        print("----------类前置条件---------")

    def test_steps(self):
        print("我是核心步骤")
        
    def teardown_class(self):
        print("----------类后置条件---------")
    
    
# 示例对象创建
if __name__ == '__main__':
    pytest.main()
"""

    # 写入文件
    with open(f"{class_name}.py", "w", encoding="utf-8") as file:
        file.write(class_content)


def main():
    # 假设 Excel 文件名为 'example.xlsx'，并且有一个名为 'Sheet1' 的工作表
    excel_file = 'example.xlsx'
    sheet_name = 'Sheet1'

    # 读取 Excel 文件，跳过第一行
    df = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=0, engine='openpyxl')

    # 遍历 DataFrame 的每一行
    for index, row in df.iterrows():
        class_name = row.iloc[12]  # 使用 .iloc[] 进行基于位置的索引
        buzhou = row.iloc[7]
        jieguo = row.iloc[8]
        mudi = row.iloc[6]

        # 创建对应的 .py 文件
        create_python_class_file(class_name, buzhou, jieguo,mudi)


if __name__ == '__main__':
    main()