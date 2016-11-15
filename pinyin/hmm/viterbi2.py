# -*- coding=utf8 -*-
"""
    viterbi算法实现,不使用sqllite,直接读取json存储的概率转移矩阵
"""
from pinyin.model import Emission, Transition
from json2sqlite.json2sqlite import json_load
# import scipy.io as sio
import pickle

def prepare_mat():
    # start_mat = json_load("base_start.json")
    # transition_mat = json_load("base_transition.json")
    # emission_mat = json_load("base_emission.json")
    start_mat = pickle.load(open("/home/jun/workspace/Pinyin_Demo/json2sqlite/start.mat","rb"))
    emission_mat = pickle.load(open("/home/jun/workspace/Pinyin_Demo/json2sqlite/emission.mat", "rb"))
    transition_mat = pickle.load(open("/home/jun/workspace/Pinyin_Demo/json2sqlite/transition.mat","rb"))
    # print transition_mat
    # print transition_mat
    # print emission_mat

    pinyin_mat = {}                      #计算拼音对应的汉字
    for hanzi in emission_mat.keys():
        for pinyin in emission_mat[hanzi]:
            if pinyin_mat.__contains__(pinyin):
                pinyin_mat[pinyin][hanzi] = emission_mat[hanzi][pinyin]
            else:
                pinyin_mat[pinyin] = {}
                pinyin_mat[pinyin][hanzi] = emission_mat[hanzi][pinyin]
    return start_mat, transition_mat, emission_mat, pinyin_mat

def viterbi(pinyin_list, start_mat, transition_mat, emission_mat, pinyin_mat):
    """
    viterbi算法实现输入法

    Args:
        pinyin_list (list): 拼音列表
    """
    if pinyin_list == []:
        return {}

    # print pinyin_mat
    start_char = {}        #计算第一个拼音对应的汉字

    if not pinyin_mat.__contains__(pinyin_list[0]):
        return {}

    for hanzi in pinyin_mat[pinyin_list[0]].keys():
        if start_mat.__contains__(hanzi):
            start_char[hanzi] = start_mat[hanzi] + emission_mat[hanzi][pinyin_list[0]]

    V = start_char
    for i in range(1, len(pinyin_list)):
        pinyin = pinyin_list[i]
        # print pinyin
        if not pinyin_mat.__contains__(pinyin):
            continue
        # print "hap"
        prob_map = {}
        for phrase, prob in V.iteritems():
            character = phrase[-1]
            maxProb = -0xffffff
            state = ""
            new_prob = 0
            for hanzi in pinyin_mat[pinyin].keys():
                if transition_mat.__contains__(character) and \
                        transition_mat[character].__contains__(hanzi):
                    # print hanzi
                    tmpProb = transition_mat[character][hanzi] + emission_mat[hanzi][pinyin]
                    # print tmpProb
                    if tmpProb > maxProb:
                        maxProb = tmpProb
                        state = hanzi
                        new_prob = tmpProb
            if not maxProb:
                if pinyin_mat.__contains__(pinyin):
                    hanzi_set = pinyin_mat[pinyin]
                    state, new_prob = sorted(hanzi_set.items(), key=lambda d: d[1], reverse=True)[0]
                    maxProb = new_prob
            if maxProb == -0xffffff:
                continue

            prob_map[phrase + state] = new_prob + prob

        if prob_map:
            V = prob_map
        else:
            return V
    return V


if __name__ == '__main__':
    flag = True
    start_mat, transition_mat, emission_mat, pinyin_mat = prepare_mat()
    while 1:
        string = raw_input('input:')
        test = {}
        pinyin_list = string.split(" ")
        print pinyin_list

        V = viterbi(pinyin_list,start_mat, transition_mat, emission_mat, pinyin_mat)
        for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
            print phrase, prob
    # transition_mat = pickle.load(open("/home/jun/workspace/Pinyin_Demo/json2sqlite/transition.mat", "rb"))

