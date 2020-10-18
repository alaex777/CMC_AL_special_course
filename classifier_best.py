from typing import List, Set, Dict, Any
from random import random
import re as re
import math as math
import statistics


def count_labels(labels: List):
    return {
        unique_label: sum(1 for label in labels if label == unique_label)
        for unique_label in set(labels)
    }

def predassembling( train_texts: List[str]) -> Any:
    result = list()
    for i in range(len(train_texts)):
        tmp = re.split('[^0-9a-z]', train_texts[i].lower())
        #tmp = [j for j in tmp if len(j) > 1]
        tmp = [tmp[j]+tmp[j+1] for j in range(len(tmp)-1) if len(tmp[j]) > 0 and len(tmp[j+1]) > 0]
        result.append(tmp)
    return result

def make_dict(list1: List) -> Dict:
    params = dict()
    tmpp = set()
    for i in list1:
        for j in i:
            if j in tmpp:
                params[j] += 1
            else:
                tmpp.add(j)
                params[j] = 1
    return params

def train(
        train_texts: List[str],
        train_labels: List[str],
        pretrain_params: Any = None) -> Any:
    """
    Trains classifier on the given train set represented as parallel lists of texts and corresponding labels.
    :param train_texts: a list of texts (str objects), one str per example
    :param train_labels: a list of labels, one label per example
    :param pretrain_params: parameters that were learned at the pretrain step
    :return: learnt parameters, or any object you like (it will be passed to the classify function)
    """
    positive = list()
    negative = list()
    pos_set = set()
    neg_set = set()
    pos_params = dict()
    neg_params = dict()
    pos_length = 0
    neg_length = 0
    pos_words = 0
    neg_words = 0

    predlist = predassembling(train_texts)
    
    for i in range(len(predlist)):
        if train_labels[i] == "pos":
            pos_length += 1
            positive.append(predlist[i])
            for j in predlist[i]:
                pos_set.add(j)
                pos_words += 1
        elif train_labels[i] == "neg":
            neg_length += 1
            negative.append(predlist[i])
            for j in predlist[i]:
                neg_set.add(j)
                neg_words += 1

    pos_params = make_dict(positive)
    neg_params = make_dict(negative)

    """pos_dict = {k: v for k, v in sorted(pos_params.items(), key=lambda item: item[1], reverse = True)}
    neg_dict = {k: v for k, v in sorted(neg_params.items(), key=lambda item: item[1], reverse = True)}
    tmp = 0
    for i in pos_dict:
        if tmp == 30:
            break
        print(i, ": ", pos_dict[i] / pos_words)
        tmp += 1
    tmp = 0
    for i in neg_dict:
        if tmp == 30:
            break
        print(i, ": ", neg_dict[i] / neg_words)
        tmp += 1"""

    

    res = [pos_set, neg_set, pos_params, neg_params, pos_length, neg_length, pos_words, neg_words]

    return res

    # ############################ REPLACE THIS WITH YOUR CODE #############################
    #label2cnt = count_labels(train_labels)  # count labels
    #print('Labels counts:', label2cnt)
    #train_size = sum(label2cnt.values())
    #label2prob = {label: cnt / train_size for label, cnt in label2cnt.items()}  # calculate p(label)
    #print(label2prob)
    #return {'prior': label2prob}  # this dummy classifier learns prior probabilities of labels p(label)
    # ############################ REPLACE THIS WITH YOUR CODE #############################


def pretrain(texts_list: List[List[str]]) -> Any:
    """
    Pretrain classifier on unlabeled texts. If your classifier cannot train on unlabeled data, skip this.
    :param texts_list: a list of list of texts (str objects), one str per example.
        It might be several sets of texts, for example, train and unlabeled sets.
    :return: learnt parameters, or any object you like (it will be passed to the train function)
    """
    # ############################ PUT YOUR CODE HERE #######################################
    return None


def classify(texts: List[str], params: Any) -> List[str]:
    """
    Classify texts given previously learnt parameters.
    :param texts: texts to classify
    :param params: parameters received from train function
    :return: list of labels corresponding to the given list of texts
    """

    pos_set = params[0]
    neg_set = params[1]
    pos_params = params[2]
    neg_params = params[3]
    pos_length = params[4]
    neg_length = params[5]
    pos_words = params[6]
    neg_words = params[7]

    inp = predassembling(texts)

    alpha = 1

    res = list()

    for i in inp:
        pos_sum = 0
        neg_sum = 0
        for j in i:
            if j in pos_set:
                pos_sum += math.log((alpha + pos_params[j]) / (alpha * len(pos_params) + pos_words))
            else:
                pos_sum += math.log(alpha / (alpha * len(pos_params) + pos_words))
            if j in neg_set:
                neg_sum += math.log((alpha + neg_params[j]) / (alpha * len(neg_params) + neg_words))
            else:
                neg_sum += math.log(alpha / (alpha * len(neg_params) + neg_words))
        pos_p = pos_sum + math.log(pos_length / (pos_length + neg_length))
        neg_p = neg_sum + math.log(neg_length / (pos_length + neg_length))
        if pos_p > neg_p:
            res.append("pos")
        else:
            res.append("neg")
    return res
       
    # ############################ REPLACE THIS WITH YOUR CODE #############################
    #def random_label(_label2prob):
    #    rand = random()  # random value in [0.0, 1.0) from uniform distribution
    #    for label, prob in _label2prob.items():
    #        rand -= prob
    #        if rand <= 0:
    #            return label

    #label2prob = params['prior']
    #res = [random_label(label2prob) for _ in texts]  # this dummy classifier returns random labels from p(label)
    #print('Predicted labels counts:')
    #print(count_labels(res))
    #return res
    # ############################ REPLACE THIS WITH YOUR CODE #############################
