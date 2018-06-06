# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Huffman En-/Decoding

'''

from heapq import heappush, heappop, heapify
from collections import Counter

def build_frequency_dict(txt: str):
    return Counter(txt)

def build_huffman_encoding_dict(txt: str):
    frq_dict = build_frequency_dict(txt)
    heap = [[wt, [sym, ""]] for sym, wt in frq_dict.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))

def build_decoder_dict(encoder_dict):
    return {y : x for x,y in encoder_dict.items()}

def encode_txt(txt: str, enc_dict=None):
    result = ""
    if not enc_dict:
        enc_dict = build_huffman_encoding_dict(txt)
    for c in txt:
        result += enc_dict[c]
    return result

def decode_txt(enc_txt: str, decode_dict=None):
    result = ""
    bits = ""
    for bit in enc_txt:
        bits += bit
        if bits in decode_dict:
            result += decode_dict[bits]
            bits = ""
    return result

def main():
    txt = "Das ist ein kleiner Test!"
    encode_dict = build_huffman_encoding_dict(txt)
    decode_dict = build_decoder_dict(encode_dict)
    enc_txt = encode_txt(txt, encode_dict)
    print(enc_txt)
    print(decode_txt(enc_txt, decode_dict))

if __name__ == "__main__":
    main()