# Copyright (c) 2018 Riki Network Systems, Inc.
"""
MAC アドレスの表記を変換するユーティリティーなど
"""

import re

TWO_HEX = r'([0-9A-Fa-f]{1,2})'
FOUR_HEX = r'([0-9A-Fa-f]{1,4})'
EX_TWO_HEX = r'([0-9A-Fa-f]{2})'
SEP_CHARS = r'[\:\-\.]'
PAT_MAC2 = '^' + SEP_CHARS.join((TWO_HEX, TWO_HEX, TWO_HEX, TWO_HEX, TWO_HEX, TWO_HEX)) + '$'
PAT_MAC4 = '^' + SEP_CHARS.join((FOUR_HEX, FOUR_HEX, FOUR_HEX)) + '$'
PAT_MAC12 = '^' + ''.join((EX_TWO_HEX, EX_TWO_HEX, EX_TWO_HEX, EX_TWO_HEX, EX_TWO_HEX, EX_TWO_HEX)) + '$'
REG_MAC2 = re.compile(PAT_MAC2)
REG_MAC4 = re.compile(PAT_MAC4)
REG_MAC12 = re.compile(PAT_MAC12)


def to_colon_separated(source):
    """
    MAC アドレスとして認識できる文字列をコロンで連結された六つ組に整形する。
    :param source:
    :type source: str
    :return: コロンで区切られた MAC アドレス
    :rtype: str
    """
    m = REG_MAC12.match(source)
    if m is not None:
        return ':'.join(m.group(1, 2, 3, 4, 5, 6)).lower()
    m = REG_MAC2.match(source)
    if m is not None:
        return ':'.join([expand(x, 2) for x in m.group(1, 2, 3, 4, 5, 6)]).lower()
    m = REG_MAC4.match(source)
    if m is not None:
        (t1, t2, t3) = [expand(x, 4) for x in m.group(1, 2, 3)]
        return ':'.join((t1[0:2], t1[2:4], t2[0:2], t2[2:4], t3[0:2], t3[2:4])).lower()
    return source


def to_dot_separated(source):
    """
    MAC アドレスとして認識できる文字列をドットで連結された三つ組みに整形する。
    :param source: 入力 MAC アドレス
    :type source: str
    :return: ドットで連結された4桁の16進数三つ組み
    :rtype: str
    """
    m = REG_MAC2.match(source)
    if m is not None:
        sextet = [expand(x, 2) for x in m.group(1, 2, 3, 4, 5, 6)]
        return '.'.join((sextet[0] + sextet[1], sextet[2] + sextet[3], sextet[4] + sextet[5])).lower()
    m = REG_MAC12.match(source)
    if m is not None:
        return '.'.join((m.group(1) + m.group(2), m.group(3) + m.group(4), m.group(5) + m.group(6))).lower()
    m = REG_MAC4.match(source)
    if m is not None:
        triple = [expand(x, 4) for x in m.group(1, 2, 3)]
        return '.'.join(triple).lower()
    return source


def expand(num, dig):
    """
    規定の桁数になるまで左にゼロを補う。
    :param num: MAC アドレスの部分
    :param dig: 伸張すべき規定の桁数
    :return: 桁数の数値
    """
    if num is None:
        num = '0'
    while len(num) < dig:
        num = '0' + num
    return num
