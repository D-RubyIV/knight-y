from equipment.models import ShortRecord
from repository.shortrepository import ShortRepository
from service.baseservice import BaseService


class ShortService(BaseService):
    def __init__(self):
        self.repo = ShortRepository()
        super().__init__(self.repo, ShortRecord)
