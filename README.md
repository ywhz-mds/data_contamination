# data_contamination
LLM&amp;NLG Project
# Perplexity
在初步尝试中，通过计算模型对valid.json里所有文本的困惑度，得到统计分布后发现，可以通过模型困惑度来区分数据污染。
# my_data_contamination
通过对文本截断，让模型进行补全，比较补全后的句子与原句子的相似度来判断句子是clean还是dirty，评测指标主要用SequenceMatching,余弦相似度
# calculate_score
计算置信区间，结果为clean=(14.405536295975855, 15.229970502540832)
dirty=(12.263873552658106, 13.088307759223083)
其实是可以区分的
# new_valid
把label变成0和1，方便auc_score的计算
# auc_score
计算auc_score
# probability
打分，思路很简单，就是分成小于10，10-15，15-20，20-30，30以上五个分数段，直接算概率
# min-K
一种新的尝试，具体思路文档中有伪代码
# BLEURT & ROUGE指标计算
由作业readme的第四篇论文中提到的指标，对数据进行测算，目前只测算了压缩到原来文本长度1/4后，输出文本和原文本之间的指标结果

可以通过文件中输出发现基本没有效果，0.5左右
