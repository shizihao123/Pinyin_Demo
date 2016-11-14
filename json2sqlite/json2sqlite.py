# -*- coding=utf8 -*-
from __future__ import division
import json
from pinyin.model import (
    Transition,
    Emission,
    Starting,
    init_hmm_tables,
    HMMSession
)

"""
    加载jason文件
"""
def json_load(file_name= "base_start.json"):
    f = open("/home/jun/workspace/Pinyin_Demo/json2sqlite/" + file_name, "r")
    s = json.load(f)
    return s


"""
    获取HMM模型
"""
def init_start():
    """
    初始化起始概率
    """
    s = json_load("base_start.json")
    for character in s.keys():
        Starting.add(character, s[character])


def init_emission():
    """
    初始化发射概率
    """
    s = json_load("base_emission.json")
    for hanzi in s.keys():
        for pinyin in s[hanzi].keys():
            Emission.add(hanzi, pinyin, s[hanzi][pinyin])


def init_transition():
    """
    初始化转移概率
    """
    s = json_load("base_transition.json")
    for previous in s.keys():
        for behind in s[previous].keys():
            Transition.add(previous, behind, s[previous][behind])


if __name__ == '__main__':
    # init_hmm_tables()  #重新建hmm.sqlite
    # init_start()
    init_emission()
    init_transition()
    #
    # # 创建索引
    # session = HMMSession()
    # session.execute('create index ix_starting_character on starting(character);')
    # session.execute('create index ix_emission_character on emission(character);')
    # session.execute('create index ix_emission_pinyin on emission(pinyin);')
    # session.execute('create index ix_transition_previous on transition(previous);')
    # session.execute('create index ix_transition_behind on transition(behind);')
    # session.commit()


