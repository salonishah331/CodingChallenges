
'''
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

'''


def minAvailableDuration(self, slots1, slots2, duration):

        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i = 0
        j = 0
        
        while i < len(slots1) and j < len(slots2):
            head = max(slots1[i][0], slots2[j][0])
            tail = min(slots1[i][1], slots2[j][1])
            if head + duration <= tail:
                return [head, head+duration]
            
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        return []