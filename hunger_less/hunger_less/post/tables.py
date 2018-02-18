import django_tables2 as tables
from .models import post, postlink,foodtype
from django.utils.html import format_html, mark_safe, escape
import datetime as dt

class PostTable(tables.Table):
    date = tables.Column(accessor='date')
    collectdate = tables.Column(accessor='collectdate',verbose_name= 'Collect Date')
    address = tables.Column(accessor='address',verbose_name= 'Address')
    description = tables.Column(accessor='description',verbose_name= 'Description')
    usercompany = tables.Column(accessor='user.CompanyName',verbose_name= 'Company')
    foodtype = tables.Column(accessor='foodtype.name',verbose_name= 'Food')
    quantity = tables.Column(accessor='quantity',verbose_name= 'Quantity')

    class Meta:
        model = post
        order_by = '-date'
        fields = ('date','collectdate','address','description','usercompany','foodtype','quantity')
        sequence = ('usercompany','date','address','foodtype','quantity','description','collectdate')

    def render_usercompany(self,value,record):
        return mark_safe("<div class=\"card-header\">%s" % (escape(value)))

    def render_date(self,value,record):
        return mark_safe(" <large class=\"float-sm-right\">Pick up By: %s</large></div>" % (escape(value.strftime('%d %B %Y'))))

    def render_address(self,value,record):
        return mark_safe("<ul class=\"list-group list-group-flush\">\
                        <li class=\"list-group-item\">%s</li>" % (escape(value)))

    def render_foodtype(self,value,record):
        return mark_safe("<li class=\"list-group-item\">%s" % (escape(value)))

    def render_quantity(self,value,record):
        return mark_safe("<large class=\"float-sm-right\">%s</large></li>" % (escape(value)))
    
    def render_description(self,value,record):
        return mark_safe("<li class=\"list-group-item\">%s</li></ul>" % (escape(value)))

    def render_collectdate(self,value,record):
        return mark_safe("<div class=\"card-footer text-muted\">\
                        <small class=\"float-sm-right\">%s</small>\
                </div>" % (escape(value.strftime('%d %B %Y'))))


