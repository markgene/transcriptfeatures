"""Test TranscriptFeaturesCreator class with ERBB2 NM004448.2."""

import unittest

from transcriptfeatures import TranscriptFeatures
from transcriptfeatures.transcriptfeaturescreators import (
    TranscriptFeaturesCreator,
)


class TranscriptFeaturesCreatorErbb2Nm004448_2TestCase(unittest.TestCase):
    """Test TranscriptFeaturesCreator class with ERBB2 NM004448.2."""
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        tx_ac = "NM_004448.2"
        genome_ac = "NC_000017.10"
        transcript_features_creator = TranscriptFeaturesCreator(
            tx_ac=tx_ac,
            genome_ac=genome_ac,
            alt_aln_method="splign",
            promoter_tss_upstream_offset=1500,
        )
        cls.transcript_features_creator = transcript_features_creator

    def test_create(self):
        transcript_features = self.transcript_features_creator.create()
        self.assertTrue(isinstance(transcript_features, TranscriptFeatures))
