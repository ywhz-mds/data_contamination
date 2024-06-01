import json
import numpy as np
from scipy import stats
import torch
import torch.nn.functional as F


data_path='min_K/sum_min_k_prob_d.json'
with open(data_path, 'r',encoding = 'utf-8') as f:
    data = json.load(f)

p_list = []
for item in data:
    p_list.append(item['min_k_prob'])

min_val=np.min(p_list)
max_val=np.max(p_list)
result=[]
for i in range(len(p_list)):
    result.append((max_val-p_list[i])/(max_val-min_val))
final_score = []
for sample in data:
    final_score.append({
        'text':sample['text'],
        'score':result.pop(0)
    })


with open('min_K/min_k_final_score1.json', 'w',encoding = 'utf-8') as f:
    json.dump(final_score, f, ensure_ascii=False, indent=4)