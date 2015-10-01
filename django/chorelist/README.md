```sh
$ django-admin startproject chorelist
$ cd chorelist/

$ python manage.py startapp chores
$ python manage.py makemigrations chores

$ python manage.py sqlmigrate chores 0001
$ python manage.py migrate
```

```sh
$ python manage.py shell
```

```python
>>> from chores.models import ChoreList, Chore
>>> ChoreList.objects.all()
[]
>>> from django.utils import timezone
>>> list = ChoreList(name="Monday List", due_date=timezone.now())
>>> list
<ChoreList: ChoreList object>
>>> list.name
'Monday List'
>>> list.save()
>>> quit()
```

``` python
>>> from chores.models import ChoreList, Chore
>>> ChoreList.objects.all()
[<ChoreList: Monday List>]
>>> ChoreList.objects.get(pk=1)
<ChoreList: Monday List>
>>> list = ChoreList.objects.get(pk=1)
>>> list.chore_set.all()
[]
>>> from django.utils import timezone
>>> list.chore_set.create(name="Wash dishes", due_date=timezone.now(), complete=False)
<Chore: Wash dishes>
>>> chore = list.chore_set.get(pk=1)
>>> chore
<Chore: Wash dishes>
>>>
```

```python
>>> chore.delete()
>>> list.delete()
```


```sh
$ python manage.py createsuperuser
$ python manage.py runserver
```
