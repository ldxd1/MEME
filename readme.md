MEME: The 19 nCov virus project

基于数学模型和优化方法建立武汉病毒的传染病学模型预测

患病人数资料由这个项目获取
https://github.com/globalcitizen/2019-wuhan-coronavirus-data

由于网络原因，同步如下：
https://gitee.com/victordefoe/wuhan-coronavirus-data/

可以git clone 上述链接 到19_nCoV_data文件夹下


感谢 Wang Peng, Northwestern Polytechnical University 的贡献

### requirments
（ 用使的Python 平台一些开源包）
geatpy
pandas
matplotlib
numpy
json


# 理论  
基于SEIR 模型
改进

基于SEIR基础上，做了如下考虑：
* 考虑病毒在潜伏期也具有相同传染性
* 考虑确诊患者在医院进行了较好的隔离，这部分患者比率传染性配比了隔离系数
* 取潜伏期平均日7日计算
* 使用带参数的s型函数拟合传染率的下降规律，来模拟日益完善的防疫力量
* 用演化计算优化拟合参数，结果显示目前趋势相当于模型发病前36天的趋势

# 论文
技术细节和相关论文说明报告已经更新，请看'docs/report.pdf'


