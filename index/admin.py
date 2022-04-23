import os

from django.contrib import admin

from user.models import PersonInfo
from .models import Vocation

# 将模型直接注册到admin后台
# admin.site.register(PersonInfo)

# 自定义类
# 使用装饰器
@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'name', 'age']

# 注册方法二
# admin.site.register(PersonInfo, PersonInfoAdmin)

# 修改title和header
admin.site.site_title = 'MyDjango后台管理'
admin.site.site_header = 'MyDjango'


@admin.register(Vocation)
class VocationAdmin(admin.ModelAdmin):
    # 在数据新增或修改的页面设置可编辑字段
    # fields = ['job', 'title', 'payment', 'person']

    # 在数据新增或修改的页面设置不可编辑字段
    # exclude = []

    # 改变新增或修改的页面的网页布局
    fieldsets = (
        ('职业信息', {
            'fields': ('job', 'title', 'payment')
        }),
        ('人员信息', {
            # 设置隐藏与显示
            'classes': ('collapse',),
            'fields': ('person',),
        }),
    )

    # 将下拉框改为单选按钮
    # admin.HORIZONTAL 是水平排列
    # admin.VERTICAL 是垂直排列
    radio_fields = {'person': admin.HORIZONTAL}

    # 在数据新增或修改的页面设置可读子段,不可编辑
    # readonly_fields = ['job']

    # 设置排序方式
    ordering = ['id']

    # 设置数据列表页的每列数据是否可排列显示
    sortable_by = ['job', 'title']

    # 在数据列表页设置显示的模型字段
    list_display = ['id', 'job', 'title', 'payment', 'person']

    # 为数据列表页的id和job设置路由地址,由该路由地址可进入数据修改页
    # list_display_links = ['id', 'job']

    # 设置过滤器,若有外键,则应使用双下划线连接两个模型的字段
    list_filter = ['job', 'title', 'person__name']

    # 设置每页数据量
    list_per_page = 20

    # 在数据列表页设置每一页显示的最大上限的数据量
    list_max_show_all = 100

    # 为数据列表页的字段job和title设置可编辑状态
    list_editable = ['job', 'title']

    # 设置可搜索字段
    search_fields = ['job', 'title']

    # 在数据列表页设置日期选择器
    date_hierarchy = 'recordTime'

    # 在数据修改页添加"另存为"功能
    save_as = True

    # 设置"动作"栏的位置
    actions_on_top = False
    actions_on_bottom = True

    # 重写get_readonly_fields函数
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['payment']
        return self.readonly_fields

    list_display.append('colored_name')

    # 根据当前用户名设置数据访问权限
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=2)

    # 新增或修改数据时,设置外键可选值
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'person' and not request.user.is_superuser:
            v = Vocation.objects.filter(id__lt=2)
            kwargs['queryset'] = PersonInfo.objects.filter(id__in=v)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 获取数据模型的choice的值
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'job':
            kwargs['choices'] = (('软件开发', '软件开发'),
                                 ('软件测试', '软件测试'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    # 数据的修改实现日志记录
    def save_model(self, request, obj, form, change):
        if change:
            user = request.user.username
            job = self.model.objects.get(pk=obj.pk).job
            person = form.cleaned_data['person'].name
            path = os.path.abspath(os.path.dirname(__file__))
            f = open(path + '/log/log.txt','a')
            f.write(person + '职位: ' + job + ', 被' + user + '修改' + '\r\n')
            f.close()
        else:
            pass
        super().save_model(request, obj, form, change)

    # 数据的删除实现日志记录
    def delete_model(self, request, obj):

        user = request.user.username
        job = self.model.objects.get(pk=obj.pk).job
        path = os.path.abspath(os.path.dirname(__file__))
        f = open(path + '/log/log.txt', 'a')
        f.write('职位: ' + job + ', 被' + user + '删除' + '\r\n')
        f.close()

        pass
        super().delete_model(request, obj)

    # 数据批量操作
    def get_datas(self, request, queryset):
        temp = []
        for d in queryset:
            t = [d.job, d.title, str(d.payment), d.person.name]
            temp.append(t)
        path = os.path.abspath(os.path.dirname(__file__))
        f = open(path + '/data.txt', 'a')
        for t in temp:
            f.write(','.join(t) + '\r\n')

        f.close()
        # 设置提示信息
        self.message_user(request, '数据导出成功')

    # 设置函数的显示名称
    get_datas.short_description = '导出所选数据'
    # 添加到动作栏
    actions = ['get_datas']