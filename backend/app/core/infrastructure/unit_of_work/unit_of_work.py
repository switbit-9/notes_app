from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_N = TypeVar('_N')


class AbstractUnitOfWork(ABC, Generic[_N]):

    repository: _N

    @abstractmethod
    def begin(self):
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()