class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            length = len(i)
            encoded= encoded +  str(length) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        decode = []
        while len(s) > 0:
            for i in range(0, len(s)):
                if s[i]=="#":
                    length = int(s[0:i])
                    string_len = str(length)
                    word = s[len(string_len) + 1 :length + (len(string_len)) + 1]
                    decode.append(word)
                    break
            s= s[length + (len(string_len)) + 1:]
        return decode
                

