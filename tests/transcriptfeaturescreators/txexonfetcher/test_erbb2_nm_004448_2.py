"""Test TxExonFetcher class."""

import unittest

from transcriptfeatures.transcriptfeaturescreators.txexon import TxExon
from transcriptfeatures.transcriptfeaturescreators.txexonfetcher import TxExonFetcher


class TxExonFetcherTestCase(unittest.TestCase):
    """Test TxExonFetcher class."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        tx_ac = "NM_004448.2"
        genome_ac = "NC_000017.10"
        alt_aln_method = "splign"
        cls.tx_exon_fetcher = TxExonFetcher(
            tx_ac=tx_ac,
            genome_ac=genome_ac,
            alt_aln_method=alt_aln_method,
        )

    def test_fetch(self):
        tx_exon = self.tx_exon_fetcher.fetch()
        self.assertTrue(isinstance(tx_exon, TxExon))
        self.assertEqual(TxExon, None)
        
    def test_get_exons(self):
        exons = self.tx_exon_fetcher.get_exons()
        self.assertTrue(isinstance(exons, list))
        self.assertEqual(exons, None)

