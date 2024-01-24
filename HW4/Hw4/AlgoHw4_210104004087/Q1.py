def findFlawedFuse(fuses, first_index, last_index):
    if first_index > last_index:
        return -1

    mid = (first_index + last_index) // 2

    if fuses[mid] == 0:
        left_value = findFlawedFuse(fuses, first_index, mid - 1)
        if left_value == -1:
            return mid 
        else:
            return left_value
    elif fuses[mid] == 1:
        return findFlawedFuse(fuses, mid + 1, last_index)


def main():
    fuses = [1,1,1,0,0,0]
    
    print(findFlawedFuse(fuses, 0, len(fuses)-1))

main()