class TrieNodes():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.TrieNode = TrieNodes()
        

        

    def insert(self, word: str) -> None:
        cur = self.TrieNode
        for aword in word:
            if aword not in cur.children:
                cur.children[aword] = TrieNodes()
            cur = cur.children[aword]
                
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.TrieNode
        for aword in word:
            if aword not in cur.children:
                return False

            cur = cur.children[aword]

        return cur.endOfWord 
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.TrieNode
        for aword in prefix:
            if aword not in cur.children:
                return False

            cur = cur.children[aword]

        return True

        
        
        