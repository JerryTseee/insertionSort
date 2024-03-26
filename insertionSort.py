"""
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons.
But it is efficient enough to solve small number of elements
"""
def insertion(n):
    for i in range(1,len(n)):
        key = n[i]
        j = i - 1
        while n[j] > key:
            #move every bigger than key elements to the right
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key#finally insert the key
    return n

print(insertion(n=[1,23,4,43,2,42]))