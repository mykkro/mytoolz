# -*- coding: utf-8 -*-

from unittest import TestCase

from mytoolz import remove_accents

class TestRemoveAccents(TestCase):
    def test_remove_accents(self):
        input = "Příliš žluťoučký kůň úpěl ďábelské kódy. PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ KÓDY."
        expected = "Prilis zlutoucky kun upel dabelske kody. PRILIS ZLUTOUCKY KUN UPEL DABELSKE KODY."
        output = remove_accents(input)
        self.assertEquals(output, expected)
