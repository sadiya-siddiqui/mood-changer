
# def two_sum(num:list[int],target:int):
#     dict1={}
#     n=len(num)
#     for i in range(n):
#         rem=target-num[i]
#         if rem in dict1:
#            return [dict1[rem],i]
#         dict1[num[i]]=i

# print(two_sum([5,1,8,2,6,4,9],12))  # Output: [1, 2] (1 + 9 = 10)

                    #two_sum function using two pointers approach# This function finds two numbers in a sorted list that add up to a target value.# It returns the indices of those two numbers (1-based index).
# def two_sum(num:list[int],target:int):
#     left=0
#     right=len(num)-1
#     while left<right:
#         sum1=num[left]+num[right]
#         if sum1==target:
#             return [sum1,left+1,right+1]
#         elif sum1>target:
#            right-=1  
#         else:
#             left+=1

# print(two_sum([5,10,15,16,23],26))  # Output: [1, 9] (1 + 9 = 10)


                    #intersection of two arrays
# def inter(arr1:list[int],arr2:list[int]):
#     set1=set(arr1)
#     set2=set(arr2)
#     intersection_set=set1.intersection(set2)
#     intersection_set=set2.intersection(set1)
#     return list(intersection_set)
    
# print(inter([1,2,3,4,5],[4,5,6,7,8]))
# print(inter([1,2,3,4,5],[2,3,6,7,8]))  # This function finds the intersection of two arrays and returns a list of common elements.# It uses sets to efficiently find the common elements.# def inter(arr1:list[int],arr2:list[int]): 

                     #valid anagram
# def valid_anagram(s1:str,s2:str):
#     if len(s1) != len(s2):
#         return False
#     count = {}
#     for char in s1:
#         count[char] = count.get(char, 0) + 1
#     for char in s2:
#         if char not in count or count[char] == 0:
#             return False
#         count[char] -= 1
#     return all(value == 0 for value in count.values())

# print(valid_anagram("listen", "silent"))  # Output: True
# print(valid_anagram("hello", "world"))    # Output: False

                   #group anagrams
# def group_anagrams(strs:list[str]):
#     anagrams = {} 
#     for s in strs:
#         key = ''.join(sorted(s))  # Sort the characters in the string to create a key
#         if key not in anagrams:
#             anagrams[key] = []
#         anagrams[key].append(s)
#     return list(anagrams.values())

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
               

            #substring with all distinct characters 
# def countGoodSubstrings( s: str) -> int:
#         n=len(s)
#         ans=0
#         for i in range(n-2):
#          if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
#              ans+=1
#         return ans

# print(countGoodSubstrings("aabacbacaa"))  # Output: 1 (The substring "xyz" is the only good substring)

def lengthOfLongestSubstring( s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        ans=1
        set1=set({})
        set1.add(s[0])
        i=0
        j=1
        while j<n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
                set1.add(s[j])
                j+=1
                ans=max(ans,(j-i))
                return ans
                
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 (The longest substring without repeating characters is "abc")