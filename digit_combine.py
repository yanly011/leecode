class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ld = len(digits)
        result = []

        if (ld == 0):
            return []
        else:
            for digit in digits:
                if (int(digit) < 2):
                    return []
        if (ld == 1):
            return mapping[digits[0]]
        else:
            for index, digit in enumerate(digits):
                if (index == 0):
                    result = mapping[digit]
                    continue
                else:
                    current_level = mapping[digit]

                    if (int(digit) < 2):
                        return []
                    else:
                        new_result = []
                        for c in current_level:
                            for e in result:
                                e = e + c
                                new_result.append(e)
                        result = new_result
        return result