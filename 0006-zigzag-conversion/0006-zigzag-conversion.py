class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) < numRows or numRows == 1:
            return s

        cycle_elements = 2*numRows - 2
        full_cycles = len(s) // cycle_elements

        cycle_columns = numRows - 1

        modulo = len(s) % cycle_elements

        if (modulo == 0):
            numCols = cycle_columns * full_cycles
        
        elif (modulo <= numRows):
            numCols = cycle_columns * full_cycles + 1

        else:
            numCols = cycle_columns * full_cycles + 1 + (modulo - numRows)

        numCols = cycle_columns * (full_cycles + 1)

        output_array = [[0 for _ in range(numRows)] for _ in range(numCols)]

        c = 0
        r = -1
        rows_counter = 0

        for i in range(len(s)):
            if rows_counter == numRows:
                c += 1
                r -= 1
                output_array[c][r] = s[i]
                if r == 0:
                    rows_counter = 1

            else:
                r += 1
                output_array[c][r] = s[i]
                rows_counter += 1

        answer = ''

        for col in range(len(output_array[0])):
            for row in output_array:
                if row[col] == 0:
                    continue
                else:
                    answer = answer + str(row[col])

        return answer