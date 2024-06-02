from fastapi import APIRouter, Query
from tortoise.expressions import Q

from app.controllers.dmm import dmm_task_controller, film_intro_controller, film_detail_controller, \
    telegram_info_controller

from app.schemas import Success, SuccessExtra
from app.schemas.dmm import DmmTaskCreate, DmmTaskUpdate, FilmIntroCreate, FilmIntroUpdate, FilmDetailCreate, \
    FilmDetailUpdate, TelegramInfoCreate, TelegramInfoUpdate

router = APIRouter()


@router.get("/dmm-task/list", summary="任务历史")
async def list_dmm_task(
        page: int = Query(1, description="页码"),
        page_size: int = Query(10, description="每页数量"),
        has_run: str = Query("", description="是否已经运行"),
        run_date: str = Query(None, description="运行日期"),
):
    q = Q()
    if has_run:
        has_run = bool(has_run)
        q &= Q(has_run=has_run)
    if run_date:
        q &= Q(run_date__contains=run_date)
    total, moni_objs = await dmm_task_controller.list(page=page, page_size=page_size, search=q,
                                                      order=["-run_date", "-id"])
    data = [await obj.to_dict() for obj in moni_objs]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/dmm-task/get", summary="查看任务")
async def get_dmm_task(
        dmm_task_id: int = Query(..., description="DMM task Record Id"),
):
    moni_obj = await dmm_task_controller.get(id=dmm_task_id)
    data = await moni_obj.to_dict()
    return Success(data=data)


@router.post("/dmm-task/create", summary="新建任务")
async def create_dmm_task(
        dmm_task_in: DmmTaskCreate,
):
    await dmm_task_controller.create(obj_in=dmm_task_in)
    return Success(msg="Created Successfully")


@router.post("/dmm-task/update", summary="修改任务")
async def update_dmm_task(
        dmm_task_in: DmmTaskUpdate,
):
    await dmm_task_controller.update(id=dmm_task_in.id, obj_in=dmm_task_in.update_dict())
    return Success(msg="Update Successfully")


@router.delete("/dmm-task/delete", summary="删除任务")
async def delete_dmm_task(
        dmm_task_id: int = Query(..., description="监控记录ID"),
):
    await dmm_task_controller.remove(id=dmm_task_id)
    return Success(msg="Deleted Success")


################################

@router.get("/film-intro/list", summary="影片简介列表")
async def list_film_intro(
        page: int = Query(1, description="页码"),
        page_size: int = Query(10, description="每页数量"),
        film_title: str = Query(None, description="影片标题"),
        film_star: str = Query(None, description="演员"),
        film_price: str = Query(None, description="价格"),
):
    q = Q()
    if film_title:
        q &= Q(film_title__contains=film_title)
    if film_star:
        q &= Q(film_star__contains=film_star)
    if film_price:
        q &= Q(film_price__contains=film_price)
    total, film_intro_objs = await film_intro_controller.list(page=page, page_size=page_size, search=q,
                                                              order=["-film_price", "id"])
    data = [await obj.to_dict() for obj in film_intro_objs]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/film-intro/get", summary="查看作品简介")
async def get_film_intro(
        film_intro_id: int = Query(..., description="FilmIntro Record Id"),
):
    film_intro_obj = await film_intro_controller.get(id=film_intro_id)
    data = await film_intro_obj.to_dict()
    return Success(data=data)


@router.post("/film-intro/create", summary="新建作品简介")
async def create_film_intro(
        film_intro_in: FilmIntroCreate,
):
    await film_intro_controller.create(obj_in=film_intro_in)
    return Success(msg="Created Successfully")


@router.post("/film-intro/update", summary="更新作品简介")
async def update_film_intro(
        film_intro_in: FilmIntroUpdate,
):
    await film_intro_controller.update(id=film_intro_in.id, obj_in=film_intro_in.update_dict())
    return Success(msg="Update Successfully")


@router.delete("/film-intro/delete", summary="删除作品简介")
async def delete_film_intro(
        film_intro_id: int = Query(..., description="作品简介id"),
):
    await film_intro_controller.remove(id=film_intro_id)
    return Success(msg="Deleted Success")


#################################

@router.get("/film-detail/list", summary="影片详情列表")
async def list_film_detail(
        page: int = Query(1, description="页码"),
        page_size: int = Query(10, description="每页数量"),
        film_title: str = Query(..., description="影片标题"),
        film_publish_date: str = Query(..., description="影片发布日期"),
        film_sell_date: str = Query(..., description="影片销售日期"),
        film_length: str = Query(..., description="影片时长"),
        film_stars: str = Query(..., description="影片演员"),
        film_director: str = Query(..., description="影片导演"),
        film_series: str = Query(..., description="影片系列"),
        film_producers: str = Query(..., description="影片制片人"),
        film_brand: str = Query(..., description="影片品牌"),
        film_content_type: str = Query(..., description="影片内容类型"),
        film_type: str = Query(..., description="影片类型"),
        film_tags: str = Query(..., description="影片标签"),
        film_code: str = Query(..., description="影片代码"),
        film_desc: str = Query(..., description="影片描述"),
):
    q = Q()
    if film_title:
        q &= Q(film_title__contains=film_title)
    if film_publish_date:
        q &= Q(film_publish_date__contains=film_publish_date)
    if film_sell_date:
        q &= Q(film_sell_date__contains=film_sell_date)
    if film_length:
        q &= Q(film_length__contains=film_length)
    if film_stars:
        q &= Q(film_stars__contains=film_stars)
    if film_director:
        q &= Q(film_director__contains=film_director)
    if film_series:
        q &= Q(film_series__contains=film_series)
    if film_producers:
        q &= Q(film_producers__contains=film_producers)
    if film_brand:
        q &= Q(film_brand__contains=film_brand)
    if film_content_type:
        q &= Q(film_content_type__contains=film_content_type)
    if film_type:
        q &= Q(film_type__contains=film_type)
    if film_tags:
        q &= Q(film_tags__contains=film_tags)
    if film_code:
        q &= Q(film_code__contains=film_code)
    if film_desc:
        q &= Q(film_desc__contains=film_desc)
    total, film_detail_objs = await film_detail_controller.list(page=page, page_size=page_size, search=q,
                                                                order=["film_sell_date", "id"])
    data = [await obj.to_dict() for obj in film_detail_objs]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/film-detail/get", summary="查看作品详情")
async def get_film_detail(
        film_detail_id: int = Query(..., description="FilmDetail Record Id"),
):
    film_detail_obj = await film_detail_controller.get(id=film_detail_id)
    data = await film_detail_obj.to_dict()
    return Success(data=data)


@router.post("/film-detail/create", summary="新建作品详情")
async def create_film_detail(
        film_detail_in: FilmDetailCreate,
):
    await film_detail_controller.create(obj_in=film_detail_in)
    return Success(msg="Created Successfully")


@router.post("/film-detail/update", summary="更新作品详情")
async def update_film_detail(
        film_detail_in: FilmDetailUpdate,
):
    await film_detail_controller.update(id=film_detail_in.id, obj_in=film_detail_in.update_dict())
    return Success(msg="Update Successfully")


@router.delete("/film-detail/delete", summary="删除作品详情")
async def delete_film_detail(
        film_detail_id: int = Query(..., description="作品详情id"),
):
    await film_detail_controller.remove(id=film_detail_id)
    return Success(msg="Deleted Success")


################################################################
@router.get("/telegram-info/list", summary="电报记录详情列表")
async def list_telegram_info(
        page: int = Query(1, description="页码"),
        page_size: int = Query(10, description="每页数量"),
        telegraph_post_url: str = Query(None, description="电报备份链接"),
        film_detail_id: int = Query(None, description="影片详情ID"),
        has_create_post: bool = Query(None, description="是否创建Telegraph"),
        has_push_channel: bool = Query(None, description="是否推送Telegram频道")
):
    q = Q()
    if telegraph_post_url:
        q &= Q(telegraph_post_url__contains=telegraph_post_url)
    if film_detail_id:
        q &= Q(film_detail_id=film_detail_id)
    if has_create_post is not None:
        q &= Q(has_create_post=has_create_post)
    if has_push_channel is not None:
        q &= Q(has_push_channel=has_push_channel)
    total, telegram_info_objs = await telegram_info_controller.list(page=page, page_size=page_size, search=q,
                                                                    order=["id"])
    data = [await obj.to_dict() for obj in telegram_info_objs]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/telegram-info/get", summary="查看电报记录详情")
async def get_telegram_info(
        telegram_info_id: int = Query(..., description="TelegramInfo Record Id"),
):
    telegram_info_obj = await telegram_info_controller.get(id=telegram_info_id)
    data = await telegram_info_obj.to_dict()
    return Success(data=data)


@router.post("/telegram-info/create", summary="新建电报记录详情")
async def create_telegram_info(
        telegram_info_in: TelegramInfoCreate,
):
    await telegram_info_controller.create(obj_in=telegram_info_in)
    return Success(msg="Created Successfully")


@router.post("/telegram-info/update", summary="更新电报记录详情")
async def update_telegram_info(
        telegram_info_in: TelegramInfoUpdate,
):
    await telegram_info_controller.update(id=telegram_info_in.id, obj_in=telegram_info_in.update_dict())
    return Success(msg="Update Successfully")


@router.delete("/telegram-info/delete", summary="删除电报记录详情")
async def delete_telegram_info(
        telegram_info_id: int = Query(..., description="电报记录详情id"),
):
    await telegram_info_controller.remove(id=telegram_info_id)
    return Success(msg="Deleted Success")


########################################################################


@router.get("/statics-dash", summary="DMM Daily图表数据")
async def get_statics_dash(
        sn: str = Query(..., description="SN编码"),
):
    # datas = await monitor_controller.model.filter(sn=sn).order_by("report_time").all()
    # data = [await obj.to_dict() for obj in datas]
    #
    # return Success(data=data)
    pass
