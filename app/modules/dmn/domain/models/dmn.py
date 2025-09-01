from datetime import datetime


class DMNModel:
    #    __tablename__ = "dmn_rules"
    #
    #    id: str = Column(String, primary_key=True, default=lambda: str(uuid4()))
    #    account_id: str = Column(String, nullable=False)
    #    commission_percentage: float = Column(Float, nullable=False)
    #    take_rate_percentage: float = Column(Float, nullable=True)
    #    recurrence_type: str = Column(String, nullable=False)
    #    created_at: datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    #    updated_at: datetime = Column(
    #        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    #    )

    id: str
    account_id: str
    commission_percentage: float
    take_rate_percentage: float
    recurrence_type: str
    created_at: datetime
    updated_at: datetime
