import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# 设置中文字体为SimSun（宋体）
font = {'family': 'SimHei', 'size': 12}
# 设置全局字体
plt.rc('font', **font)
plt.rcParams['axes.unicode_minus'] = False  # 禁用Unicode负号，使用标准负号字符

# 加载数据
data = pd.read_excel('result.xlsx')

# 将销售月份列设置为日期时间索引
data['销售月份'] = pd.to_datetime(data['销售月份'])
data.set_index('销售月份', inplace=True)

# 选择要分析的产品编号列
column_names = data.columns

labels = ['花叶类', '花菜类', '水生根茎类', '茄类', '辣椒类', '食用菌']
i = 0
# 遍历列名
for column_name in column_names:
    product_code = int(column_name)
    product_data = data[product_code]

    # 使用seasonal_decompose进行季节性分解
    decomposition = seasonal_decompose(product_data, model='additive', period=12)

    # 绘制季节性分解图
    plt.figure(figsize=(12, 8))

    # Original Data
    plt.subplot(411)
    plt.plot(product_data, label='原始数据')
    plt.legend(loc='best')
    plt.title(f'产品编号: {labels[i]}')

    # Trend
    plt.subplot(412)
    plt.plot(decomposition.trend, label='趋势')
    plt.legend(loc='best')

    # Seasonal
    plt.subplot(413)
    plt.plot(decomposition.seasonal, label='季节性')
    plt.legend(loc='best')

    # Residual
    plt.subplot(414)
    plt.plot(decomposition.resid, label='残差')
    plt.legend(loc='best')

    plt.tight_layout()

    # 显示图形
    plt.show()

    i += 1
