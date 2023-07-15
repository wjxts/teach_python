创建github repo, 共享给我, 每次上传到github

1.5 hour per day

数据类型和运算(int, float, bool, str; + ,-, *, /, **, //, %)(✅)

循序语句(✅)(day 1)、判断语句(✅)、循环语句(✅)   

函数(✅)(day2)、lambda表达式(方便、紧凑、简洁)(✅)

try except语句(✅)

内置函数(sorted, min/max/sum, len)(✅)


数据结构: 
- list(✅)(day3)
- dict(✅)
- tuple(✅)
- set(✅)
构建、方法、转化、遍历   

list comprehension (map, filter, reduce)(✅) (各种判断质数) (day4, 2.5h)
8皇后问题


* 类(对象)(✅)、初始化(✅)、继承(✅)
  * 类/对象(模版和实例化) 成员变量(属性)、成员函数(方法)(✅)
  * 静态变量、方法(✅)
* 抽象基类(✅)、公有/保护(弱私有)/私有(强私有)(✅)(day5, 2h) chessboard习题
* 内置函数 (dir, hasattr, isinstance, getattr, setattr)(✅)
* 魔法方法  (emulation, duck type) [B站非常好的讲魔法方法的系列视频][magic_method_bili]
  * __init__(✅)
  * __str__, __repr__(✅)
  * __call__(✅)
  * __getattr__, __getattribute__, __setattr__(✅)
  * 比较相关 __eq__, (le, lt, ge, gt, ne) (与sorted联用)(✅)
  * 运算相关 __add__, (sub, mul, matmul, truediv, ...)(✅)
  * __len__, __contains__ (为了使用len, in)(✅)
  * __getitem__ this[key], __index__ other[this](as key)(✅)
  * context manager (with ... as ...语句) __enter__, __exit__ (计时)(✅)

先从一些轻松的开始 

命名系统: 大/小写下划线 大/小驼峰 在Python的默认规范(✅)
* 大写下划线: 常量
* 小写下划线: 变量、函数名、模块名、成员变量、成员函数

decorator (是否带参数)可以装饰函数、类、类的成员函数  系统自带decorator(property, classmethod, staticmethod)(✅)
例子: 计时、register(✅)

file io (✅)
* open(r, w, a+) read/readlines/write (✅)
* contextmanager enter/exit (✅)
* json (✅)(day6, 2.5h)

import package (module, package )
* absolute import file 表示当前运行python指令的路径下 file
* relative import .file .表示所在文件的相对路径(实际执行时会把相对路径转为绝对路径)


(做leetcode题目)

iterable & iterator / generator(yield关键字) / for loop

多进程/多线程 
* 数据并行处理
* 与函数式结合 (list comprehension的并行版)

正则表达式 re

路径相关的package
io / glob / pathlib (非常方便, 可以替代前两个)

important packages (that's why python dominates data science programming)
* numpy 
* pandas
* matplotlib (seaborn)

爬虫
* 根据url获取网页内容
* 解析网页内容
* 获取新的url继续爬取

前端
* html
* css
* javescript

数据科学 (kaggle竞赛)
* sklearn
* pytorch
* tensorflow

web应用程序开发框架: django

linux基本指令(一切靠点鼠标的操作都可以用命令行实现)
> 命令行trick: 上翻/下翻, tab补全, ctrl+a/e移动到开头/结尾    
> 查看操作(ls, vim, cat, head, tail, more)   
> 文件操作(mkdir, touch, mv, cp, vim), 查找操作(find, grep)   
> 文本处理(字符流处理) sed (stream editor)    
> 管道操作 |   
> 重定向 >, <, &>     
> top, htop, ps (aux), kill, nvidia-smi -l 1   
> ifconfig, ping, ssh, scp, wget     
> tmux   

1. 高级语言、汇编语言、机器码
    * 编译器
    * 指令集 (例如x86)
2. `面向过程的编程`、``面向对象的编程``、```函数式编程```

写程序的基本: 语法+算法
写软件: 

[面向对象][website]的开发，除了**基本的东西**用来实现*功能*，主要是根据***功能***设计`抽象`

[website]: https://baike.baidu.com/item/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1/2262089?fr=aladdin
[magic_method_bili]: https://www.bilibili.com/video/BV1b84y1e7hG/?spm_id_from=333.788&vd_source=2e11bf5777ff070409e5bbf74862f555
<u>***underline***</u>
