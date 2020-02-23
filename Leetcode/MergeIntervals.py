# Merge Intervals:
#     Write a function that takes a list of multiple meetings time ranges and returns a list of condensed ranges
#     Input:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#     Output: [(0, 1), (3, 8), (9, 12)]


def MergeIntervals(times):
    times.sort(key = lambda x : x[0])
    sorted = []

    
    for time in times:
        if time[0] > sorted[-1][1]:
            sorted.append(times)
        else:
            sorted[-1] = (sorted[-1][0], max(time[1], sorted[-1][1]))
    return sorted 
        
