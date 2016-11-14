#!/usr/bin/env python
import sys, cPickle as pickle, os
from pinyin.hmm.viterbi2 import *

class TrieNode(object):
    def __init__(self):
        self.value = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                child = TrieNode()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key

    def search(self, key):
        if not key:
            return []
        node = self.root
        matches = []
        matched_length = 0
        for char in key:
            if char not in node.children:
                break
            node = node.children[char]
            if node.value:
                matches.append(node.value)
        if not matches:
               matches = key[0]
        return matches



class ScanPos(object):
    def __init__(self, pos, token=None, parent=None):
        self.pos = pos
        self.token = token
        self.parent = parent


from pinyinSplit import Trie
class PinyinTokenizer(object):

    def __init__(self):
        # with open('/home/jun/workspace/Pinyin_Demo/pinyinSplit/pinyin_trie') as f:

        # self.trie = prepare()
        from pinyinSplit import Trie

        self.trie = pickle.load(open("/home/jun/workspace/Pinyin_Demo/pinyinSplit/pinyin_trie.pkl", "r"))
        # self.trie= pickle.load(f)

    def tokenize(self, content):
        total_length = len(content)
        tokens = []
        candidate_pos = [ScanPos(0)]
        last_pos = None
        while candidate_pos:
            p = candidate_pos.pop()
            if p.pos == total_length:
                last_pos = p
                break
            matches = self.trie.search(content[p.pos:])
            for m in matches:
                new_pos = ScanPos(len(m) + p.pos, m, p)
                candidate_pos.append(new_pos)
        pos = last_pos
        while pos:
            if pos.parent:
                tokens.insert(0, pos.token)
            pos = pos.parent
        return tokens


def prepare():
    from pinyinSplit import Trie
    trie = Trie()
    file = open("/home/jun/workspace/Pinyin_Demo/pinyinSplit/pinyin.uniq", "r")
    while 1:
        line = file.readline().split("\n")[0]
        if not line:
            break
        trie.add(line)
        pass  # do something
    output = open('/home/jun/workspace/Pinyin_Demo/pinyinSplit/pinyin_trie.pkl', 'wb')
    pickle.dump(trie, output, 0)
    return trie

if __name__ == '__main__':
    while 1 :
        input = raw_input("input:")
        tokenizer = PinyinTokenizer()
        # # print tokenizer.tokenize('woaibeijingtiananmentiananmenshangtaiyangsheng')
        # print tokenizer.tokenize(input)

        pinyin_list = tokenizer.tokenize(input)
        print pinyin_list
        V = viterbi(pinyin_list)

        i = 0
        for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
            print phrase, prob
            i += 1
            if i >= 5:
                break
