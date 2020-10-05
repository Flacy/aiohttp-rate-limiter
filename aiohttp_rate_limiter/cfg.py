from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    method: Enum

    max_requests: int
    interval: int = 60
