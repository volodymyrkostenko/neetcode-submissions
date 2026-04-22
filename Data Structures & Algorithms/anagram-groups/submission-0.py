class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s: str, t: str):
            if len(s) != len(t):
                return False

            s_dic = {}
            t_dic = {}

            for i in range(0, len(s), 1):
                if s[i] in s_dic:
                    s_dic[s[i]] += 1
                else:
                    s_dic[s[i]] = 1

                if t[i] in t_dic:
                    t_dic[t[i]] += 1
                else:
                    t_dic[t[i]] = 1

            for key in s_dic:
                if s_dic.get(key, 0) != t_dic.get(key, 0):
                    return False

            return True

        results = [[strs.pop(0)]]

        for s in strs:
            hasAnagram = False
            for result in results:
                if isAnagram(s, result[0]):
                    hasAnagram = True
                    result.append(s)
                    break

            if not hasAnagram:
                results.append([s])

        return results
