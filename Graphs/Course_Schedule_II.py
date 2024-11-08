'''
so we are given total of numCourses, courses are labeled 0 to numCourses - 1,
and a list of preRequistes, that tell us what courses we need to do complete to complete course A
we have to return the order of the courses u need to take to finish all the courses
if its impossible, return []

so similar to Course Schedule I
we will have an adjacncey list, a preReq map 
that maps the courses to their list of preReqs
run dfs on each course and on their preReqs

and as we are done exploring course, we will add them to the output
we dont want to add the same node to the output twice
so we will have a visitSet, if we arleady visited, just return True

and we also have to keep trrack of cycles
if on our path when going through the preReqs, we come across the same course twice
theres a loop, and its impossible, so return False

if our dfs ever returns False, we return an empty array, otherwise return the output array

Time Complexity: O(E + P) = O(n + p) = # of courses + # of preReqs

'''



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}
        #append the reqs to the courses in the map
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        visit, cycle = set(), set()
        output = []
        
        # each course has 3 states
        # visited -> its already in the output array, or visited, return True
        # visiting -> if in the cycle on the path of our dfs, theres a loop, return False
        # unvisited -> not in cycle or visit Set, so we can explore
        def dfs(crs):
            # in cycle, so visiting same course twice on same path
            if crs in cycle:
                return False
            
            # already in output array
            if crs in visit:
                return True

            cycle.add(crs)
            # go through all of the preReqs of the course, and run dfs
            # if dfs returns, False, we return False
            for pre in preReq[crs]:
                if dfs(pre) == False:
                    return False
            
            # if we get through the entire loop, we can take off the course from the cycle
            cycle.remove(crs)
            # add course to visited, so we dont add to output array twice
            visit.add(crs)
            # done with the course, so add to output array
            output.append(crs)
            return True
        
        # we want to run dfs on all the courses initially
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return output            
