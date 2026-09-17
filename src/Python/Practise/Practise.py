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




