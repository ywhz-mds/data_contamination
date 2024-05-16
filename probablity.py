import json
import numpy as np
from scipy import stats
with open('perplexity.json', 'r',encoding = 'utf-8') as f:
    perplexity_data = json.load(f)
p_list = []
print(len(perplexity_data))
for item in perplexity_data:
    p_list.append(item['perplexity'])
p_clean=p_list[:809]
p_dirty=p_list[809:1618]

#先把valid的标签标为0和1
with open('dataset/valid.json','r',encoding='utf-8') as f:
    valid = json.load(f)
new_valid=[]
for sample in valid:
    if sample['label']=='clean':
        sample['label']=0
    else:
        sample['label']=1
    new_valid.append(sample)
with open('new_valid.json', 'w',encoding = 'utf-8') as f:
    json.dump(new_valid, f, ensure_ascii=False, indent=4)

num_ca=0 #算小于10的clean
num_da=0 #算小于10的dirty

num_cb=0 #算10-15的clean
num_db=0 #算10-15的dirty

num_cc=0 #算15-20的clean
num_dc=0 #算15-20的dirty

num_cd=0 #算20-30的clean
num_dd=0 #算20-30的dirty

num_ce=0 #算30以上的clean
num_de=0 #算30以上的dirty

for i in range(len(p_clean)):
    if p_clean[i]<=10:
        num_ca+=1
    elif p_clean[i]<=15:
        num_cb+=1
    elif p_clean[i]<=20:
        num_cc+=1
    elif p_clean[i]<=30:
        num_cd+=1
    else:
        num_ce+=1

for i in range(len(p_dirty)):
    if p_dirty[i]<=10:
        num_da+=1
    elif p_dirty[i]<=15:
        num_db+=1
    elif p_dirty[i]<=20:
        num_dc+=1
    elif p_dirty[i]<=30:
        num_dd+=1
    else:
        num_de+=1

score_a=num_da/(num_ca+num_da)
score_b=num_db/(num_cb+num_db)
score_c=num_dc/(num_cc+num_dc)
score_d=num_dd/(num_cd+num_dd)
score_e=num_de/(num_ce+num_de)

final_score=[]
for sample in perplexity_data:
    if sample['perplexity']<=10:
        final_score.append(
            {
                'text':sample['text'],
                'score':score_a
            }
        )
    elif sample['perplexity']<=15:
        final_score.append(
            {
                'text':sample['text'],
                'score':score_b
            }
        )
    elif sample['perplexity']<=20:
        final_score.append(
            {
                'text':sample['text'],
                'score':score_c
            }
        )
    elif sample['perplexity']<=30:
        final_score.append(
            {
                'text':sample['text'],
                'score':score_d
            }
        )
    else:
        final_score.append(
            {
                'text':sample['text'],
                'score':score_e
            }
        )

with open('final_score.json', 'w',encoding = 'utf-8') as f:
    json.dump(final_score, f, ensure_ascii=False, indent=4)