from equipment.models import ShortRecord
from repository.baserepository import BaseRepository


class ShortRepository(BaseRepository):
    def __init__(self):
        super().__init__(domain=ShortRecord)