from datetime import datetime

import pytz
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

Base = declarative_base()

vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
current_time_in_vietnam = datetime.now().replace(microsecond=0)

class BaseModel(DeclarativeBase):
    __abstract__ = True
    alias = "N/a"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    created_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=current_time_in_vietnam,
    )
    updated_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=current_time_in_vietnam,
        onupdate=current_time_in_vietnam,
    )

from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Bảng phụ cho Short - Category (đã có)
category_short = Table(
    'category_short',
    BaseModel.metadata,
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True),
    Column('short_id', Integer, ForeignKey('shorts.id'), primary_key=True)
)


# ✅ Category Entity
class CategoryRecord(BaseModel):
    __tablename__ = 'categories'

    name = Column(String, unique=True)

    shorts = relationship("ShortRecord", secondary=category_short, back_populates="categories")

    def __str__(self):
        return f"Category: {self.name}"

# ✅ Short Entity
class ShortRecord(BaseModel):
    __tablename__ = 'shorts'

    url = Column(String(50))
    like_count = Column(Integer)
    comment_count = Column(Integer)
    is_selected = Column(Boolean, default=False)
    description = Column(String(255))
    note = Column(String(100))
    hashtags = Column(String(255))

    categories = relationship("CategoryRecord", secondary=category_short, back_populates="shorts")

    def __str__(self):
        return f"Url: {self.url} | Likes: {self.like_count} | Comments: {self.comment_count}"
