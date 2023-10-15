class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        alphabet = list(string.ascii_lowercase)

        letters_array = []
        output = []

        def get_letters(digit):

            letters = []

            index = 3*(digit-2)
            if digit > 7:
                index +=1

            if digit < 7 or digit == 8:

                for i in range(3):
                    letters.append(alphabet[index+i])

            else:
                for i in range(4):
                    letters.append(alphabet[index+i])

            return letters

        if digits == "":
            return []

        for d in digits:

            digit_letters = [get_letters(int(d))]

            letters_array += digit_letters

        def generate_combinations(arrays, current_combination = ""):
            if not arrays:
                yield current_combination
            else:
                for element in arrays[0]:
                    new_combination = current_combination + element
                    yield from generate_combinations(arrays[1:], new_combination)

        for kombinacja in generate_combinations(letters_array):
            output.append(kombinacja)

        return output