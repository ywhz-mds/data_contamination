import json
import numpy as np
from scipy import stats
with open('perplexity.json', 'r',encoding = 'utf-8') as f:
    perplexity_data = json.load(f)
p_list = []
i=0
print(len(perplexity_data))
for item in perplexity_data:
    p_list.append(item['perplexity'])
    if(item['label']=='dirty'):
        print(i)
        break
    i+=1
p_clean=p_list[:i]
p_dirty=p_list[i:1618]
c_mean=np.mean(p_clean)
d_mean=np.mean(p_dirty)
std_clean=np.std(p_clean)
std_dirty=np.std(p_dirty)

confidence_level=0.95

std_error_clean=stats.sem(p_clean)
std_error_dirty=stats.sem(p_dirty)
 
t_critical = stats.t.ppf((1+confidence_level)/2, df=len(p_clean)-1)  # Get the t-critical value*

margin_of_error = t_critical * std_error_clean
lower_bound = c_mean - margin_of_error
upper_bound = c_mean + margin_of_error
print("clean data: mean={}, std={}, std_error={}, margin_of_error={}, confidence_interval=({}, {})".format(c_mean,std_clean,std_error_clean,margin_of_error,lower_bound,upper_bound))
d_lower_bound = d_mean - margin_of_error
d_upper_bound = d_mean + margin_of_error
print("dirty data: mean={}, std={}, std_error={}, margin_of_error={}, confidence_interval=({}, {})".format(d_mean,std_dirty,std_error_dirty,margin_of_error,d_lower_bound,d_upper_bound)) 
