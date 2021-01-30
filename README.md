### 说在前面
欢迎点Star  
* 有人点Star，说明被需要，我可以加快开发进度
* 如果Star多，更容易被需要的人看到

### 项目渊源
rurality: 田园生活  
enjoy: 荫照椅(早晨和黄昏照射着阳光，午后又遮挡在树荫下的椅子)  
darling: 达令  
> 寓意着从重复的工作中解脱出来，和自己的达令坐在荫照椅上，享受着田园生活  

### 目的
设计一款更人性的运维平台  

* 如果你想找运维平台的设计思路，那么它就是一个设计思路
* 如果你想开发一套自己的运维平台，那么它就是一个开发起点
* 如果你想学习python/django开发，那么它就是一个开发教程

> 项目中有关IT资源都是基于阿里云的，如果要接入其它平台，我认为很容易修改(即使是混合云)  

### 体验说明
* [体验地址: http://39.105.71.60](http://39.105.71.60)(有点懒的备案)  
* 体验系统管理账号: admin/123456 (超级管理员，需要取消LDAP用户选项)  
* 体验业务操作账号: buxingxing/123456 (管理员, 需要选中LDAP用户选项)  

##### 体验及提示
* 请不要将自己实际账号等重要信息填写到体验系统中，如果因此造成损失作者不承担责任  
* 体验地址主要是体验整个控制界面及流程，如果要实际操作，可以本地部署测试  

### 安装教程
[开发环境安装文档](https://github.com/bxxfighting/rurality/blob/master/docs/install/README.md)  

### 开发教程
[开发教程](https://github.com/bxxfighting/rurality/blob/master/docs/develop/README.md)  
[后端代码库](https://github.com/bxxfighting/rurality)  
[前端代码库](https://github.com/bxxfighting/enjoy)  
[流水线代码库](https://github.com/bxxfighting/darling)  

<details>
<summary>第一章 美好生活的开启</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/1.md">第一节 开启美好生活</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/2.md">第二节 增加常用的工具方法</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/3.md">第三节 增加基础错误及基础类型校验</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/4.md">第四节 根据自己的需求删减django中间件及apps</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/5.md">第五节 定制自己的基础model</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/6.md">第六节 定制自己的基础api</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/7.md">第七节 增加依赖管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/8.md">第八节 定义用户model</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/9.md">第九节 角色与部门</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/10.md">第十节 模块与权限</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/11.md">第十一节 基础操作model对象方法</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/12.md">第十二节 配置数据库</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/13.md">第十三节 跨域配置</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/14.md">第十四节 创建超级管理员账号</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/15.md">第十五节 运行服务(gunicorn)</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/16.md">第十六节 第一个接口：登录</a>
</code></pre>
</details>

<details>
<summary>第二章 努力的积淀</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/enjoy/blob/master/how/to/do/1.md">第一节 开辟新战场</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/1.md">第二节 模块基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/2.md">第三节 权限基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/3.md">第四节 部门基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/4.md">第五节 角色基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/5.md">第六节 用户基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/6.md">第七节 接口并发请求锁</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/7.md">第八节 完善所有接口的并发处理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/8.md">第九节 用户\角色\模块\部门\权限关联关系接口</a>
</code></pre>
</details>
<details>
<summary>第三章 画画的北北</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/1.md">第一节 前后开工</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/2.md">第二节 写一个mod模块玩玩</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/3.md">第三节 是时候展示复制粘贴的魅力了</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/4.md">第四节 继续感受复制粘贴的强大</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/5.md">第五节 无规矩不成方圆</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/6.md">第六节 整点实际的</a>
</code></pre>
</details>
<details>
<summary>第四章 完善基础支撑功能</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/4/1.md">第一节 啥系统都得有任务</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/4/2.md">第二节 总得有日志吧?</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/4/3.md">第三节 防背锅手册</a>
</code></pre>
</details>
<details>
<summary>第五章 拥抱阿里云</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/1.md">第一节 开启阿里云的钥匙</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/2.md">第二节 阿里云资产模块管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/3.md">第三节 阿里云地域、可用区管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/4.md">第四节 环境管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/5.md">第五节 先玩玩阿里云ECS</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/6.md">第六节 服务配置需要用到的资产模块</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/7.md">第七节 服务与ECS有个约会</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/8.md">第八节 干SLB</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/9.md">第九节 服务关联SLB服务器组</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/10.md">第十节 干RDS</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/11.md">第十一节 服务关联数据库</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/12.md">第十二节 干Redis</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/13.md">第十三节 干Mongo</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/14.md">第十四节 域名也得管理上</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/15.md">第十五节 MQ中选一个写写(RocketMQ)</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/16.md">第十六节 便捷万岁</a>
</code></pre>
</details>
<details>
<summary>第六章 来点正经的</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/1.md">第一节 统一任务管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/2.md">第二节 引用代码库管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/3.md">第三节 服务增加编程语言、框架、代码库属性</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/4.md">第四节 服务基础部署配置</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/5.md">第五节 Jenkins管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/6.md">第六节 接入LDAP</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/7.md">第七节 数据权限之密码权限管理</a>
</code></pre>
</details>

### 使用教程
目前项目处于开发阶段，预计发布1.0.0版本时，会增加使用教程  

### TODO
* 增加阿里云资源的增删改操作(服务增加机器、增加域名等一系列相关操作)
* 接入jumpserver
* 服务配置管理(服务的业务配置/nginx配置等)
* 工单审批(工单审批完成自动触发各种功能任务)

### 赞助支持
哈哈，支付宝收款码在此，一分不嫌少，一元不嫌多，就是图一个乐子  
<img src="https://i.loli.net/2021/01/27/LPSvRCFqfI46xEY.jpg" width="300" hegiht="300" />

[赞助名单](https://github.com/bxxfighting/rurality/blob/master/data/sponsor/README.md)

### 免责声明
* 本项目属于教学及体验设计，如果在生产环境使用，请进行充分测试与评估，出现任何问题作者不承担任何责任  
