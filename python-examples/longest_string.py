import collections

def lengthOfLongestSubstring(s):

        """
        longest substring without repeating characters

        always hold a window with only non repeating characters, see which is max len

        Time complexity: O(N)
        Space Complexity: O(1) #includes a dictonary of charatcers
        """
        counter = collections.defaultdict(int)

        n = len(s)
        i=0
        ans = 0
        for j in range(n):
            c= s[j]
            counter[c]+=1

            while counter[c] >1 and i<=j:
                counter[s[i]]-=1
                i+=1

            #now check the len
            print(f"loop {j}:  j={j}, i={i}, prev_ans={ans}")
            print(counter)
            ans = max(j-i+1, ans)
            print(f"c={c}, counter[c]={counter[c]}, ans={ans}")
        return ans

str = input("input your string: ")
print(lengthOfLongestSubstring(str))
