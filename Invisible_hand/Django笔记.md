# Django笔记

### cd到文件夹：

#### cd /Users/MakerLike/Desktop/Invisible_hand_1.2/Invisible_Hand

### 开启一个项目：

#### django-admin startproject ...

### 启动服务器：

#### python3 manage.py runserver 0.0.0.0:8080

### 网址：

#### 127.0.0.1:8080/...

### 创建项目：

#### python3 manage.py startapp ...

### 写好迁移文件：

#### python3 manage.py makemigrations ...

### 进入迁移状态/实际开始迁移：

#### python3 manage.py migrate

### 让Django注意到新的app：

#### settings.py

#### INSTALLED_APPS = [        

#### 	'common.apps.CommonConfig',

#### ]

### 创建超级用户：

#### python3 manage.py createsuperuser

### 修改数据步骤：

#### 每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤:修改models.py;对 learning_logs调用makemigrations;让Django迁移项目。

### 云服务器账户： Administrator

### 云服务器密码： 5X)wzc{$mS|E8vy7