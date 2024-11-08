"""0-based genomic ranges (like SPDI and GA4GH and Biocommons alignment)."""

from dataclasses import dataclass

from .genomicrange import GenomicRange
from .sp0based import Sp0Based
from .sp1based import Sp1Based


@dataclass
class GenomicRange0Based(GenomicRange):
    """0-based genomic ranges (like SPDI and GA4GH and Biocommons alignment)."""

    def contains_position(self, pos: int) -> bool:
        """Does the range contain the position?

        As it is 0-based and behaves like Python. It checks in the
        manner like (start, end].
        """
        if pos > self.start and pos <= self.end:
            return True
        else:
            return False

    def contains_sp0_based(self, sp0_based: Sp0Based) -> bool:
        """Does the range contain the position?
        
        Check sequence accession first.

        Args:
            sp0_based (Sp0Based): a position.

        Returns:
            bool
        """
        if sp0_based.ac == self.ac:
            return self.contains_position(sp0_based.pos + 1)
        else:
            return False

    def contains_sp1_based(self, sp1_based: Sp1Based) -> bool:
        """Does the range contain the position?
        
        Check sequence accession first.

        Args:
            sp1_based (Sp0Based): a position.

        Returns:
            bool
        """
        if sp1_based.ac == self.ac:
            return self.contains_position(sp1_based.pos)
        else:
            return False
