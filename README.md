# DjangoWebDevOps
##### This is  DevOps-Manager-Platform  for Django WebUI .
 
 ##### 这是我的csdn博客地址：https://blog.csdn.net/qq_28513801/article/details/100750538
 email: 1300042631@qq.com
 
 > 先说一下，完成一半自己想做的项目的感受和经历。
 
> 这是一个从后台到前端独自完成的自己的项目，虽然这两天刚加入的功能还没有完全实现，但是也差不多存在一些功能了。
由于没有使用前端模板，所以代码写的很烂，期间遇到了很多问题，saltstack,zabbix等各种api的调用，
以及获取到的数据如何发到前端利用Echarts展示，等等，不过也学到了很多，特别是浏览需要调用的API接口，
像Zabbix，Saltstack等等。特别是如何调用API，官网是最好的，最有用的，最值得花时间去研究的。


>> 由于从zabbix–saltstack等API调用和后端接口书写以及前端Echarts数据图形展示，都是独自开发，
>> 由于一直在学云计算运维相关的知识，开发代码写的不好，请多多指教，不胜感激涕零。


实现思路
边学Django边规划着自己所谓的LINUX运维平台，初开始打算做这样的功能：

* 1） 最必不可少的就是主机资产管理了，无论是虚拟机还是服务器或者云主机，我们对他们各自的 - HostInfo都应该一目了然。 这里采用SaltStack调用收集主机配置信息，并且输入ip、ssh用户名和密码，自动部署salt-minion，主机自动添加到salt-master。涉及到前端窗口输入命令结果返回，采用Prism高亮展示代码。

* 2） 可能是因为当初做PAAS运维的时候，一直在docker的rancerUI上操作各种监控相关的应用，像Granafa,普罗米修斯，Zabbix,ELS等以鲜艳的图形向我们展示她所监控的各种信息。所以觉得监控和图形也是必不可少，像流量图，CPU负载使用率，Memory使用率等图也应该存在。

* 3） 运维的话，那么自动化运维工具当然也必不可少，像Ansible自动化运维工具，SaltStack自动化运维工具，目前为止，我只用过这两个，所以UI界面也应该存在Dalang形式的针对于LINUX的CLI环境下操作的功能。

* 4)那么自动化也应该必不可少，XX一键部署，比如前段时间刚接触K8S时，写得不成熟的利用Kubeadm部署最新版的1.15.1的自动化脚本，和之前HADOOP完全分布式二进制部署时的一键脚本，以及先电云计算平台的PAAS，一键部署脚本等，所以，UI界面也应该存在XX一键部署功能。

* 5） 觉得成熟的平台，应该也存在SQL语句转化和SQL语句评分的功能，因为数据库非常重要，那么用优良的SQL语句操作必然更为重要。

* 6） 平台上也应该存在我觉得运维最为重要的标志------日志。所以这个运维平台的UI界面应该具备日志管理功能，能够在大量的日志中，过滤出关键字，并图形化的展示出来，好减少运维人员的痛苦。

* 7） 我认为这个平台还应该具备UI下操作，用户权限管理功能，避免某些用户执行rm -rf…
 
|软件	|版本|
|:---|:---|
|ZABBIX	|V3.4
|Python|	V3.6
|Django	|V1.95
|bootstrap	|v3.30
|Mysql	|v5.7
|saltstack	|v2019.2.0 (Fluorine)
|Centos	|CentOS-7-x86_64-DVD-1511
|Pycharm(专业版)	|v2019.2.x
|Docker	|v18.3
|Grafana（测试API）|	v5.6
|Echarts	|官网最新版（开发者版完整版）

![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/shouye.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/shouyecaidan.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/cmd.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/zican.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tinajiazhuji.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua1.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua2.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua3.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua4.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua5.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua6.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua7.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua8.png) 
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua9.png)
![image](https://github.com/pwxwmm/DjangoWebDevOps/blob/master/DisplayImages/tuxinghua10.png) 
 


### 一、部署的方法：

##### 第一种方法：

>可以选择在WIN环境下，调试，使用Pycharm进行部署，运行runserver，打开浏览器就能访问了。

下面是细节：

* 1,先下载专业版的Pycharm，选择Django模板，这里如果Django使用的是v2.X版本的话，会报一些警告，因为1.95和2.x的平台会有些不兼容，比如urls.py文件内容的书写格式，有很大偏差，建议没有特殊要求，就直接使用1.95。

* 2,首先使用pycharm导入这个项目目录，并且要先安装好MYSQL，建议二进制安装。并配置好。

* 3,其次在Pycharm的Django中，也要能成功连接MYSQL，修改好setting.py后，最好再测试一下。

* 4,紧接着在models.py文件中写好自己的数据模型，Django会自己帮你生成你需要的数据表，如果暂时没有其他额外需求，可以不修改我这里的models.py文件。

* 5,执行数据迁移。打开pycharm的terminal窗口，默认路径即可，执行py manage.py makemigrations webserver . 继续执行py manage.py migrate webserver
如果没有报异常，那么就可以打开migrations这个目录，看一下0001_initial.py这个文件的内容，或者使用命令python manage.py showmigrations直接输出迁移内容。

* 6,最重要的是要检查下模块的依赖性，这里最难导入的模块就是saltstack模块，使用pip导入的时候，尽可能的加个–timeout参数把默认超时时间15s加大一下.然后运行服务，打开浏览器，输入自己配置的django的IP+端口号，就可以访问啦。



##### 第二种方法：

> 使用Docker-compose部署Django环境，这种方法是在linux环境下部署的，或者你购买的云主机服务器等。

1,可以先安装Docker,然后执行命令启动：
```bash
[root@master ~]# systemctl start docker
[root@master ~]# systemctl enable docker
```
2,把所有能用到的镜像都pull下来，可以使用自己的dockerHub或者使用阿里云的，
```
[root@master ~]# docker pull mysql
[root@master ~]# docker pull django:1.9.5
[root@master ~]# docker pull python:3.6.0
[root@master ~]# mkdir -p /mysite/{DjangoWeb,db}
```
3,Dockerfile包含创建镜像所需要的全部指令。在项目根目录下创建Dockerfile文件，其内容如下

```bash
[root@master mysite]# vim /mysite/Dockerfile
FROM python:3.6.0   #ROM指令表示新的镜像将基于python:2.7的镜像来构建
ENV PYTHONUNBUFFERED 1     #ENV为环境变量（PYTHONUNBUFFERED见这里）
RUN mkdir /code     # RUN指令表示在镜像内新建/code目录
RUN mkdir /code/db   
WORKDIR /code     # 指定RUN、CMD与ENTRYPOINT命令的工作目录
ADD ./DjangoWeb/requirements.txt /code/    # 将./mysite/requirements.txt文件添加到刚才新建的code目录中
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt   # 运行pip安装所需的软件
ADD . /code/
```

4.在Dockerfile定义了一个应用，而使用compose，可以在一个文件里，定义多容器的应用。该YAML配置语言，用于描述和组装多容器的分布式应用。在项目根目录创建
docker-compose.yml文件，其内容如下：

```yaml
[root@master mysite]#  vim /mysite/docker-compose.yml
db:     #db标签
  image: mysql     # images表示使用mysql镜像
  expose:     # expose表示暴露端口3306，但不发布到宿主机上
    - "3306"   
  volumes:    # volume表示挂载宿主机的路径作为卷，冒号左边为宿主机路径，右边为镜像内路径
    - ./db:/var/lib/mysql
  environment:     # environment为环境变量，每个容器都有自己定义的环境变量，具体查看镜像手册中的mysql
    - MYSQL_DATABASE=mysitedb
    - MYSQL_ROOT_PASSWORD=888888

web:     # web标签：
  build: .   # build指定建立Dockerfile路径
  command: python ./DjangoWeb/manage.py runserver 0.0.0.0:8000    # command将覆盖默认的命令
  volumes:  
    - .:/code
  ports:   # ports指定主机开放的端口
    - "8000:8000"
  links:   # links指向其他容器中的服务
    - db
```
5，在子目录mysite下requirements.txt文件，该文件内容如下:

```
[root@master mysite]# vim /mysite/DjangoWeb/requirements.txt 

django==1.9.5
mysqlclient
django-admin-bootstrapped
django_bootstrap3
pillow
salt
```
6,构建镜像:

```bash
[root@master mysite]# cd /mysite
[root@master mysite]# docker-compose build
[root@master mysite]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mysite_web          latest              4306618s87c7        6 minutes ago       720.5 MB
docker.io/mysql     latest              b4e78b89bcf3        9 months ago        412.3 MB
docker.io/python    3.6.0               a1782fa44ef7        4 months ago        687.1 MB
docker.io/django    1.9.5               c5b6e7c5c44c        11 months ago       433.4 MB


[root@master mysite]#  docker-compose run web django-admin.py startproject webserver ./DjangoWeb

[root@master mysite]#  docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                     PORTS               NAMES
ad0c75e2fd3d        mysite_web          "django-admin.py star"   5 minutes ago       Exited (0) 5 minutes ago                       mysite_web_run_1
77e91e05178d        mysql               "docker-entrypoint.sh"   5 minutes ago       Up 5 minutes               3306/tcp            mysite_db_1

[root@master mysite]#  chmod -R 777 DjangoWeb
[root@master mysite]#  vim DjangoWeb/webserver/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysitedb',
        'USER': 'root',
        'PASSWORD': '888888',
        'HOST': 'db',
        'PORT': 3306,
    }
}
```

添加net端口映射:

```yaml
[root@master DjangoWeb]# docker inspect 1bf8642343e3 | grep IPAddress    #这里的inspect命令很强大
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.3",
                    "IPAddress": "172.17.0.3",

[root@master DjangoWeb]# iptables -t nat -A  DOCKER -p tcp --dport 80 -j DNAT --to-destination 172.17.0.3:8000     
```
7， 移入项目到新的创建的项目中，执行数据迁移：
这里要注意最好是在manage.py的目录下执行：
```python
python manage.py makemigrations 
python manage.py migrate
```
8，创建超级用户
```python
python manage.py createsuperuser 
```
9,进入mysite目录，启动容器
```
docker-compose up
```
有关Docker-compose的相关操作，我已经在上面添加了链接，可以了解一下，该流程和操作。
