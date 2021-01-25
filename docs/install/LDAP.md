### 安装说明
> 一般公司都有自己的LDAP服务，因此这里只是介绍一下，搭建开发环境使用的ldap过程  
> 并且说明，此系统如何接入LDAP  
> 还是那句话，我不想弄一个通用的功能，因此如果想要接入已有的LDAP服务，可能需要修改代码逻辑  

#### 开发环境搭建
* 操作系统：Ubuntu 16.04.6 Server LTS
* 机器IP：192.168.50.101  
* 安装docker环境
> 因为是开发环境，所以还是用docker安装比较方便  

##### 安装openldap
```
docker run --restart=always -p 389:389 --name openldap \
    --network bridge --hostname openldap-host \
    --env LDAP_ORGANISATION=oldb --env LDAP_DOMAIN=oldb.top \
    --env LDAP_ADMIN_PASSWORD=ldap123 -d osixia/openldap
```
> openldap默认使用端口是389，并且一般389端口确实没有被占用，所以直接使用389:389  
> LDAP_ORGANISATION=oldb: 组织名称，自己根据实际设置   
> LDAP_DOMAIN=oldb.top: 这里的oldb.top是我自己的一个域名名称所以直接这么用了  
> LDAP_ADMIN_PASSWORD=ldap123: 指定密码，随便设置  

##### 安装phpldapadmin
```
docker run --restart=always --name phpldapadmin -p 9999:80 \
    --env PHPLDAPADMIN_HTTPS=false --env PHPLDAPADMIN_LDAP_HOSTS=192.168.50.101 \
    -d osixia/phpldapadmin
```
> phpldapadmin是操作ldap的界面，你可以不用(可以自己写一个^@)  
> 默认端口80，但是机器上80已经被nginx占用了，所以映射到9999  
> PHPLDAPADMIN_LDAP_HOSTS=192.168.50.101: 指定ldap服务所有机器IP(因为是一台机器上，所以指定当前机器IP)
> 在生产环境，最好配置成域名  

##### 访问
```
访问地址：http://192.168.50.101:9999
账号：cn=admin,dc=oldb,dc=top
密码：ldap123
```

##### 使用策略
> 在根节点下创建两个组，一个组名叫group，一个组名叫member  
> 创建方法: Create a child entry -> Generic: Posix Group  
> group: 此组下用来创建其它组(Generic: Posix Group)  
> member: 此组下用来创建用户(Generic: User Account), 所有用户都放在这下面  
> 至于组和用户之间的关系可以通过在对应组下执行：  
> Add new attribute -> memberUid  
> 这样就可以在组下关联多个用户了  

##### 使用示例
> 在cn=member,dc=oldb,dc=top下创建用户buxingxing  
> Create a child entry -> Generic: User Account  
> 填写如下信息：

```
Last name: 卜星星
Common Name: buxingxing
User ID: buxingxing
Password: 123456
GID Number: member
```

> Last name: 用来存储用户中文名  
> Common Name: 存储username  
> 其实Common Name和User ID我都存储了username，但是具体可以根据实际情况来设置  
> 比如Common Name可以是邮箱，User ID可以是公司其它系统的用户ID等等  
> 但是我这里就这么用了  
