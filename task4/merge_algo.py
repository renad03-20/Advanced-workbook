# description: merge sort algorithm
def merge_sorted_list(list1, list2):
    i, j = 0, 0 
    merged = []

    # merge te two list together
    while i < len (list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # adds the remaining elements to the merged list
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# merging all the sequences
def merge_all(sequnces):
    while len(sequnces) > 1:
        merged_sequnces = []

        # merging by pairs
        for i in range(0, len(sequnces), 2):
            if i + 1 < len(sequnces):
                merged = merge_sorted_list(sequnces[i], sequnces[i + 1])
                merged_sequnces.append(merged)
            else:
                merged_sequnces.append(sequnces[i])

        #updating the sequence
        sequnces = merged_sequnces

    return sequnces[0]

# main function
if __name__ == "__main__":
    
    #testing 
    sequnces = [
    [1, 3, 5, 7], 
    [2, 4, 6, 8], 
    [0, 9, 10, 11]
    ]

    result = merge_all(sequnces)
    print(f'Merged sequnces: {result}')