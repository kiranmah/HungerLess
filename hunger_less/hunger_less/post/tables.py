import django_tables2 as tables
from .models import post, postlink,foodtype

class PostTable(tables.Table):
    date = tables.Column(accessor='date')
    collectdate = tables.Column(accessor='collectdate',verbose_name= 'Collect Date')
    address = tables.Column(accessor='headline',verbose_name= 'Address')
    description = tables.Column(accessor='description',verbose_name= 'Description')
    usercompany = tables.Column(accessor='user.companyname',verbose_name= 'Company')
    foodtype = tables.Column(accessor='foodtype.name',verbose_name= 'Food')
    quantity = tables.Column(accessor='quantity',verbose_name= 'Quantity')
    quality = tables.Column(accessor='quality',verbose_name= 'Quality')  

    class Meta:
        model = post
        order_by = '-date'
        fields = ('date','collectdate','address','description','usercompany','foodtype','quantity','quality')
        sequence = ('date','collectdate','address','description','usercompany','foodtype','quantity','quality')
