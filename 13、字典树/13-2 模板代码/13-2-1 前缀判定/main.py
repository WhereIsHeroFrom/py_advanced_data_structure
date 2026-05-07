#####################×ÖµäÊ÷Ä£°å(Ç°×ºÅÐ¶¨)####################### 

ALPHABET_SIZE = 62 

class TrieNode: 
    def __init__(self): 
        self.children = [None] * ALPHABET_SIZE 
        self.isEndOfWord = False 
        self.count = 0 
        self.val = 0 

def trieIndex(c): 
    if 'a' <= c <= 'z': 
        return ord(c) - ord('a') 
    elif 'A' <= c <= 'Z': 
        return ord(c) - ord('A') + 26 
    return ord(c) - ord('0') + 52 

class Trie: 
    def __init__(self): 
        self.root = TrieNode() 

    def Insert(self, key, val = 0): 
        node = self.root 
        for c in key: 
            index = trieIndex(c) 
            if not node.children[index]: 
                node.children[index] = TrieNode() 
            node = node.children[index] 
            node.count += 1 
        node.isEndOfWord = True 
        node.val = val 

    def Search(self, key): 
        node = self.root 
        for c in key: 
            index = trieIndex(c) 
            if not node.children[index]: 
                return None 
            node = node.children[index] 
        if node.isEndOfWord: 
            return node.val 
        return None 

    def QueryPrefixCount(self, prefix): 
        node = self.root 
        for c in prefix: 
            index = trieIndex(c) 
            if not node.children[index]: 
                return 0 
            node = node.children[index] 
        return node.count        
#####################×ÖµäÊ÷Ä£°å(Ç°×ºÅÐ¶¨)####################### 

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    
    while t > 0:
        t -= 1
        n = int(data[idx]); idx += 1
        q = int(data[idx]); idx += 1
        
        trie = Trie()
        for _ in range(n):
            s = data[idx]; idx += 1
            trie.Insert(s, 1)
        
        out = []
        for _ in range(q):
            s = data[idx]; idx += 1
            out.append(str(trie.QueryPrefixCount(s)))
        
        print('\n'.join(out))

if __name__ == "__main__":
    main()