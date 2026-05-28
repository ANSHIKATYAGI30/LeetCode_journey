class TrieNode(object):
    def __init__(self):

        self.children = {}

        # best index for this suffix
        self.idx = -1
        self.length = float('inf')


class Solution(object):

    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        # Build reversed trie
        for i, word in enumerate(wordsContainer):

            node = root

            # Update best answer at root
            if len(word) < node.length:
                node.length = len(word)
                node.idx = i

            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store shortest length word
                if len(word) < node.length:
                    node.length = len(word)
                    node.idx = i

        ans = []

        # Process queries
        for word in wordsQuery:

            node = root

            for ch in reversed(word):

                if ch not in node.children:
                    break

                node = node.children[ch]

            ans.append(node.idx)

        return ans
