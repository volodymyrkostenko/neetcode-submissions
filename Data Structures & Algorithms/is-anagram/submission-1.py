class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
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