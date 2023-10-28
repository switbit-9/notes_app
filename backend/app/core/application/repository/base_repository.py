from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

_R = TypeVar('_R')


class BaseRepository(ABC, Generic[_R]):

    @abstractmethod
    def create(self, entity: _R) -> _R:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[_R]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id_: int) -> _R | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: _R) -> _R:
        raise NotImplementedError()

    @abstractmethod
    def delete_by_id(self, id_: int) -> _R:
        raise NotImplementedError()
