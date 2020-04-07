'''
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.
'''

# time: o(n) 
# space: o(n)
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # Create tree
        tree = collections.defaultdict(list)
        for i,parent in enumerate(ppid):
            tree[parent].append(pid[i])
            
        # traversal subtree
        result = []
        stack = [kill]
        while stack:
            cur_node = stack.pop()
            result.append(cur_node)
            if cur_node in tree:
                stack += tree[cur_node]
                
        return result