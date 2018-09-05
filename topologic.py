import collections
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#BFS 

def findOrder1(numCourses, prerequisites):
    dic = {i:set() for i in  range(numCourses)}
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    queue = collections.deque([i for i in dic if not dic[i]])
    count, res = 0, []
    while queue:
        node = queue.popleft()
        res.append(node)    
        count += 1
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                queue.append(i)
    return res if count == numCourses else []

#DFS
def find(numCourses, prerequisites):
    dic = collections.defaultdict(set)
    neigh = collections.defaultdict(set)
    for  i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    stack = [i for i in range(numCourses) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res if not dic else []
        

            