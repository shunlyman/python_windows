from __future__ import annotations

from typing import Any

class Node(object):
    def __init__(self, data: Any):
        self.data = data
        self.next = Any