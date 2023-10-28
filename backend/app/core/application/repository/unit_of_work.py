from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_R = TypeVar('_R')


class AbstractUnitOfWork(ABC, Generic[_R]):

    repository: _R

    @abstractmethod
    def begin(self):
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()