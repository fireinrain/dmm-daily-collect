from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# dmm task 任务
class BaseDmmTask(BaseModel):
    id: int = Field(..., description="ID", example=1)
    fetch_url: str = Field(..., description="URL", example="https://example.com")
    has_run: bool = Field(..., description="Has Run", example=True)
    run_date: str = Field(..., description="Run Date", example="2022-01-01")
    created_at: datetime = Field(..., description="Created At", example=datetime.now())
    updated_at: datetime = Field(..., description="Updated At", example=datetime.now())


class DmmTaskCreate(BaseDmmTask):
    ...


class DmmTaskUpdate(BaseDmmTask):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})


# 影片详情
class BaseFilmDetail(BaseModel):
    id: int = Field(..., description="ID", example=1)
    film_detail_url: str = Field(..., description="Film Detail URL", example="https://example.com/film-detail")
    film_pic_url: str = Field(..., description="Film Picture URL", example="https://example.com/film-pic")
    film_poster_url: str = Field(..., description="Film Poster URL", example="https://example.com/film-poster")
    film_title: str = Field(..., description="Film Title", example="The Movie")
    film_publish_date: str = Field(..., description="Film Publish Date", example="2022-01-01")
    film_sell_date: str = Field(..., description="Film Sell Date", example="2022-01-01")
    film_length: str = Field(..., description="Film Length", example="120 minutes")
    film_stars: str = Field(..., description="Film Stars", example="John Doe, Jane Smith")
    film_director: str = Field(..., description="Film Director", example="John Smith")
    film_series: str = Field(..., description="Film Series", example="Film Series Name")
    film_producers: str = Field(..., description="Film Producers", example="Producer 1, Producer 2")
    film_brand: str = Field(..., description="Film Brand", example="Film Brand Name")
    film_content_type: str = Field(..., description="Film Content Type", example="Action, Drama")
    film_type: str = Field(..., description="Film Type", example="Movie")
    film_tags: str = Field(..., description="Film Tags", example="Tag 1, Tag 2")
    film_code: str = Field(..., description="Film Code", example="ABC123")
    film_desc: str = Field(..., description="Film Description", example="This is a film description.")
    film_sample_image_prefix: str = Field(..., description="Film Sample Image Prefix",
                                          example="https://example.com/sample-images/")
    film_sample_images: str = Field(..., description="Film Sample Images", example="image1.jpg, image2.jpg")
    del_flag: bool = Field(None, description="Delete Flag", example=True)
    created_at: datetime = Field(..., description="Created At", example=datetime.now())
    updated_at: datetime = Field(..., description="Updated At", example=datetime.now())


class FilmDetailCreate(BaseFilmDetail):
    ...


class FilmDetailUpdate(BaseFilmDetail):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})


# 作品简介
class BaseFilmIntro(BaseModel):
    id: int = Field(..., description="ID", example=1)
    film_title: str = Field(..., description="Film Title", example="The Movie")
    film_cover_url: str = Field(..., description="Film Cover URL", example="https://example.com/film-cover")
    film_detail_url: str = Field(..., description="Film Detail URL", example="https://example.com/film-detail")
    film_star: str = Field(..., description="Film Star", example="John Doe")
    film_price: str = Field(..., description="Film Price", example="$9.99")
    del_flag: bool = Field(None, description="Delete Flag", example=True)
    created_at: datetime = Field(..., description="Created At", example=datetime.now())
    updated_at: datetime = Field(..., description="Updated At", example=datetime.now())


class FilmIntroCreate(BaseFilmIntro):
    ...


class FilmIntroUpdate(BaseFilmIntro):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})


# TelegramInfo
class BaseTelegramInfo(BaseModel):
    id: int = Field(..., description="ID", example=1)
    telegraph_post_url: str = Field(..., description="Telegraph Post URL", example="https://telegra.ph/post")
    film_detail_id: int = Field(..., description="Film Detail ID", example=1)
    has_create_post: bool = Field(..., description="Has Create Post", example=True)
    has_push_channel: bool = Field(..., description="Has Push Channel", example=True)
    del_flag: bool = Field(None, description="Delete Flag", example=True)
    created_at: datetime = Field(..., description="Created At", example=datetime.now())
    updated_at: datetime = Field(..., description="Updated At", example=datetime.now())


class TelegramInfoCreate(BaseTelegramInfo):
    ...


class TelegramInfoUpdate(BaseTelegramInfo):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})
