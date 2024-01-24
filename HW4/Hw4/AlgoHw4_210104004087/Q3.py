def findMaxArea(start_index, end_index, area, tempStart_index, tempEnd_index, temp_sum):
    sum = 0
    current_endIndex= end_index
    index = start_index
    if(index == end_index):
        #print("index == end_index geldi")
        return area[index], end_index, area[index], index, end_index
    
    while(index <= end_index):
        if(area[index] < 0 and index != start_index):
            current_endIndex = index -1
            real_sum, real_endIndex, return_sum, returnStart_index, returnEnd_index = findMaxArea(index, end_index, area, tempStart_index, tempEnd_index, temp_sum)

            if (real_sum > 0):
                sum = sum + real_sum
                current_endIndex = real_endIndex
            if (sum < 0):
                sum = 0
            if (sum > return_sum):
                temp_sum = sum
                tempStart_index = start_index
                tempEnd_index = current_endIndex
            else:
                temp_sum = return_sum
                tempStart_index = returnStart_index
                tempEnd_index = returnEnd_index

            return sum, current_endIndex, temp_sum, tempStart_index, tempEnd_index
        else:
            sum += area[index]
        index += 1
    if (sum > temp_sum):
        temp_sum = sum
        tempStart_index = start_index
        tempEnd_index = end_index
    #print("returnden önce sum: ", sum, " currenEndIndex: ", current_endIndex, " Temp_sum: ", temp_sum, " tempstart_Index: ", tempStart_index, " tempEdn_index: ", tempEnd_index)
    return sum, current_endIndex, temp_sum, tempStart_index, tempEnd_index


def MaxArea(area):
   sum, current_endIndex, temp_sum, tempStart_index, tempEnd_index = findMaxArea(0, len(area)-1, area, -1, -1, -1)
   return temp_sum, tempStart_index, tempEnd_index
    
def main():

    area = [2, 1, -4, 2, 1, 8, -44, 3, 11, -2, 15, 1]
    sum, start_index, end_index = MaxArea(area)
    print("Max sum is:", sum, "in interval [", start_index, ",", end_index,"]")

main()