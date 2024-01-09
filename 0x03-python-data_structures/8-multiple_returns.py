#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        l = len(sentence)
    else:
        l = 0
    return (l, sentence if not sentence else sentence[:1])
