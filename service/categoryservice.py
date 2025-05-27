from equipment.models import CategoryRecord
from repository.categoryrepository import CategoryRepository
from service.baseservice import BaseService


class CategoryService(BaseService):
    def __init__(self):
        self.repo = CategoryRepository()
        super().__init__(self.repo, CategoryRecord)