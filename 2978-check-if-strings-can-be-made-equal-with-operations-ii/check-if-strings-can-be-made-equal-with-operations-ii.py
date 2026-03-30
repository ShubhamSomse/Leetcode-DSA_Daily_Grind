class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even = Counter()
        s1_odd = Counter()
        s2_even = Counter()
        s2_odd = Counter()

        for i in range(len(s1)):
            if i % 2 == 0:
                s1_even[s1[i]] += 1
                s2_even[s2[i]] += 1
            else:
                s1_odd[s1[i]] += 1
                s2_odd[s2[i]] += 1

        return s1_even == s2_even and s1_odd == s2_odd