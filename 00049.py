# Time: O(n*m)
# Space: O(n)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = defaultdict(list)

        for i in strs:
            current = [0] * 26
            for j in i:
                current[ord(j)-ord('a')] += 1
            
            hashes[tuple(current)].append(i)
        
        return hashes.values()
