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
# minmax
通过minmax来打分
# BLEURT & ROUGE指标计算
由作业readme的第四篇论文中提到的指标，对数据进行测算，目前只测算了压缩到原来文本长度1/4后，输出文本和原文本之间的指标结果

可以通过文件中输出发现基本没有效果，0.5左右

# Train_Classifier
*检测方法不限。可以考虑使用模型对于每条数据的困惑度（[perplexity](https://huggingface.co/docs/transformers/perplexity)）、对比模型在同义改写后的文本的行为是否有显著差异、以模型的隐层和文本为特征训练分类模型、让模型续写等等。*

对作业readme提到的**训练分类模型**进行尝试，目前选用了**gaunernst/bert-medium-uncased**这个预训练模型，数据是将文本输入**detected-model**后得到output，选取*output*的最后一层*hidden state*经过pooling和维度转换（未来适配选用模型）构成。

结果发现效果依旧不行，输出效果不太稳定且最终分类AUC值也最多只能在0.58左右。

考虑是由于训练数据不好导致的，可能存在：
- hidden states的向量化数据特征难以提取，或不具有普适性
- 尚未和文本特征结合来构造数据，因为没想好怎么构建，或许结合文本本身特征会好一点
- 容易过拟合，用训练数据作为test-data训练50 epochs 可以达到AUC score 0.91，但对于没见过的数据AUC score为0.5上下波动
