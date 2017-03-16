import sys
sys.path.append("/home/jun/workspace/Pinyin_Demo")
from pinyin.hmm.viterbi2 import *
start_mat, transition_mat, emission_mat, pinyin_mat = prepare_mat()