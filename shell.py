from instagramm.models import *

posts = Post.objects.all()

posts_postman = Post.objects.filter(title='Postman')
#query setы ленивы потому что запрос данных после не летит в базу данных,
# оно полетит если принтить/serialize/template


# posts_2 = posts_filter.filter(createdat='2022-01-01')

posts_2023 = Post.objects.filter(date_posted__year=2023)

Post.objects.filter(date_posted__year=2023) #два нижних подчеркивания это обращение, не точкой

post_windows = Post.objects.filter(body__startswith='Windows').filter(date_posted__year=2023)

post_windows = Post.objects.filter(body__startswith='Windows')(date_posted__year=2023)

posts = Post.objects.filter(date_posted__year=2021)

post = Post.objects.get(id=1)

post = Post.objects.get(date_updated__year=2023)

post = Post.objects.filter(date_updated__year=2024).first() #вернет None

posts = Post.objects.exclude(date_posted__year=2023).filter(title__startswith='Linux').exclude()

posts= Post.objects.all().order_by('-title') #desc, если без минуса сделает asc

posts = Post.objects.all().values() #получаем весь список

posts = Post.objects.all().values('title', 'body') #получаем то что нам надо

posts = Post.objects.all().values_list() #получаем результат в виде списка из кортежей

posts = Post.objects.all().values_list('title', 'body') #позиционная передача данных

posts = Post.objects.all().values_list('title', flat=True)

posts = Post.objects.all().none() #возвращает пустой список , у него нет query


comments = Comment.objects.all()

comments = Comment.objects.all().select_related('post', 'user', 'post__user') #inner join SQL

posts = Post.objects.all() #срезы через [0:2] [c какого-то : по такой-то] LIMIT SQl

post = Post.objects.all()[0]

post = Post.objects.all().order_by('-id')[0]

post = Post.objects.filter(id=250)[0]

posts = Post.objects.all().only('title', 'body')

#Filter Lookup Type

posts = Post.objects.filter(date_posted__lte='2022-12-31') #lte меньше чем или равно

posts = Post.objects.filter(date_posted__gt='2022-12-31') #gte больше чем

post = Post.objects.filter(id__exact=1) #чаще всего он не нужен т.к это одно и то же post = Post.objects.filter(id=1)

post = Post.objects.filter(title__exact=' Post about postman program')
post = Post.objects.filter(title__iexact=' Post about postman program') #iexact не обращает на регистры

posts =Post.objects.filter(title__contains='program')
posts =Post.objects.filter(title__icontains='program') #LIKE SQL

posts = Post.objects.filter(id__in=[3, 4])

comments = Comment.objects.filter(post__title__icontains='postman')
comments = Comment.objects.filter(post__user__username__startswith='adm')

posts = Post.objects.filter(date_posted__year=2022, title__icontains='postman')

from django.db.models import Q

posts = Post.objects.filter(Q(date_posted__year=2022) | Q(title__icontains='postman'))
posts = Post.objects.filter(Q(date_posted__year=2022), Q(title__icontains='postman'))
posts = Post.objects.filter(Q(date_posted__year=2022) & Q(title__icontains='postman'))

posts = Post.objects.filter((Q(date_posted__year=2022) | Q(title__icontains='postman')) & (Q(body__icontains='gaming')))


