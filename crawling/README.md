# 语言特性

1.谈谈对 Python 和其他语言的区别

2.简述解释型和编译型编程语言

3.Python 的解释器种类以及相关特点？

4.说说你知道的Python3 和 Python2 之间的区别？

5.Python3 和 Python2 中 int 和 long 区别？

6.xrange 和 range 的区别？

# 编码规范

7.什么是 PEP8?

8.了解 Python 之禅么？

9.了解 docstring 么？

10.了解类型注解么？

11.例举你知道 Python 对象的命名规范，例如方法或者类等

12.Python 中的注释有几种？

13.如何优雅的给一个函数加注释？

14.如何给变量加注释？

15.Python 代码缩进中是否支持 Tab 键和空格混用。

16.是否可以在一句 import 中导入多个库?

17.在给 Py 文件命名的时候需要注意什么?

18.例举几个规范 Python 代码风格的工具

# 数据类型

字符串

19.列举 Python 中的基本数据类型？

20.如何区别可变数据类型和不可变数据类型

21.将"hello world"转换为首字母大写"Hello World"

22.如何检测字符串中只含有数字?

23.将字符串"ilovechina"进行反转

24.Python 中的字符串格式化方式你知道哪些？

25.有一个字符串开头和末尾都有空格，比如“ adabdw ”,要求写一个函数把这个字符串的前后空格都去掉。

26.获取字符串”123456“最后的两个字符。

27.一个编码为 GBK 的字符串 S，要将其转成 UTF-8 编码的字符串，应如何操作？

28. (1)s="info：xiaoZhang 33 shandong"，用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong'](2) a = "你好 中国 "，去除多余空格只留一个空格。

29. (1)怎样将字符串转换为小写 (2)单引号、双引号、三引号的区别？

操作类题目

49.Python 交换两个变量的值

50.在读文件操作的时候会使用 read、readline 或者 readlines，简述它们各自的作用

51.json 序列化时，可以处理的数据类型有哪些？如何定制支持 datetime 类型？

52.json 序列化时，默认遇到中文会转换成 unicode，如果想要保留中文怎么办？

53.有两个磁盘文件 A 和 B，各存放一行字母，要求把这两个文件中的信息合并(按字母顺序排列)，输出到一个新文件 C 中。

54.如果当前的日期为 20190530，要求写一个函数输出 N 天后的日期，(比如 N 为 2，则输出 20190601)。

55.写一个函数，接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。

56.下面代码会存在什么问题，如何改进？




57.一行代码输出 1-100 之间的所有偶数。

58.with 语句的作用，写一段代码？

59.python 字典和 json 字符串相互转化方法

60.请写一个 Python 逻辑，计算一个文件中的大写字母数量

62.说一说 Redis 的基本类型。

1.  请写一段 Python连接 Redis 数据库的代码。

2.  请写一段 Python 连接 MySQL 数据库的代码。

65.了解 Redis 的事务么？

66.了解数据库的三范式么？

67.了解分布式锁么？

68.用 Python 实现一个 Reids 的分布式锁的功能。

69.写一段 Python 使用 Mongo 数据库创建索引的代码。

高级特性

70.函数装饰器有什么作用？请列举说明？

71.Python 垃圾回收机制？

72. How to use __call__ method?
implementing __call__ method makes an object of the current class callable.

74.@classmethod 和@staticmethod 用法和区别

75.Python 中的接口如何实现？

76.Python 中的反射了解么?

77.metaclass 作用？以及应用场景？

78.hasattr() getattr() setattr()的用法

79.请列举你知道的 Python 的魔法方法及用途。

80.如何知道一个 Python 对象的类型？

81.Python 的传参是传值还是传址？
传值

82.Python 中的元类(metaclass)使用举例

83.简述 any()和 all()方法

84.filter 方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

85.what is monkey patching？
(monkey patching)[https://web.archive.org/web/20120730014107/http://wiki.zope.org/zope2/MonkeyPatch] is an extension of an existing class. We can utilize this feature for testing our features that depend on current external stub. 

86.在 Python 中是如何管理内存的？

87.当退出 Python 时是否释放所有内存分配？

算法和数据结构

122.已知：
(1) 从 AList 和 BSet 中 查找 4，最坏时间复杂度那个大？

(2) 从 AList 和 BSet 中 插入 4，最坏时间复杂度那个大？

123.用 Python 实现一个二分查找的函数

124.python 单例模式的实现方法

125.使用 Python 实现一个斐波那契数列

126.找出列表中的重复数字

127.找出列表中的单个数字

128.写一个冒泡排序

129.写一个快速排序

130.写一个拓扑排序

131.python 实现一个二进制计算

132.有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。

133.单链表反转

134.交叉链表求交点

135.用队列实现栈

136.找出数据流的中位数

137.二叉搜索树中第 K 小的元素

爬虫相关

138.在 requests 模块中，requests.content 和 requests.text 什么区别

139.简要写一下 lxml 模块的使用方法框架

140.说一说 scrapy 的工作流程

141.scrapy 的去重原理

142.scrapy 中间件有几种类，你用过哪些中间件

143.你写爬虫的时候都遇到过什么？反爬虫措施，你是怎么解决的？

144.为什么会用到代理？

145.代理失效了怎么处理？

146.列出你知道 header 的内容以及信息

147.说一说打开浏览器访问 www.baidu.com 获取到结果，整个流程。

148.爬取速度过快出现了验证码怎么处理

149.scrapy 和 scrapy-redis 有什么区别？为什么选择 redis 数据库？

150.分布式爬虫主要解决什么问题

151.写爬虫是用多进程好？还是多线程好？ 为什么？

152.解析网页的解析器使用最多的是哪几个

153.需要登录的网页，如何解决同时限制 ip，cookie,session（其中有一些是动态生成的）在不使用动态爬取的情况下？

154.验证码的解决（简单的：对图像做处理后可以得到的，困难的：验证码是点击，拖动等动态进行的？）

155.使用最多的数据库（mysql，mongodb，redis 等），对他的理解？



