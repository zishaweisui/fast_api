from infrastructure_exceptions import NotFoundException
from fastapi import HTTPException

class BaseHandler:
    def __init__(self, presenter=None):
        self.presenter = presenter

    def execute(self, handler_func, *args, **kwargs):
        try:
            data = handler_func(*args, **kwargs)
            if self.presenter:
                if isinstance(data, list):
                    data = [self.presenter.present(item) for item in data]
                else:
                    data = self.presenter.present(data)
            return data
        except NotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
