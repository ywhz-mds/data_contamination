# data_contamination
LLM&amp;NLG Project
# Perplexity
在初步尝试中，通过计算模型对valid.json里所有文本的困惑度，得到统计分布后发现，可以通过模型困惑度来区分数据污染。
# my_data_contamination
通过对文本截断，让模型进行补全，比较补全后的句子与原句子的相似度来判断句子是clean还是dirty，评测指标主要用SequenceMatching,余弦相似度
