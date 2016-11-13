# -*- coding=utf8 -*-
"""
    viterbi算法实现
"""
from pinyin.model import Emission, Transition
from json2sqlite.json2sqlite import json_load

def prepare_mat():
    start_mat = json_load("base_start.json")
    transition_mat = json_load("base_transition.json")
    emission_mat = json_load("base_emission.json")
    pinyin_mat = {}
    for hanzi in emission_mat.keys():
        for pinyin in emission_mat[hanzi]:
            if pinyin_mat.__contains__(pinyin):
                pinyin_mat[pinyin][hanzi] = emission_mat[hanzi][pinyin]
            else:
                pinyin_mat[pinyin] = {}
                pinyin_mat[pinyin][hanzi] = emission_mat[hanzi][pinyin]
    return start_mat, transition_mat, emission_mat, pinyin_mat

def viterbi(pinyin_list):
    """
    viterbi算法实现输入法

    Args:
        pinyin_list (list): 拼音列表
    """
    start_mat, transition_mat, emission_mat, pinyin_mat = prepare_mat()
    start_char = {}
    # start_char = Emission.join_starting(pinyin_list[0])
    for hanzi in pinyin_mat[pinyin_list[0]].keys():
        # print "hanzi", hanzi
        if start_mat.__contains__(hanzi):
            start_char[hanzi] = start_mat[hanzi] + emission_mat[hanzi][pinyin_list[0]]

    V = {char: start_char[char] for char in start_char}

    for i in range(1, len(pinyin_list)):
        pinyin = pinyin_list[i]
        prob_map = {}
        for phrase, prob in V.iteritems():
            character = phrase[-1]
            maxProb = 0
            state = ""
            new_prob = 0
            for hanzi in pinyin_mat[pinyin].keys():
                if transition_mat.__contains__(character) \
                    and transition_mat[character].__contains__(hanzi):
                    tmpProb = transition_mat[character][hanzi] + emission_mat[hanzi][pinyin]
                    if tmpProb > maxProb:
                        maxProb = tmpProb
                        state = hanzi
                        new_prob = tmpProb
            # result = Transition.join_emission(pinyin, character)
            if not maxProb:
                # del prob_map[phrase]
                continue
            prob_map[phrase + state] = new_prob + prob

        if prob_map:
            V = prob_map
        else:
            return V
    return V


if __name__ == '__main__':
    while 1:
        string = raw_input('input:')
        test = {}
        pinyin_list = string.split()
        V = viterbi(pinyin_list)

        for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
            print phrase, prob
