def allPermutations2(mainList, list, newList):
    if len(list) == 0:
        mainList.append(newList.copy())
        #print(newList)
    else:
        for i in range(len(list)):
            newList.append(list[i])
            temp = list.copy()
            temp.remove(list[i])
            allPermutations2(mainList, temp, newList)
            newList.pop()
            
def main():
    list = [1, 2, 3]
    newlist = []
    mainList = []
    allPermutations2(mainList, list, newlist)
    print(mainList)
    min = float(inf)
	maxSet= set()
	for item in mainList:
		a = calc_cost(item)
		if(a < min):
			min = a
			minSet = set(item)

main()