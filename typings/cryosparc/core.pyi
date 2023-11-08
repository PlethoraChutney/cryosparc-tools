"""
This type stub file was generated by pyright.
"""
from enum import Enum
from typing import Optional, Tuple
from numpy.typing import NDArray

__all__ = ["DsetType", "Stream", "Data"]

class MemoryView:  # Note: Supports buffer protocol.
    base: "Array"
    size: int
    itemsize: int
    nbytes: int
    ndim: int
    shape: Tuple[int, ...]
    strides: Tuple[int, ...]
    suboffsets: Tuple[int, ...]
    T: "MemoryView"
    def copy(self) -> "MemoryView": ...
    def copy_fortran(self) -> "MemoryView": ...
    def is_c_contig(self) -> bool: ...
    def is_f_contig(self) -> bool: ...

class Array:
    memview: MemoryView

class DsetType(int, Enum):
    pass

class Data:
    pass

class Stream:
    def __init__(self, data: Data) -> None: ...
    def cast_objs_to_strs(self) -> None: ...
    def stralloc_col(self, col: str) -> Optional[Array]: ...
    def compress_col(self, col: str) -> Array: ...
    def compress_numpy(self, arr: NDArray) -> Array: ...
    def compress(self, arr: Array) -> Array: ...
    def decompress_col(self, col: str, data: bytes) -> Array: ...
    def decompress_numpy(self, data: bytes, arr: NDArray) -> Array: ...
    def decompress(self, data: bytes, outptr: int = 0) -> Array: ...
