from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import List


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(100), index=True)
    password: Mapped[str] = mapped_column(String(200), index=True)
    mobile: Mapped[str] = mapped_column(String(100))
    user_extension: Mapped["UserExtension"] = relationship(back_populates="user",
    uselist=False     # 一对多的关系用 uselist , 默认值是 true
    )
    # 一对多的关系
    articles: Mapped[List["Article"]] = relationship(back_populates="author")

# 和User模型是一对一的关系
class UserExtension(Base):
    __tablename__ = "user_extension"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    university:Mapped[str] = mapped_column(String(100), index=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), unique=True)
    user:Mapped["User"] = relationship(back_populates="user_extension")
