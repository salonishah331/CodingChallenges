'''

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

'''


class HitCounter(object):

    def __init__(self, next=None, prev=None, data=None):
#         create array of size 300
        self.counter = [[0,i+1] for i in range(300)]
       
    
    def hit(self, timestamp):
#        add frequency of hits and time of hit into array
#        use mod to save space
        time = (timestamp - 1)%300
        if self.counter[time][1] == timestamp:
            self.counter[time][0] += 1
        else:
            self.counter[time][0] = 1
            self.counter[time][1] = timestamp
        
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        

    def getHits(self, timestamp):
#         count number of hits 300 seconds before timestamp
        numHits = 0
        for x in self.counter:
            f, t = x[0], x[1]
            if timestamp - t < 300:
                numHits += f
        return numHits

   

