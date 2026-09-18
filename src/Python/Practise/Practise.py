"""Python Practise with claude"""


#List (like List<String>)

fruits = ['apple', 'banana','grapes']
print("fruits : ", fruits)
fruits.append('mango')
print("fruits append : ", fruits)
print("fruits oth index : ", fruits[0])

#Dict (Like Map<String,Integer>)

scores = {"Harsh": 90, "Anu": 95}
print("scores : ", scores)
print("scores harsh : ", scores["Harsh"])
scores["Mom"] = 70
print("scores Mom : ", scores["Mom"])

#Set (like Set<String>)
#sets doesent have any index and they are unordered so no gurantee of order.

uniqueNames = {"Harsh", "Anu" , "Mom"}
print("UniqueNames : ", uniqueNames)
uniqueNames.add("Raj")
print("UniqueNames raj : ", uniqueNames)
uniqueNames.add("Harsh")
print("UniqueNames harsh duplicate : ", uniqueNames)


# Loops - same idea as Apex for-each

for f in fruits:
    print("fruits loop : ", f)



"""Write a Python function that takes a list of numbers and returns a dict where 
keys are the numbers and values are how many times each number appears — 
i.e., build a frequency map, exactly like you'd do with Map<Integer, Integer> in Apex when counting duplicates."""

def count_frequency(nums):
        dNum = {}
        if(nums is not None):
              for k in nums:
                dNum[k] = dNum.setdefault(k,0) + 1


        return dNum   
    
print("count_frew : ", count_frequency([1, 2, 2, 3, 3, 3]))

##however a direct way of doing this just for our info:

from collections import Counter
count_frequency = Counter([1,2,2,3,3,3])
print("count_frew collections : ", count_frequency)



#Tuples

locations = {}
locations[(3,4)] = "treasure" #works cuz its a tuple
print("locations tup : ", locations)

#but lists cant be dict keys see

#locations[[3,4]] = "tresure"
#print("locations list : ", locations)  #TypeError: unhashable type: 'list'

#so this is also one good use case of tuple

#multiple return values

def min_max(nums):
     return min(nums) , max(nums)


print("min_max : ", min_max([3,2,1,5,9]))

#This "unpacking" syntax shows up constantly in DSA solutions (e.g., swapping: a, b = b, a).
low , high = min_max([3,2,1,5,9])


tup1 = 3,4,5,3,3,9,1,2,
print("tup1 : ", tup1.count(3)) ## 3 — how many times 3 appears

#unpacking works with any iterable (list, tuple, string, even the keys of a dict)
#list unpacking
a,b,c = [10,20,30]
print(a,b,c)

#string unpacking
x,y,z = "abc"
print(x,y,z)

#Swapping - the classic use case
a,b = 7,9
a,b = b,a
print(a,b)


##Extended unpacking with * — 
#useful when you don't know/care about the exact count, common in DSA when you want "first element, then the rest":

first, *rest = [1,2,3,4,5]
print(first)
print(rest)

*rest, last = [1,2,3,4,5]
print(rest)
print(last)

#This *rest pattern shows up a lot in linked-list and array problems (e.g., "process head, recurse on the rest").

"""Write a function that takes a list of (x, y) coordinate tuples 
and returns the set of coordinates that appear more than once in the list 
(i.e., duplicates) — this combines what you just learned about tuples-as-hashable-keys 
with the frequency-counting pattern from before."""

def count_duplicates(tups):
    print(tups)
    count_dupli_frequency = Counter(tups)
    dSet = set()
    for coord , cnt in count_dupli_frequency.items():
         
        if cnt > 1: 
            print(coord)
            dSet.add(coord)
    
            
    return dSet

print("here : ", count_duplicates(((1,2),(2,3),(1,2),(6,7),(2,3))))



"""You've now independently built the "count then filter" pattern — this is huge in DSA: count everything with a hash map (Counter/dict), then filter based on a condition. This exact shape reappears in: majority element, anagram grouping, top-K frequent elements, and dozens of interview problems."""


#if we would have applied set comprehension
#then all over in a single line

def count_duplicates2(tups2):
    count_dupli_frequency2 = Counter(tups2)
    return {coord for coord, cnt in count_dupli_frequency2.items() if cnt > 1}

#Same logic, no explicit dSet = set() / .add() — the {... for ... if ...} syntax does both.

#let me try this comprehension on my own

def test1(t1):
    sSet = set()
    for s in t1:
        if s is not None:
            sSet.add(s)

    return sSet

print("test1 : ", test1([1,2,3,4,8]))         


def test2(t2):
    print(t2)
    test2Set = set()
    return {s for s in t2 if s is not None}

print(test2([1,2,3,4,8]))  



############### DSA ##################

#DSA Pattern #1: Two Sum (the most common interview opener, 
#and the foundation of hash-map-based problems)


## hashing , important----
#python has built-in hash() function

print("hashing : ", hash("Harsh"))  # 4895245337058191612  some large numb
print(hash(42)) # 42  (small integers often hash to themselves)
print(hash((1,2)))   # a large number — tuples are hashable, as you learned , -3550055125485641917

#but lists are not hashable
#print(hash([1,2])) #TypeError: unhashable type: 'list'


#Seeing why it makes lookup fast — a mini side-by-side

#list vs set

import time

big_list = list(range(1_000_000))
big_set = set(range(1_000_000))

start = time.time()

999_999 in big_list # has to scan up to a million items
elaspes_ms = (time.time() - start) * 1000
print("list lookup : " , elaspes_ms)

start = time.time()
999_999 in big_set # hash tells it exactly where to look
elaspes_ms = (time.time() - start) * 1000
print("set lookup : ", elaspes_ms)

"""Now it's readable at a glance: list lookup ≈ 8.93 ms, 
set lookup ≈ 0.0012 ms — roughly 7500x faster for the set, same data size, 
same check. That gap is the entire reason hashing exists as a technique, and 
it's what you'll lean on constantly in DSA."""


#now
# List look up Time complexity is O(n) , as we had to check 
#every element one by one until we find the match

#Space complexity - extra for the operation itself so its O(1)

#Set lookup - Time was O(1) as hash function knwe where to look directly
#so doesent matte if set has 1 or 1mn items
#Space - extra for the operation itself O(1) same reasoning






"""DSA Pattern #1: Two Sum (the most common interview opener, 
and the foundation of hash-map-based problems)

Problem: Given a list of numbers and a target, 
return the indices of the two numbers that add up to the target. 
Assume exactly one solution exists, 
and you can't use the same element twice.

python
nums = [2, 7, 11, 15]
target = 9
# 2 + 7 = 9, so answer is [0, 1] (their indices)"""


#note - use enumerate() instead of .index()
#enumerate() — get index + value together while looping

nums = [2, 7, 11, 15]

for idx , val in enumerate(nums):
    seen = {}
    print("enumerate index: ", idx,"enumerate val : ", val)
    seen[val] = idx  #this is like mapVar.put(key, value) in Apex,

def two_sum(numbs , target):
    seen = {}
    for idx,val in enumerate(numbs):
        
        if (target - val) in seen:
            return [seen[target - val] , idx]

        seen[val] = idx  #this is like mapVar.put(key, value) in Apex,


#print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3,3], 6))

##that's a fully correct, O(n) time / O(n) space solution to Two Sum


#quick reverse string
s = "Hello World"
print("rev st : ", s[::-1])




#####Write a function that checks whether a given string 
# is a palindrome (reads the same forwards and backwards), 
# ignoring case and spaces.

#strings r immutable

def is_palindrom(s):
    s = s.lower().replace(" ","")
    return s[::-1] == s

print(is_palindrom("racecar"))                          # True
print(is_palindrom("A man a plan a canal Panama"))       # True
print(is_palindrom("hello"))                              # False




##Valid Anagram

#Problem: Given two strings s and t, 
# return True if t is an anagram of s 
#(uses exactly the same letters, same counts, 
# just rearranged), otherwise False.


#approach 1 - sort and compare
#Sort approach (what you wrote): time complexity is O(n log n) — sorting dominates the cost.
def is_anagram(s,t):
    s = s.lower().replace(" ","")
    t = t.lower().replace(" ","")

    return sorted(s) == sorted(t) 


print(is_anagram("listen", "silent"))   # True  — same letters rearranged
print(is_anagram("rat", "car"))          # False — different letters
print(is_anagram("aacc", "ccac"))        # False — same letters, but wrong counts (three c's vs two)



#approach 2 - Frequency map (Counter)

from collections import Counter

def is_anagram2(s,t):
    s = s.lower().replace(" ","")
    t = t.lower().replace(" ","")

    return Counter(s) == Counter(t)


print(is_anagram("listen", "silent")) 

"""
VALID ANAGRAM — two approaches

Approach 1: Sort-and-compare
    sorted(s) == sorted(t)
    Time:  O(n log n)  — sorting dominates
    Space: O(n)         — sorted() creates new lists

Approach 2: Frequency map (BETTER — use this one)
    Counter(s) == Counter(t)
    Time:  O(n)   — one pass per string, no sorting
    Space: O(n)   — but often less in practice (only unique chars stored)

RULE OF THUMB: comparing "same elements/counts" between two collections?
Reach for a hash map (dict/Counter) before sorting — usually faster.
"""





##Contains Duplicate

#Problem: Given a list of integers, return True 
# if any value appears at least twice, 
#False if every element is distinct.

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:  #1,2,3,
            return True
        seen.add(num)

    return False


print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))   # expect False






##Group Anagrams

#Problem: Given a list of strings, group the anagrams together. 
# Return a list of groups (each group is a list of strings 
# that are anagrams of each other).


#Time complexity: O(n · k log k)
#Space complexity: O(n · k)


def group_anagrams(words):
    groups = {} #dict
    #result = groups.setdefault("aet",[]).append("tea")
    #result = groups.setdefault("aet",[]).append("eat")
    #print("res : ", result)
    #print("grp : ", groups)

    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key,[]).append(word)
        print("ker : ", key)
    return list(groups.values())    
              

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))