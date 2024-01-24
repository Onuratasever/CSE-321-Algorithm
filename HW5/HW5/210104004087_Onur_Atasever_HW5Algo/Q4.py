def mostDiscount(setOfStores):#Since calc_discount i snot implemented, it will not work correctly, but as you see, it will find max discount and the stores
    subsets = [set()]
    subsets = findAllSubsets(setOfStores)
    max = 0
    maxSet= set()
    for item in subsets:
        a = calc_discounts(item) # According to calc_discount function it finds best discount
        if(a > max):
            max = a
            maxSet = set(item)
    #print(subsets)

    
def calc_discounts(subsets): #It does something
    return 1

def findAllSubsets(stores):
    all_subsets = [[]]  # Initialize with an empty subset
    #Iterates
    for store in stores:
        current_subsets = []
        for subset in all_subsets: # It iterates subsets and adds new items to old sets
            current_subsets.append(subset + [store])
        all_subsets.extend(current_subsets)

    return all_subsets

# Example usage:
store_set = {'a','b','c','d'}
mostDiscount(store_set)