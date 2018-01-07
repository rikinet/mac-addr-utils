# Copyright (c) 2018 Riki Network Systems, Inc.
# All rights reserved.

from ipaddress import IPv4Address, IPv6Address, AddressValueError


def normalize_v4_address(source):
    """
    IPv4 アドレスを整形する。

    :param source: IPv4 アドレスと思われる文字列
    :type source: str
    :return: 整形した IPv4 アドレス
    :rtype: str
    """
    try:
        v4 = IPv4Address(source)
    except AddressValueError as _:
        return None
    return str(v4)


def normalize_v6_address(source):
    """
    IPv6 アドレスを整形する。

    :param source: IPv6 アドレスと思われる文字列
    :type source: str
    :return: 整形した IPv6 アドレス
    :rtype: str
    """
    try:
        v6 = IPv6Address(source)
    except AddressValueError:
        return None
    return str(v6)


def is_global(source):
    """
    グローバルアドレスであるかどうか判定する。

    :param source: IPv6 アドレスと思われる文字列
    :type source: str
    :return: IPv6 グローバルアドレスであるとき真
    """
    try:
        v6 = IPv6Address(source)
    except AddressValueError:
        return False
    return v6.is_global


def is_link_local(source):
    """
    リンクローカルアドレスであるかどうか判定する。

    :param source: IPv6 アドレスと思われる文字列
    :type source: str
    :return: IPv6 リンクローカルアドレスであるとき真
    """
    try:
        v6 = IPv6Address(source)
    except AddressValueError:
        return False
    return v6.is_link_local
