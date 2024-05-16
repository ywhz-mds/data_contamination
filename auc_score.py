from sklearn.metrics import roc_auc_score
import json
with open('new_valid.json','r',encoding='utf-8') as f:
    valid = json.load(f)
with open('final_score.json','r',encoding='utf-8') as f:
    predict = json.load(f)
labels=[]
predictions=[]
for sample in valid:
    label=sample['label']
    labels.append(label)
for sample in predict:
    prediction=sample['score']
    predictions.append(prediction)
auc=roc_auc_score(labels, predictions)
print("AUC on validation set:", auc)