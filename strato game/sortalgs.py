import time

# Insertion Sort

def insertion_sort(the_list):
    for i in range(1, len(the_list)):
        for j in range(i - 1, -1, -1):
            if the_list[j] > the_list[j + 1]:
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]
            else: break
            time.sleep(0.02)
        time.sleep(0.02)

# Selection Sort

def selection_sort(the_list):
    for i in range(0, len(the_list)):
        minIndex = i
        for j in range(i, len(the_list)):
            if the_list[j] < the_list[minIndex]: minIndex = j
            time.sleep(0.02)
        the_list[i], the_list[minIndex] = the_list[minIndex], the_list[i]
        time.sleep(0.02)

# Bubble Sort

def bubble_sort(the_list):
    for i in range(0, (len(the_list) - 1)):
        for j in range(0, (len(the_list) - 1 - i)):
            if the_list[j] > the_list[j + 1]:
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]
                time.sleep(0.02)
        time.sleep(0.02)
            
# Merge Sort

def merge_sort(the_list):
    merge_sort_two(the_list, 0, (len(the_list) - 1))
    
def merge_sort_two(the_list, first, last):
    time.sleep(0.02)
    if first < last:
        middle = (first + last) // 2
        merge_sort_two(the_list, first, middle)
        merge_sort_two(the_list, (middle + 1), last)
        merge(the_list, first, middle, last)
        
def merge(the_list, first, middle, last):
    L =  the_list[first : (middle + 1)]
    R = the_list[(middle + 1) : (last + 1)]
    L.append(999999999)
    R.append(999999999)
    i = j = 0
    for k in range(first, (last + 1)):
        if L[i] <= R[j]:
            the_list[k] = L[i]
            i += 1
        else:
            the_list[k] = R[j]
            j += 1
        time.sleep(0.02)
            
# Quick Sort

def quick_sort(the_list):
    quick_sort_two(the_list, 0, (len(the_list) - 1))
                   
def quick_sort_two(the_list, low, high):
    time.sleep(0.02)
    if low < high:
        p = partition(the_list, low, high)
        quick_sort_two(the_list, low, p - 1)
        quick_sort_two(the_list, p + 1, high)

def get_pivot(the_list, low, high):
    mid = (low + high) // 2
    pivot = high
    if the_list[low] < the_list[mid] < the_list[high]:
            pivot = mid
    elif the_list[low] < the_list[high]:
            pivot = low
    return pivot

def partition(the_list, low, high):
    pivot_index = get_pivot(the_list, low, high)
    pivot_value = the_list[pivot_index]
    the_list[pivot_index], the_list[low] = the_list[low], the_list[pivot_index]
    border = low

    for i in range(low, (high + 1)):
        if the_list[i] < pivot_value:
            border += 1
            the_list[i], the_list[border] = the_list[border], the_list[i]
        time.sleep(0.02)
    the_list[low], the_list[border] = the_list[border], the_list[low]
    
    return (border)
