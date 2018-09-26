#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def convert(word):
    n_word = word[1:] + word[0]
    return n_word

def igpay(word):
    if word[0] in 'aeiou':
        return print(word + 'way')
    else:
        n_word = convert(word) + 'ay'
        return print(n_word)

if __name__ == '__main__':
    igpay('pig')
    igpay('apple')

