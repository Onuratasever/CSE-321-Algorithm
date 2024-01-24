def mostDiscount(setOfStores):
    subsets = [set()]
    findAllSubsets(subsets, setOfStores)
    max = 0
    maxSet= set()
    for item in subsets:
        a = calc_dscounts(item)
        if(a > max):
            max = a
            maxSet = set(item)
    print(subsets)
    
def calc_dscounts(subsets): #It does something

		
    
def findAllSubsets(subsets, setOfStores):
	if len(setOfStores) != 0:
		element = setOfStores.pop()
		findAllSubsets(subsets, setOfStores)
		newset = []
		for item in subsets:
			temp_item = set(item)
			temp_item.add(element)
			newset.append(temp_item)
		subsets.extend(newset)
  
seta = {'a','b','c','d'}
mostDiscount(seta)