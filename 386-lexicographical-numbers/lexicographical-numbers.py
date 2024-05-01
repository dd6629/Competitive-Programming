class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []
    
    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1,n+1):
            self.insert(str(i))
        self._dfs(self.root,"")
        return self.ans

    def _dfs(self, child, path):
        if child.isWord:
            self.ans.append(int(path))
        for k, child in child.children.items():
            self._dfs(child, path+k)

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True