# -*- coding=utf8 -*-
"""
    viterbi算法实现
"""
from pinyin.model import Emission, Transition


def viterbi(pinyin_list):
    """
    viterbi算法实现输入法

    Args:
        pinyin_list (list): 拼音列表
    """
    start_char = Emission.join_starting(pinyin_list[0])
    V = {char: prob for char, prob in start_char}

    for i in range(1, len(pinyin_list)):
        pinyin = pinyin_list[i]

        prob_map = {}
        maxProb = 0
        maxPhase = ""
        for phrase, prob in V.iteritems():
            if prob > maxProb:
                maxProb = prob
                maxPhase = phrase
            character = phrase[-1]
            result = Transition.join_emission(pinyin, character)
            if not result:
                result = Emission.join_starting(pinyin)

            for state, new_prob in result:
                prob_map[phrase + state] = new_prob + prob

        if prob_map:
            V = prob_map
        else:
            return  V

    return V


if __name__ == '__main__':
    while 1:
        string = raw_input('input:')
        pinyin_list = string.split()
        V = viterbi(pinyin_list)

        i = 0
        for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
            print phrase, prob
            i += 1
            if(i > 5):
                break
