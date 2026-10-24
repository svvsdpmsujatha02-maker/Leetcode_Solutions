class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        result = ""

        for ch in sorted(freq, key=lambda x: freq[x], reverse=True):
            result += ch * freq[ch]

        return result
