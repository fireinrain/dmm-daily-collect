from tortoise import fields

from app.schemas.menus import MenuType

from .base import BaseModel, TimestampMixin
from .enums import MethodType


class User(BaseModel, TimestampMixin):
    username = fields.CharField(max_length=20, unique=True, description="用户名称")
    alias = fields.CharField(max_length=30, null=True, description="姓名")
    email = fields.CharField(max_length=255, unique=True, description="邮箱")
    phone = fields.CharField(max_length=20, null=True, description="电话")
    password = fields.CharField(max_length=128, null=True, description="密码")
    is_active = fields.BooleanField(default=True, description="是否激活")
    is_superuser = fields.BooleanField(default=False, description="是否为超级管理员")
    last_login = fields.DatetimeField(null=True, description="最后登录时间")
    roles = fields.ManyToManyField("models.Role", related_name="user_roles")
    dept_id = fields.IntField(null=True, description="部门ID")

    class Meta:
        table = "user"

    class PydanticMeta:
        # todo
        # computed = ["full_name"]
        ...


class Role(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, unique=True, description="角色名称")
    desc = fields.CharField(max_length=500, null=True, blank=True, description="角色描述")
    menus = fields.ManyToManyField("models.Menu", related_name="role_menus")
    apis = fields.ManyToManyField("models.Api", related_name="role_apis")

    class Meta:
        table = "role"


class Api(BaseModel, TimestampMixin):
    path = fields.CharField(max_length=100, description="API路径")
    method = fields.CharEnumField(MethodType, description="请求方法")
    summary = fields.CharField(max_length=500, description="请求简介")
    tags = fields.CharField(max_length=100, description="API标签")

    class Meta:
        table = "api"


class Menu(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, description="菜单名称")
    remark = fields.JSONField(null=True, description="保留字段", blank=True)
    menu_type = fields.CharEnumField(MenuType, null=True, blank=True, description="菜单类型")
    icon = fields.CharField(max_length=100, null=True, blank=True, description="菜单图标")
    path = fields.CharField(max_length=100, description="菜单路径")
    order = fields.IntField(default=0, description="排序")
    parent_id = fields.IntField(default=0, max_length=10, description="父菜单ID")
    is_hidden = fields.BooleanField(default=False, description="是否隐藏")
    component = fields.CharField(max_length=100, description="组件")
    keepalive = fields.BooleanField(default=True, description="存活")
    redirect = fields.CharField(max_length=100, null=True, blank=True, description="重定向")

    class Meta:
        table = "menu"


class Dept(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, unique=True, description="部门名称")
    desc = fields.CharField(max_length=500, null=True, blank=True, description="备注")
    is_deleted = fields.BooleanField(default=False, description="软删除标记")
    order = fields.IntField(default=0, description="排序")
    parent_id = fields.IntField(default=0, max_length=10, description="父部门ID")

    class Meta:
        table = "dept"


class DeptClosure(BaseModel, TimestampMixin):
    ancestor = fields.IntField(description="父代")
    descendant = fields.IntField(description="子代")
    level = fields.IntField(default=0, description="深度")

    class Meta:
        table = "deptclosure"


class Monitor(BaseModel, TimestampMixin):
    sn = fields.CharField(max_length=100, description="SN编号")
    content = fields.CharField(max_length=1000, description="监控数据")
    report_time = fields.IntField(description="上报时间")
    start_time = fields.IntField(description="开始时间", null=True)
    end_time = fields.IntField(description="结束时间", null=True)

    class Meta:
        table = "monitor"


class MonitorSet(BaseModel, TimestampMixin):
    sn = fields.CharField(max_length=100, description="SN编号")
    api_url = fields.CharField(max_length=1000, description="监控数据api")
    fetch_interval = fields.IntField(description="采集间隔")
    enable = fields.CharField(max_length=10, description="是否开启")

    class Meta:
        table = "monitor_set"

    def __str__(self) -> str:
        return f"{self.sn}:{self.api_url}:{self.fetch_interval}:{self.enable}"


# dmm 数据
class DmmTask(BaseModel, TimestampMixin):
    fetch_url = fields.CharField(max_length=200, description='任务爬取链接')
    has_run = fields.BooleanField(default=False, description="是否已经运行")
    run_date = fields.CharField(max_length=25, description="开始运行时间")

    class Meta:
        table = "dmm_av_daily"


# 影片详情数据
class FilmDetail(BaseModel, TimestampMixin):
    film_detail_url = fields.CharField(max_length=255)
    film_pic_url = fields.CharField(max_length=255)
    film_poster_url = fields.CharField(max_length=255)
    film_title = fields.CharField(max_length=255)
    film_publish_date = fields.CharField(max_length=255)
    film_sell_date = fields.CharField(max_length=255)
    film_length = fields.CharField(max_length=255)
    film_stars = fields.CharField(max_length=255)
    film_director = fields.CharField(max_length=255)
    film_series = fields.CharField(max_length=255)
    film_producers = fields.CharField(max_length=255)
    film_brand = fields.CharField(max_length=255)
    film_content_type = fields.CharField(max_length=255)
    film_type = fields.CharField(max_length=255)
    film_tags = fields.CharField(max_length=255)
    film_code = fields.CharField(max_length=255)
    film_desc = fields.CharField(max_length=500)
    film_sample_image_prefix = fields.CharField(max_length=255)
    film_sample_images = fields.CharField(max_length=800)
    del_flag = fields.BooleanField(null=True, default=False)

    class Meta:
        table = "film_detail_item"

    def __str__(self):
        return f"{self.id}: {self.film_title}"


# 影片简介
class FilmIntro(BaseModel, TimestampMixin):
    film_title = fields.CharField(max_length=255)
    film_cover_url = fields.CharField(max_length=255)
    film_detail_url = fields.CharField(max_length=255)
    film_star = fields.CharField(max_length=255)
    film_price = fields.CharField(max_length=255)
    del_flag = fields.BooleanField(null=True)

    class Meta:
        table = "film_intro_item"

    def __str__(self):
        return f"{self.id}: {self.film_title}"


# 电报信息

class TelegramInfo(BaseModel, TimestampMixin):
    film_detail_id = fields.CharField(max_length=255)
    has_create_post = fields.BooleanField(default=False)
    has_push_channel = fields.BooleanField(default=False)
    telegraph_post_url = fields.CharField(max_length=255)
    del_flag = fields.BooleanField(null=True)

    class Meta:
        table = "telegram_info_detail"

    def __str__(self):
        return f"{self.id}: {self.film_title}"
