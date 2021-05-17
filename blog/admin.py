import csv

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.dispatch.dispatcher import logger
from django.http import HttpResponse
from django.utils.datetime_safe import datetime

from .models import BlogArticles


# define export action
# 接收的是固定的参数， 在 admin 的 action 中
def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = ['title', 'author', 'publish']
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_value = getattr(obj, field)
            # field_object = queryset.model._meta.get_field(field)
            # field_value = field_object.value_from_object(obj)
            csv_line_values.append(str(field_value))
        writer.writerow(csv_line_values)
    logger.error(" %s has exported %s candidate records" % (request.user.username, len(queryset)))

    return response



# 设置相应的表现形式
class BlogArticlesAdmin(admin.ModelAdmin):
    actions = [export_model_as_csv,]
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'
    ordering = ['publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)