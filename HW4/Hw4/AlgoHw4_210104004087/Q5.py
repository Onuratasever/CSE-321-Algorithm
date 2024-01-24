def merge_sort(tasks):
    if len(tasks) > 1:
        mid = len(tasks) // 2
        left_half = tasks[:mid]
        right_half = tasks[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                tasks[k] = left_half[i]
                i += 1
            else:
                tasks[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            tasks[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            tasks[k] = right_half[j]
            j += 1
            k += 1

def minAndMaxTasks(tasks):
    merge_sort(tasks)
    return tasks[0], tasks[len(tasks) -1]

def main():
    tasks = [[1, 3], [2, 2], [3, 4], [4, 1]]
    print(minAndMaxTasks(tasks))