#!/usr/bin/python
# -*- coding: utf-8 -*-


def tag_from_text(text):
    split_text = text.split(' ')
    if len(split_text) >= 2:
        return split_text[1]
