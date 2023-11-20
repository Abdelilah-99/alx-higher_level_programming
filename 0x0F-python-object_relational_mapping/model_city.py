"""..."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    """..."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, foreign_keys=('state_id'))

    state = relationship('State', backref='cities')
