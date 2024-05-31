from app.core.crud import CRUDBase
from app.models.admin import DmmTask, FilmIntro, FilmDetail, TelegramInfo
from app.schemas.dmm import DmmTaskUpdate, DmmTaskCreate, FilmIntroCreate, FilmIntroUpdate, FilmDetailCreate, \
    FilmDetailUpdate, TelegramInfoCreate, TelegramInfoUpdate


class DmmTaskController(CRUDBase[DmmTask, DmmTaskCreate, DmmTaskUpdate]):
    def __init__(self):
        super().__init__(model=DmmTask)


dmm_task_controller = DmmTaskController()


class FilmIntroController(CRUDBase[FilmIntro, FilmIntroCreate, FilmIntroUpdate]):
    def __init__(self):
        super().__init__(model=FilmIntro)


film_intro_controller = FilmIntroController()


class FilmDetailController(CRUDBase[FilmDetail, FilmDetailCreate, FilmDetailUpdate]):
    def __init__(self):
        super().__init__(model=FilmDetail)


film_detail_controller = FilmDetailController()


class TelegramInfoController(CRUDBase[TelegramInfo, TelegramInfoCreate, TelegramInfoUpdate]):
    def __init__(self):
        super().__init__(model=TelegramInfo)


telegram_info_controller = TelegramInfoController()
