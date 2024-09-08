from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comomPrefix = ''
        firstString = strs[0]
        for i in range(len(firstString)):
            letter = firstString[i]
            concat = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    concat = False
                    break
                if strs[j][i] != letter:
                    concat = False
                    break

            if concat:
                comomPrefix += letter
            else:
                break

        return comomPrefix
