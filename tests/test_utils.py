#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from utils import tag_from_text


class TestGettag(unittest.TestCase):

    def test_text_with_tag(self):
        text = 'imgur tag_name other text'

        self.assertEqual(
            'tag_name', tag_from_text(text)
        )

    def test_text_without_more_text(self):
        text = 'imgur'
        self.assertEqual(None, tag_from_text(text))
