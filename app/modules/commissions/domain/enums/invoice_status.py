from enum import Enum


class InvoiceStatus(str, Enum):
    OPEN = "open"
    PAID = "paid"
    CLOSED = "closed"
    CANCELLED = "cancelled"
    AWAITING_PAYMENT = "awaiting_payment"
