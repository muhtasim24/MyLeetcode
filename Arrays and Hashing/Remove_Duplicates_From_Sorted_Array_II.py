'''
so we are given an integer array nums in sorted order
we have to remove some duplicates IN-PLACE 
we only want any element to appear at most twice
the order should be the same

so since we are doing in-place, we want the first k elements to be have the correct elements
have all elements appear only twice, and the extra will be after k elements
so how can we keep track of how many times we see an element
we can use a hashmap
and we will use k to set places, and an iterator i

the hashmap will map the element -> count of element
when we want to "remove" an element, we will set index k with whatver value i is at

when we come across an element with i, lets say hashmap[i] == 2, 
since we only want each element to appear twice, thats when we set nums[k] = i

but if hashmap[i] < 2, we can update our map count
hashmap[i] += 1
incrmenet k 

ex: [1, 1, 1, 2, 2, 3]
     k
     i
so we visit 1, first we should check if its in the map, if not we add it
map: {1 : 1}
increment k and i
ex: [1, 1, 1, 2, 2, 3]
        k
        i
i is at 1 again, check if in map
it is, so now since its arleady in the map, we check if map[i] < 2
if it is under 2, we can increment the count again
update k and i
ex: [1, 1, 1, 2, 2, 3]
           k
           i
map: {1 : 2}
now i is at 1 again, check if in map, yes 
if map[i] < 2, we increment but if its not, we cant do anything ,
SO we only check if its in the map, and if count is under 2
ex: [1, 1, 1, 2, 2, 3]
           k
              i
map: {1 : 2, }, so everytime we add a value to the map, we can set nums[k] = i
and then add to map
so we are visiting 2, its not in the map, we add it
and set nums[k] = nums[i]
so now we have 
ex: [1, 1, 2, 2, 2, 3]
              k
                 i
map: {1 :2 , 2: 1}
2 in map, but under 2, update map count, set nums[k] = nums[i], and incremnt k
ex: [1, 1, 2, 2, 2, 3]
                 k
                    i
map: {1 :2 , 2: 2}
3 not in map. add it, set nums[k] = nums[i], and update k
ex: [1, 1, 2, 2, 3, 3]
                    k
                    i
and algo endds here since i has reached the end

so what we learned from the runThrough:
iterate through the array, nums
if nums[i] is in the map, we check if under 2, if it is
update count in map, and set nums[k] = nums[i]

but if not in map, we also add to map, increment k and set nums[k]
only time we dont set or increment k, when map[i] == 2, map[i] < 2 is not true
return k

'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        mapDup = {}

        for i in range(len(nums)):
            # 2 cases, we touch the map
            # if not in the map, or count under 2
            # check if not in the map, add it to the map
            if nums[i] not in mapDup:
                mapDup[nums[i]] = 1
                nums[k] = nums[i]
                k += 1
            # so if we dont enter the first condition, that means, it is in the map
            # so we can just check if the count in the map, is under 2
            elif mapDup[nums[i]] < 2:
                mapDup[nums[i]] += 1
                nums[k] = nums[i]
                k += 1
            # and we do nothing if, count is 2 or higher, so k never updates, i keeps going
        return k
