from equipment.models import CategoryRecord
from repository.baserepository import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(domain=CategoryRecord)
