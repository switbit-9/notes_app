from abc import ABC, abstractmethod
from typing import Sequence, TypeVar, Generic

_N = TypeVar('_N')

class QueryService(ABC, Generic[_N]):

    @abstractmethod
    def find_by_id(self, id_: int) -> _N | None:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[_N]:
        raise NotImplementedError()
