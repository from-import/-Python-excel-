import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体为SimSun（宋体）
font = {'family': 'SimHei', 'size': 8}
# 设置全局字体
plt.rc('font', **font)
plt.rcParams['axes.unicode_minus'] = False  # 禁用Unicode负号，使用标准负号字符

# 读取销售量数据
data = pd.read_excel("Combined_Single_Sum.xlsx")

# 提取销售量数据
sales_data = data.iloc[:, 1:]  # 假设销售量数据从第二列开始，第一列是单品编码

# 计算每个商品的总销售量
data["总销售量"] = sales_data.sum(axis=1)

# 选择总销售量排前50的商品
top_50_data = data.nlargest(15, "总销售量")

# 提取销售量数据（仅包括排前50的商品）
sales_data_top_50 = top_50_data.iloc[:, 1:-1]  # 去除第一列单品编码和最后一列总销售量

# 计算Spearman秩相关系数
spearman_corr, _ = spearmanr(sales_data_top_50, axis=1)

# 读取单品编码到单品名称的映射数据
code_to_name_data = pd.read_excel("data1.xlsx")

# 创建单品编码到单品名称的字典映射
code_to_name = dict(zip(code_to_name_data["单品编码"], code_to_name_data["单品名称"]))

# 创建相关性热力图，选择不同的颜色映射
plt.figure(figsize=(10, 8))

# 将单品编码替换为单品名称
product_names = top_50_data["单品编码"].map(code_to_name)

sns.heatmap(spearman_corr,cmap = "plasma", xticklabels=product_names, yticklabels=product_names, annot=False)

plt.title("Spearman相关系数热力图（总销售量排前15的商品）")
plt.xlabel("单品名称")
plt.ylabel("单品名称")
plt.show()
