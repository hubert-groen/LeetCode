class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        output = ''

        shortest_string = min(strs, key=len)
        shortest_string_index = strs.index(shortest_string)

        for i in range(len(strs[shortest_string_index])):

            current_letter = strs[0][i]

            for k in strs[1:]:

                print(i)

                if k[i] != current_letter:
                    return output
                
            output += current_letter
        
        return output