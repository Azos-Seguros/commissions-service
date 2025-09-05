from enum import Enum


class InvoiceType(str, Enum):
    COMMISSION = "commission"
    TAKE_RATE = "take_rate"
