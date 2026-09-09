class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        for i in range(len(word)):
            if word[i] == ch :
                index = i
                break
        first_word = word[0:index+1]
        last_word = word[index+1:]
        reversing_1st_word = first_word[::-1]
        ans = reversing_1st_word + last_word
        return ans

        
        