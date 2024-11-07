"""Genomic range."""

from dataclasses import dataclass


@dataclass
class GenomicRange:
    """Genomic range."""

    ac: str
    start: int
    end: int
    name: str = ""

    def __post_init__(self):
        if not isinstance(self.ac, str):
            raise ValueError(f"ac (sequence accession) {self.ac} must be a string")
        if not isinstance(self.start, int):
            raise ValueError(f"start (start position) {self.start} must be an integer")
        if self.start < 0:
            raise ValueError(
                f"start (start position) {self.start} must be a non-negative integer"
            )
        if not isinstance(self.end, int):
            raise ValueError(f"end (end position) {self.end} must be an integer")
        if self.end < 0:
            raise ValueError(
                f"end (end position) {self.end} must be a non-negative integer"
            )
        if self.start > self.end:
            raise ValueError(
                f"start {self.start} must be less than or equal to end {self.end}"
            )

    def __str__(self) -> str:
        return f"{self.name}: {self.ac}:{self.start}-{self.end}"
