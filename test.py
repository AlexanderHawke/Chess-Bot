class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        sizes = []
        for string in strs:
            sizes.append(len(string))
        for size in sizes:
            result += str(size)
            result += "|"
        result += "#"
        for s in strs:
            res += s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        words = []
        for char in s:
            wordLength = 0




        return words
