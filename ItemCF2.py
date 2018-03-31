import json
import sys

user = sys.argv[1]
k = int(sys.argv[2])
n = int(sys.argv[3])
def Recommend(user,K=k,N=n):  
		#print user
		with open('train.json', 'r') as f:
			train = json.load(f)
		#print train
		with open('metrix.json', 'r') as f:
			W = json.load(f)
		#print W
		rank = dict()  
		action_item = train[user]     
		for item,score in action_item.items():  
			for j,wj in sorted(W[item].items(),key=lambda x:x[1],reverse=True)[0:K]:  
				if j in action_item.keys():  
					continue  
				rank.setdefault(j,0)  
				rank[j] += score * wj  
		#print rank.items()
		return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N]) 

recommedDic = Recommend(user)
print json.dumps(recommedDic) 
