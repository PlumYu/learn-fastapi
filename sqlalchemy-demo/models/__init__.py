from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import DB_URL
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

# 定义命名约定的 Base 类
class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        # ix: index, 索引
        "ix": 'ix_%(column_0_label)s',
        # un:unique , 唯一主键
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        # ck: check,检查约束
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        # fk： Foreign Key， 外键约束
        "fk": "fk_%(table_name)s_%(column_0_name)s_fk",
        # pk： Primary Key， 主键约束
        "pk": "pk_%(table_name)s",
    })

from . import user
from . import article


## 创建引擎对象
engine = create_async_engine(
    DB_URL,
    # 将输出所有执行sql的日志（默认是关闭的）
    echo=True,
    # 连接池的大小（默认是 5 个） 设置并发零 70% ~ 80%
    pool_size=10,
    # 允许连接池的最大连接数（默认是 10 个）  允许临时创建链接  真正的连接数量 = pool_size + max_overflowfdssdfgf
    max_overflow=20,
    # 获得链接超时时间（默认是 30s）
    pool_timeout=10,
    # 连接回收时间（默认是 -1， 代表永不回收）
    pool_recycle=3600,
    # 连接前是否预检查 （默认是 False）
    pool_pre_ping=True,
)



# 创建会话工厂
AsyncSessionFactory = sessionmaker(
    # Engine 或者其子类对象（这里是 AsyncRngine）
    bind=engine,
    # Session 类的代替（默认是Session类）
    class_=AsyncSession,
    # 是否在查找之前执行 flush 操作（默认是True）
    autoflush=True,
    # 是否在执行 commit 操作后 Session 就过期（默认是 True）
    expire_on_commit=False,
)
