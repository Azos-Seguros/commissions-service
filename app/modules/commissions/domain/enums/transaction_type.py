from enum import Enum


class TransactionType(str, Enum):
    COMMISSION = "commission"
    TAKE_RATE = "take_rate"
