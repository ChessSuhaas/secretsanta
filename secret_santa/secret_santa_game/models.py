from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    date = models.DateField()


class Blogs(models.Model):
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    date_time = models.DateTimeField(null=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class All_groups(models.Model):
    name = models.CharField(max_length=255)
    min_price = models.IntegerField()
    dead_line = models.DateField()
    create_date = models.DateField()
    special_key = models.CharField(20)
    password = models.CharField(max_length=255)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Group_members(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_id = models.ForeignKey(All_groups, on_delete=models.CASCADE)


class Wishes(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_id = models.ForeignKey(All_groups, on_delete=models.CASCADE)
    drawn_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='drawn_id', null=True)


class Group_chat(models.Model):
    chat = models.TextField(null=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_id = models.ForeignKey(All_groups, on_delete=models.CASCADE)