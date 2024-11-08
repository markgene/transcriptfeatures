"""Test TxExonFetcher class with ERBB2 NM004448.2."""

import unittest

from psycopg2.extras import DictRow

from transcriptfeatures.transcriptfeaturescreators.txexon import TxExon
from transcriptfeatures.transcriptfeaturescreators.txexonfetcher import TxExonFetcher


class TxExonFetcherErbb2Nm004448_2TestCase(unittest.TestCase):
    """Test TxExonFetcher class with ERBB2 NM004448.2."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        tx_ac = "NM_004448.2"
        genome_ac = "NC_000017.10"
        alt_aln_method = "splign"
        tx_exon_fetcher = TxExonFetcher(
            tx_ac=tx_ac,
            genome_ac=genome_ac,
            alt_aln_method=alt_aln_method,
        )
        cls.tx_exon_fetcher = tx_exon_fetcher

    def test_fetch(self):
        tx_exons = self.tx_exon_fetcher.fetch()
        self.assertTrue(isinstance(tx_exons, list))
        for tx_exon in tx_exons:
            self.assertTrue(isinstance(tx_exon, TxExon))
        self.assertEqual(
            tx_exons,
            [
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=0,
                    tx_start_i=0,
                    tx_end_i=311,
                    alt_start_i=37856253,
                    alt_end_i=37856564,
                    cigar="311=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964695,
                    alt_exon_id=2179879,
                    exon_aln_id=615328,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=1,
                    tx_start_i=311,
                    tx_end_i=463,
                    alt_start_i=37863242,
                    alt_end_i=37863394,
                    cigar="152=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964696,
                    alt_exon_id=2179880,
                    exon_aln_id=615225,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=2,
                    tx_start_i=463,
                    tx_end_i=677,
                    alt_start_i=37864573,
                    alt_end_i=37864787,
                    cigar="214=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964697,
                    alt_exon_id=2179881,
                    exon_aln_id=615352,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=3,
                    tx_start_i=677,
                    tx_end_i=812,
                    alt_start_i=37865570,
                    alt_end_i=37865705,
                    cigar="135=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964698,
                    alt_exon_id=2179882,
                    exon_aln_id=615201,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=4,
                    tx_start_i=812,
                    tx_end_i=881,
                    alt_start_i=37866065,
                    alt_end_i=37866134,
                    cigar="69=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964699,
                    alt_exon_id=2179883,
                    exon_aln_id=615308,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=5,
                    tx_start_i=881,
                    tx_end_i=997,
                    alt_start_i=37866338,
                    alt_end_i=37866454,
                    cigar="116=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964700,
                    alt_exon_id=2179884,
                    exon_aln_id=615330,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=6,
                    tx_start_i=997,
                    tx_end_i=1139,
                    alt_start_i=37866592,
                    alt_end_i=37866734,
                    cigar="142=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964701,
                    alt_exon_id=2179885,
                    exon_aln_id=615284,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=7,
                    tx_start_i=1139,
                    tx_end_i=1259,
                    alt_start_i=37868180,
                    alt_end_i=37868300,
                    cigar="120=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964702,
                    alt_exon_id=2179886,
                    exon_aln_id=615351,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=8,
                    tx_start_i=1259,
                    tx_end_i=1386,
                    alt_start_i=37868574,
                    alt_end_i=37868701,
                    cigar="127=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964703,
                    alt_exon_id=2179887,
                    exon_aln_id=615346,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=9,
                    tx_start_i=1386,
                    tx_end_i=1460,
                    alt_start_i=37871538,
                    alt_end_i=37871612,
                    cigar="74=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964704,
                    alt_exon_id=2179888,
                    exon_aln_id=615138,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=10,
                    tx_start_i=1460,
                    tx_end_i=1551,
                    alt_start_i=37871698,
                    alt_end_i=37871789,
                    cigar="91=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964705,
                    alt_exon_id=2179889,
                    exon_aln_id=615204,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=11,
                    tx_start_i=1551,
                    tx_end_i=1751,
                    alt_start_i=37871992,
                    alt_end_i=37872192,
                    cigar="200=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964706,
                    alt_exon_id=2179890,
                    exon_aln_id=615243,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=12,
                    tx_start_i=1751,
                    tx_end_i=1884,
                    alt_start_i=37872553,
                    alt_end_i=37872686,
                    cigar="133=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964707,
                    alt_exon_id=2179891,
                    exon_aln_id=615182,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=13,
                    tx_start_i=1884,
                    tx_end_i=1975,
                    alt_start_i=37872767,
                    alt_end_i=37872858,
                    cigar="91=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964708,
                    alt_exon_id=2179892,
                    exon_aln_id=615280,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=14,
                    tx_start_i=1975,
                    tx_end_i=2136,
                    alt_start_i=37873572,
                    alt_end_i=37873733,
                    cigar="161=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964709,
                    alt_exon_id=2179893,
                    exon_aln_id=615300,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=15,
                    tx_start_i=2136,
                    tx_end_i=2184,
                    alt_start_i=37876039,
                    alt_end_i=37876087,
                    cigar="48=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964710,
                    alt_exon_id=2179894,
                    exon_aln_id=615151,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=16,
                    tx_start_i=2184,
                    tx_end_i=2323,
                    alt_start_i=37879571,
                    alt_end_i=37879710,
                    cigar="139=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964711,
                    alt_exon_id=2179895,
                    exon_aln_id=615167,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=17,
                    tx_start_i=2323,
                    tx_end_i=2446,
                    alt_start_i=37879790,
                    alt_end_i=37879913,
                    cigar="123=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964712,
                    alt_exon_id=2179896,
                    exon_aln_id=615242,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=18,
                    tx_start_i=2446,
                    tx_end_i=2545,
                    alt_start_i=37880164,
                    alt_end_i=37880263,
                    cigar="99=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964713,
                    alt_exon_id=2179897,
                    exon_aln_id=615261,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=19,
                    tx_start_i=2545,
                    tx_end_i=2731,
                    alt_start_i=37880978,
                    alt_end_i=37881164,
                    cigar="186=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964714,
                    alt_exon_id=2179898,
                    exon_aln_id=615312,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=20,
                    tx_start_i=2731,
                    tx_end_i=2887,
                    alt_start_i=37881301,
                    alt_end_i=37881457,
                    cigar="156=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964715,
                    alt_exon_id=2179899,
                    exon_aln_id=615258,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=21,
                    tx_start_i=2887,
                    tx_end_i=2963,
                    alt_start_i=37881579,
                    alt_end_i=37881655,
                    cigar="76=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964716,
                    alt_exon_id=2179900,
                    exon_aln_id=615143,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=22,
                    tx_start_i=2963,
                    tx_end_i=3110,
                    alt_start_i=37881959,
                    alt_end_i=37882106,
                    cigar="147=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964717,
                    alt_exon_id=2179901,
                    exon_aln_id=615221,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=23,
                    tx_start_i=3110,
                    tx_end_i=3208,
                    alt_start_i=37882814,
                    alt_end_i=37882912,
                    cigar="98=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964718,
                    alt_exon_id=2179902,
                    exon_aln_id=615294,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=24,
                    tx_start_i=3208,
                    tx_end_i=3397,
                    alt_start_i=37883067,
                    alt_end_i=37883256,
                    cigar="189=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964719,
                    alt_exon_id=2179903,
                    exon_aln_id=615302,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=25,
                    tx_start_i=3397,
                    tx_end_i=3650,
                    alt_start_i=37883547,
                    alt_end_i=37883800,
                    cigar="253=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964720,
                    alt_exon_id=2179904,
                    exon_aln_id=615292,
                ),
                TxExon(
                    hgnc="ERBB2",
                    tx_ac="NM_004448.2",
                    alt_ac="NC_000017.10",
                    alt_aln_method="splign",
                    alt_strand=1,
                    ord=26,
                    tx_start_i=3650,
                    tx_end_i=4624,
                    alt_start_i=37883941,
                    alt_end_i=37884915,
                    cigar="974=",
                    tx_aseq=None,
                    alt_aseq=None,
                    tx_exon_set_id=100972,
                    alt_exon_set_id=222083,
                    tx_exon_id=964721,
                    alt_exon_id=2179905,
                    exon_aln_id=615190,
                ),
            ],
        )

    @unittest.skip("as part of fetch()")
    def test_get_exons(self):
        exons = self.tx_exon_fetcher.get_exons()
        self.assertTrue(isinstance(exons, list))
        for exon in exons:
            self.assertTrue(isinstance(exon, DictRow))
        exons_as_list = [list(exon) for exon in exons]
        self.assertEqual(
            exons_as_list,
            [
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    0,
                    0,
                    311,
                    37856253,
                    37856564,
                    "311=",
                    None,
                    None,
                    100972,
                    222083,
                    964695,
                    2179879,
                    615328,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    1,
                    311,
                    463,
                    37863242,
                    37863394,
                    "152=",
                    None,
                    None,
                    100972,
                    222083,
                    964696,
                    2179880,
                    615225,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    2,
                    463,
                    677,
                    37864573,
                    37864787,
                    "214=",
                    None,
                    None,
                    100972,
                    222083,
                    964697,
                    2179881,
                    615352,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    3,
                    677,
                    812,
                    37865570,
                    37865705,
                    "135=",
                    None,
                    None,
                    100972,
                    222083,
                    964698,
                    2179882,
                    615201,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    4,
                    812,
                    881,
                    37866065,
                    37866134,
                    "69=",
                    None,
                    None,
                    100972,
                    222083,
                    964699,
                    2179883,
                    615308,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    5,
                    881,
                    997,
                    37866338,
                    37866454,
                    "116=",
                    None,
                    None,
                    100972,
                    222083,
                    964700,
                    2179884,
                    615330,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    6,
                    997,
                    1139,
                    37866592,
                    37866734,
                    "142=",
                    None,
                    None,
                    100972,
                    222083,
                    964701,
                    2179885,
                    615284,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    7,
                    1139,
                    1259,
                    37868180,
                    37868300,
                    "120=",
                    None,
                    None,
                    100972,
                    222083,
                    964702,
                    2179886,
                    615351,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    8,
                    1259,
                    1386,
                    37868574,
                    37868701,
                    "127=",
                    None,
                    None,
                    100972,
                    222083,
                    964703,
                    2179887,
                    615346,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    9,
                    1386,
                    1460,
                    37871538,
                    37871612,
                    "74=",
                    None,
                    None,
                    100972,
                    222083,
                    964704,
                    2179888,
                    615138,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    10,
                    1460,
                    1551,
                    37871698,
                    37871789,
                    "91=",
                    None,
                    None,
                    100972,
                    222083,
                    964705,
                    2179889,
                    615204,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    11,
                    1551,
                    1751,
                    37871992,
                    37872192,
                    "200=",
                    None,
                    None,
                    100972,
                    222083,
                    964706,
                    2179890,
                    615243,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    12,
                    1751,
                    1884,
                    37872553,
                    37872686,
                    "133=",
                    None,
                    None,
                    100972,
                    222083,
                    964707,
                    2179891,
                    615182,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    13,
                    1884,
                    1975,
                    37872767,
                    37872858,
                    "91=",
                    None,
                    None,
                    100972,
                    222083,
                    964708,
                    2179892,
                    615280,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    14,
                    1975,
                    2136,
                    37873572,
                    37873733,
                    "161=",
                    None,
                    None,
                    100972,
                    222083,
                    964709,
                    2179893,
                    615300,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    15,
                    2136,
                    2184,
                    37876039,
                    37876087,
                    "48=",
                    None,
                    None,
                    100972,
                    222083,
                    964710,
                    2179894,
                    615151,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    16,
                    2184,
                    2323,
                    37879571,
                    37879710,
                    "139=",
                    None,
                    None,
                    100972,
                    222083,
                    964711,
                    2179895,
                    615167,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    17,
                    2323,
                    2446,
                    37879790,
                    37879913,
                    "123=",
                    None,
                    None,
                    100972,
                    222083,
                    964712,
                    2179896,
                    615242,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    18,
                    2446,
                    2545,
                    37880164,
                    37880263,
                    "99=",
                    None,
                    None,
                    100972,
                    222083,
                    964713,
                    2179897,
                    615261,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    19,
                    2545,
                    2731,
                    37880978,
                    37881164,
                    "186=",
                    None,
                    None,
                    100972,
                    222083,
                    964714,
                    2179898,
                    615312,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    20,
                    2731,
                    2887,
                    37881301,
                    37881457,
                    "156=",
                    None,
                    None,
                    100972,
                    222083,
                    964715,
                    2179899,
                    615258,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    21,
                    2887,
                    2963,
                    37881579,
                    37881655,
                    "76=",
                    None,
                    None,
                    100972,
                    222083,
                    964716,
                    2179900,
                    615143,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    22,
                    2963,
                    3110,
                    37881959,
                    37882106,
                    "147=",
                    None,
                    None,
                    100972,
                    222083,
                    964717,
                    2179901,
                    615221,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    23,
                    3110,
                    3208,
                    37882814,
                    37882912,
                    "98=",
                    None,
                    None,
                    100972,
                    222083,
                    964718,
                    2179902,
                    615294,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    24,
                    3208,
                    3397,
                    37883067,
                    37883256,
                    "189=",
                    None,
                    None,
                    100972,
                    222083,
                    964719,
                    2179903,
                    615302,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    25,
                    3397,
                    3650,
                    37883547,
                    37883800,
                    "253=",
                    None,
                    None,
                    100972,
                    222083,
                    964720,
                    2179904,
                    615292,
                ],
                [
                    "ERBB2",
                    "NM_004448.2",
                    "NC_000017.10",
                    "splign",
                    1,
                    26,
                    3650,
                    4624,
                    37883941,
                    37884915,
                    "974=",
                    None,
                    None,
                    100972,
                    222083,
                    964721,
                    2179905,
                    615190,
                ],
            ],
        )
