# 示例一
有一些人来参加宴会，但是宴会规定，只有名字叫卜星星的才能吃饭及进行一些其它活动  
这时候有两种写法  
* 第一种
```
names = ['lisi', 'wanger', 'buxingxing', 'zhangsan', 'buxingxing']
for name in names:
    if name == 'buxingxing':
        print(f"{name}可以吃饭")
        # TODO
```

* 第二种
```
names = ['lisi', 'wanger', 'buxingxing', 'zhangsan', 'buxingxing']
for name in names:
    if name != 'buxingxing':
        continue
    print(f"{name}可以吃饭")
    # TODO
```
> 如果是我，就会写成第二种，因为我认为这样写逻辑会更清晰，并且代码结构要更好看  

# 示例二
变量名复用
可以免去起名的烦恼，同时也方便其它功能复制粘贴后，改更少的内容
```
data = {
    'result': {
        'data': {
            'names': ['lisi', 'wanger', 'buxingxing', 'zhangsan', 'buxingxing']
        }
    }
}

data = data.get('result')
# TODO：增加校验
data = data.get('data')
# TODO：增加校验
data_list = data.get('names')
# TODO：增加校验
for data in data_list:
    if data != 'buxingxing':
        continue
    print(f"{data}可以吃饭")
    # TODO
```
> 这里面一个data变量，从上面一直用到下面，省去了来回起名字的麻烦  
> 但是这仅限于，前面的变量后面不会再用到的情况(很多时候确实是这样的)  
> 为什么没有用data['result']['data']['names']?  
> 因为其中有些值可能是不存在的，会在中间增加一起验证，如果不存在可能会有其它逻辑处理  
> 有人觉得这是python的弊端，但是这是我热爱python的一点  
> 就像以前写c语言一样，有人说switch case应该默认break，所以说C语言有问题一样  
> 但是实际情况是你用一样东西，你就应该明白它的特性，你总不能买了一把刀，说这刀太锋利，容易割到手  
