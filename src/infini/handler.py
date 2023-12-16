from abc import ABCMeta, abstractmethod
from .register import Handlers
from .event import MatcherEvent

__all__ = ["Result", "Handler"]


class Result:
    """规则包运行结果"""

    event: str
    status: bool
    kwargs: dict = {}

    def __init__(self, event: str, status: bool, **kwargs) -> None:
        self.event = event
        self.status = status
        self.kwargs = kwargs


class Handler(metaclass=ABCMeta):
    """规则包业务基类"""

    name: str
    priority: int = 0

    # def __init_subclass__(cls) -> None:
    #     handlers.regist(cls.name, cls())

    @abstractmethod
    def process(self, event: MatcherEvent) -> Result:
        raise NotImplementedError


handlers = Handlers()
