from cmath import inf


def find_optimal(users, jobs, processors, comb, sub_comb1):
	sub_comb =[]
		#for i in range(0, len(users)):
	if(len(users) == 0):
		comb.append(sub_comb1)
		sub_comb1 = []
		return sub_comb1
	sub_comb =[]
	temp_users = list(users)
	user = temp_users.pop()	
	for j in range(0, len(jobs)):
		for k in range(0, len(processors)):
			sub_comb.append(user)
			sub_comb.append(jobs[j])
			sub_comb.append(processors[k])
			sub_comb1.append(sub_comb)
			sub_comb = []
			sub_comb1 = find_optimal(temp_users, jobs[:j]+jobs[j+1:], processors[:k]+processors[k+1:], comb, sub_comb1)
	return sub_comb1

def calc_cost(item):
    
def maim():
	users = ["onur",  "salih"]
	jobs = ["job1", "job2"]
	processors = ["p1", "p2"]
	comb = []
	sub_comb1 = []
 
	find_optimal(users, jobs, processors, comb,sub_comb1)
 
	min = float(inf)
	maxSet= set()
	for item in comb:
		a = calc_cost(item)
		if(a < min):
			min = a
			minSet = set(item)
	print(comb)
 
maim()