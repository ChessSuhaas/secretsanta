from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime, timedelta
from .models import Users , Blogs, All_groups, Group_members, Wishes, Group_chat
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

global entry
entry = False

global userinfo
userinfo = ''


def login(request):
    template = loader.get_template('login.html')
    contents = {'alert': None}
    if 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        users = Users.objects.all().values('username', 'password')
        if {'username':username, 'password':password} not in list(users):
            contents.update({'alert': 'Incorrect username or paasword'})
            return HttpResponse(template.render(contents, request))
        else:
            global entry
            entry = True
            global userinfo
            userinfo = username
            return redirect(reverse('home'))
    return HttpResponse(template.render(contents, request))


def register(request):
    template = loader.get_template('register.html')
    contents = {'alert': None}
    if 'register' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        date = datetime.now().date()

        try:
            new_user = Users(
                username=username,
                password=password,
                email=email,
                date=date
            )
            new_user.save()
        except:
            contents.update({'alert':'Username or email already exists'})
            return HttpResponse(template.render(contents, request))

        global entry
        entry = True
        global userinfo
        userinfo = username
        return redirect(reverse('home'))
    return HttpResponse(template.render(contents, request))


def home(request):
    template = loader.get_template('home.html')
    if entry != True:
        return redirect(reverse('login'))
    all_blogs = Blogs.objects.select_related('user_id').all().order_by('-date_time')
    if 'create' in request.POST:
        user_id = Users.objects.filter(username=userinfo).get()
        date_time = datetime.now()
        title = str(request.POST['subject'])
        content = str(request.POST['content'])
        new_blog = Blogs(
            title=title,
            content=content,
            date_time=date_time,
            user_id=user_id
        )
        new_blog.save()
        return redirect(reverse('home'))
    if 'del' in request.POST:
        param = request.POST['invis_param']
        Blogs.objects.filter(id=param).delete()
        return redirect(reverse('home'))
    if 'edit' in request.POST:
        title = request.POST['subject']
        content = request.POST['content']
        id = request.POST['date']
        date_time = datetime.now()
        Blogs.objects.filter(id=id).update(
            title=title,
            content=content,
            date_time=date_time
        )
        return redirect(reverse('home'))
    contents = {
        'blogs': all_blogs,
        'username': userinfo
    }
    return HttpResponse(template.render(contents, request))


def create_group(request):
    if entry != True:
        return redirect(reverse('login'))
    user_id = Users.objects.get(username=userinfo).id
    group_info = All_groups.objects.filter(user_id_id=user_id).all().order_by('-create_date')
    print(f'Info: {list(group_info)} \n\n\n\n\n\n\n\n')
    if 'create' in request.POST:
        group_name = request.POST['group_name']
        min_price = request.POST['min_price']
        create_date = datetime.now().date()
        dead_line = int(request.POST['deadline'])
        dead_line = create_date + timedelta(days=dead_line)
        password = request.POST['password']
        user_id = Users.objects.filter(username=userinfo).get()
        special_keys = All_groups.objects.all().values('special_key')
        while True:
            import random
            choice1 = ['a', 'b', 'c', 'd', 'e']
            choice2 = ['a', 'b', 'c', 'd', 'e']
            choice3 = ['a', 'b', 'c', 'd', 'e']
            choice4 = ['a', 'b', 'c', 'd', 'e']
            choice5 = ['a', 'b', 'c', 'd', 'e']
            choice6 = ['a', 'b', 'c', 'd', 'e']
            choice7 = ['a', 'b', 'c', 'd', 'e']
            choice8 = ['a', 'b', 'c', 'd', 'e']
            choice9 = ['a', 'b', 'c', 'd', 'e']
            choice10 = ['a', 'b', 'c', 'd', 'e']
            choice11 = ['a', 'b', 'c', 'd', 'e']
            choice12 = ['a', 'b', 'c', 'd', 'e']
            choice13 = ['a', 'b', 'c', 'd', 'e']
            choice14 = ['a', 'b', 'c', 'd', 'e']
            choice15 = ['a', 'b', 'c', 'd', 'e']
            choice16 = ['1', '2', '3', '4', '5']
            choice17 = ['1', '2', '3', '4', '5']
            choice18 = ['1', '2', '3', '4', '5']
            choice19 = ['1', '2', '3', '4', '5']
            choice20 = ['1', '2', '3', '4', '5']
            sys_choice = [random.choice(choice1), random.choice(choice2), random.choice(choice3), random.choice(choice4), random.choice(choice5), random.choice(choice6), random.choice(choice7), random.choice(choice8), random.choice(choice9), random.choice(choice10), random.choice(choice11), random.choice(choice12), random.choice(choice13), random.choice(choice14), random.choice(choice15), random.choice(choice16), random.choice(choice17), random.choice(choice18), random.choice(choice19), random.choice(choice20)]
            random.shuffle(sys_choice)
            cus_choice = ''
            for digit in range(len(sys_choice)):
                cus_choice += sys_choice[digit]
            if (cus_choice,) in special_keys:
                cus_choice = ''
                continue
            else:
                break
        All_groups(
            name=group_name,
            min_price=min_price,
            dead_line=dead_line,
            create_date=create_date,
            special_key=cus_choice,
            password=password,
            user_id=Users.objects.get(id=user_id.id)
        ).save()
        Group_members(
            user_id=Users.objects.get(id=user_id.id),
            group_id=All_groups.objects.get(special_key=cus_choice)
        ).save()
        return redirect(reverse('create_group'))
    if 'del_2' in request.POST:
        param = request.POST['invis_param']
        All_groups.objects.filter(special_key=param).delete()
        return redirect(reverse('create_group'))
    if 'edit' in request.POST:
        new_group_name = request.POST['group_name']
        new_min_price = request.POST['min_price']
        new_create_date = datetime.now().date()
        new_dead_line = int(request.POST['deadline'])
        new_dead_line = new_create_date + timedelta(days=new_dead_line)
        date_param = request.POST['date_param']
        new_password = request.POST['password']
        All_groups.objects.filter(id=date_param).update(
            name=new_group_name,
            min_price=new_min_price,
            dead_line=new_dead_line,
            create_date=new_create_date,
            password=new_password,
        )
        return redirect(reverse('create_group'))
    template = loader.get_template('create_group.html')
    contents = {
        'groups': group_info,
        'name': userinfo
    }
    return HttpResponse(template.render(contents, request))


def join_group(request):
    contents = {
        'alert': None
    }
    template = loader.get_template('join_group.html')
    if entry != True:
        return redirect(reverse('login'))
    if 'join' in request.POST:
        key = request.POST['key']
        password = request.POST['password']
        try:
            group_id = All_groups.objects.get(special_key=key, password=password)
            my_id = Users.objects.get(username=userinfo)
            Group_members(
                user_id=my_id,
                group_id=group_id
            ).save()
            return redirect(reverse('my_group'))
        except:
            contents = {
                'alert': 'There is an error in request'
            }
            return HttpResponse(template.render(contents, request))
    return HttpResponse(template.render(contents, request))


def my_groups(request):
    if entry != True:
        return redirect(reverse('login'))
    user_id = Users.objects.get(username=userinfo)
    all_groups = Group_members.objects.filter(user_id=user_id)
    all_groups_list = []
    for group in all_groups:
        all_groups_list.append((group.group_id.id, group.group_id.name, group.group_id.min_price, group.group_id.dead_line, group.group_id.create_date, group.group_id.special_key, group.group_id.password))
    template = loader.get_template('my_groups.html')
    contents = {
        'my_groups': all_groups_list,
        'name': userinfo
    }
    return HttpResponse(template.render(contents, request))


def group_details(request, variable_id):
    user_id = Users.objects.get(username=userinfo).id
    member_validity = Group_members.objects.filter(group_id=All_groups.objects.get(id=variable_id)).all()
    member_list = []
    for member in member_validity:
        member_list.append(member.user_id.id)
    if user_id in member_list:
        value = variable_id
        print(f'value->: {value}')
        if entry != True:
            return redirect(reverse('login'))
        members = Group_members.objects.select_related('user_id', 'group_id').all()
        members_list = []
        for member in members:
            members_list.append((member.id, member.group_id.name, member.group_id.min_price, member.group_id.special_key, member.group_id.dead_line, member.user_id.id, member.user_id.username))
        all_wishes = Wishes.objects.select_related('user_id', 'group_id').filter(group_id=All_groups.objects.get(id=value)).all()
        all_wishes_list = []
        for wish in all_wishes:
            all_wishes_list.append((wish.id, wish.name, wish.price, wish.user_id.id))
        wish_users = []
        no_wish_users = []
        wish_auth_id = Wishes.objects.filter(group_id=All_groups.objects.get(id=value)).all()
        wish_auth_id_list = []
        for wish_auth in wish_auth_id:
            wish_auth_id_list.append(wish_auth.user_id.id)
        my_id = Users.objects.filter(username=userinfo).all()
        for member in members_list:
            if member[5] in wish_auth_id_list:
                wish_users.append(member[6])
            else:
                no_wish_users.append(member[6])
        leader_id = All_groups.objects.filter(id=value).get()
        leader = False
        if leader_id.user_id == my_id.get():
            leader = True
        if 'create_wish' in request.POST:
            create_item_name = request.POST['create_item_name']
            create_item_price = request.POST['create_item_price']
            Wishes(
                user_id=my_id.get(),
                group_id=All_groups.objects.get(id=value),
                name=create_item_name,
                price=create_item_price
            ).save()
            return redirect(reverse('group_details', args=[variable_id]))
        if 'draw_names' in request.POST:
            import random
            peoples = Group_members.objects.filter(group_id=value).all()
            people_list = []
            for people in peoples:
                people_list.append(people.user_id.id)
            draw = {}
            i = 0
            while len(draw) < len(people_list):
                key = random.choice(people_list)
                value = random.choice(people_list)
                if key != value:
                    if key not in draw and value not in draw.values():
                        draw[key] = value
                    else:
                        i += 1
                        if i == 5:
                            draw.clear()
                            i = 0
                            continue
            for i in draw:
                the_id = Users.objects.get(id=i)
                Wishes.objects.filter(user_id=the_id).update(
                    drawn_user_id=draw[i]
                )
            return redirect(reverse('my_group'))
        if 'edit_wish' in request.POST:
            item_name = request.POST['item_name']
            item_price = request.POST['item_price']
            Wishes.objects.filter(group_id=All_groups.objects.get(id=value), user_id=my_id.get()).update(
                name=item_name,
                price=item_price
            )
            return redirect(reverse('group_details', args=[variable_id]))
        if 'chat' in request.POST:
            message = request.POST['message']
            print(value)
            Group_chat(
                chat=message,
                user_id=my_id.get(),
                group_id=All_groups.objects.get(id=value)
            ).save()
            return redirect(reverse('group_details', args=[variable_id]))
        all_chat = Group_chat.objects.select_related('user_id').filter(group_id=value).all().order_by('-id')
        try:
            drawn_name = Wishes.objects.filter(user_id=my_id.get(), group_id=All_groups.objects.get(id=value)).get().drawn_user_id.username
        except:
            drawn_name = None
        rand = Group_members.objects.filter(group_id=All_groups.objects.get(id=value)).all()
        rand_list = []
        for item in rand:
            rand_list.append(item)
        if len(rand_list) > 1:
            rand = True
        else:
            rand = False
        contents = {
            'yes_no': rand,
            'drawn_name': drawn_name,
            'chats': all_chat,
            'my_id': my_id.values()[0]['id'],
            'value': value,
            'members': members_list,
            'wishes': all_wishes_list,
            'wish_users': wish_users,
            'no_wish_users': no_wish_users,
            'leader': leader
        }
        print('\n\n\n\n\n\n\n\n\n\n')
        for content in contents:
            print(f'{content}: {contents[content]}')
        print('\n\n\n\n\n\n\n\n\n\n')
        template = loader.get_template('group_details.html')
        return HttpResponse(template.render(contents, request))