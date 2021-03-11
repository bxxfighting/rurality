### 安装教程

#### 零、说在前面
> 因为这不是一个基础教程，只是简单的写一个安装运行过程  
> 并且也没有弄成一个一键部署的方式，我认为谁也不应该直接使用, 必须根据自己的实际情况改造才行  
> 而且需要经过充分测试，评估会使用  

#### 一、本地开发环境搭建

##### 1. 安装python环境

* python版本: 3.8.5
* 使用pyenv来创建虚拟环境[文档](https://github.com/bxxfighting/knowledge/blob/master/python/python%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.md)
* 进入安装好的虚拟环境

##### 2. 安装依赖组件
> 依赖mysql:5.7、redis:5.0.4、rabbitmq:3.7.8  
> 本地都使用docker安装  
* ```docker run --name mysql --restart=always -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7```
* ```docker run --name rabbitmq --restart=always -p 5672:5672 -p 15672:15672 -d rabbitmq:3.7.8```
* ```docker run --name redis --restart=always -p 6379:6379 -d redis:5.0.4```

##### 3. 运行后端服务

* 克隆后端代码```git clone git@github.com:bxxfighting/rurality.git```
* 安装python依赖库```pip install -r requirements.txt```
* 导入sql文件```data/sql/rurality.sql```
* python manage.py runserver 18000

##### 4. 运行前端服务

* 克隆前端代码```git clone git@github.com:bxxfighting/enjoy.git```
* 安装依赖```npm install```
* 运行服务```npm run dev```

#### 二、生产环境部署

##### 1. 运行后端服务
* ```gunicorn -c gunicorn.py rurality.wsgi:application```

##### 2. nginx配置后端服务
```
server {
        listen 80;
        listen [::]:80;

        server_name api-hello.oldb.top;

        root /var/www/rurality;
        index index.html;

        location / {
                proxy_redirect off;
                proxy_pass http://localhost:18785;
        }
}
```

##### 3. 部署前端
* 构建```npm run build:prod```
* 拷贝dist目录到服务器

##### 4. nginx配置前端
```
server {
    listen 80;
    listen [::]:80;
    server_name hello.oldb.top;

    root /var/www/enjoy/dist;
    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Static files
    location /static {
       alias /var/www/enjoy/dist/static;
    }
}
```
