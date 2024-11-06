'''
we are given an int numCourses, which means there are courses labeled 
0 to numCourses - 1
we are also given an array of preRequistes
we have to determine if we can complete the courses from the preReqs
PreReq: [0, 1] this means to complete course 0, we have to complete course 1
and since course 1 has no preReqs, we can complete 1, and if we can complete course 1, we can complete course 0

preReq: [[0, 1], [1, 0]] 
this is impossible, because to complete course 0 need to complete course 1,
but to complete course 1 we need to complete course 0

So what we could do is have an adjacency list, a preMap 
that maps the course to its list of preReqs 
and for each course, we can run dfs on the course, and then on its preReqs

numCourses = 5
preReq = [ [0, 1], [0,2] , [1,3], [1,4] , [3,4]]
PreMap:
0 -> [1, 2]
1 -> [3, 4]
2 -> []
3 -> [4]
4 -> []
Courses 2 and 4 have no preReqs
and to avoid an impossible loop, as we run dfs on a course, we will add it to a visitSet
if we ever come across the same course while visiting it along our dfs path, theres a loop
and its impossible so return False

so we start dfs on course 0
see its preReqs [1,2], run dfs on 1
1 has preReq[3,4] run dfs on 3
3 has preReq[4], run dfs on 4
4 has no preReq = [], so it can be completed, so pop back up to 3
now that we know 4 can be completed, that means 3 can be completed
so we can update 3 to have an empty preReq
and since we completed 3 we can pop back up to 1, and take out 3 from its list
then run dfs on 4 from 1 but again empty so pop back up and now 1's preReqs are empty
and so on

we will run dfs on all courses
if any course returns false, whole thing is false

Time Complexitiy: O(n + p)  n= # of nodes , p = # of preReqs
We are visiting every single node and every single preReq

'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # initial map setup, set all courses to have [] preReq
        preMap = { i: [] for i in range(numCourses)}

        # map courses to its preReqs
        for crs, pre in prerequisites:
            preMap[crs].append(pre) # prerequistes: [0, 1] course 0 has a preReq of 1

        visitSet = set()
        # run dfs on all courses 
        def dfs(crs):
            # if already visited while visiting, theres a loop
            if crs in visitSet:
                return False
            
            # if course has no preReq, it can be completed so return True
            if preMap[crs] == []:
                return True
            
            #anything else, we can start visitng this course
            visitSet.add(crs)
            # now for this course, we want to go through all of its preReqs
            # to see if it can be completed, if any returns False, we reutnr False
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # now we are done visiting, so we can remove from visitSet
            visitSet.remove(crs)
            #after we're done visiting, that means course can be completed
            # so the preReq map can be updated to just be empty in case we try to visit again later on
            # visit again on a new path not same path
            preMap[crs] = []
            return True

        # we also want to run dfs on every single course
        # if any return False, if any course cant be completed, we have to return False
        # since we cant finish all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
