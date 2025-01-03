创建github repo, 共享给我, 每次上传到github

1.5 hour per day

数据类型和运算(int, float, bool, str; + ,-, *, /, **, //, %, &, |, ^)(✅)
*data_type_and_operation.py*

顺序语句(✅)(day 1)、判断语句(✅)、循环语句(✅)   
*judge_and_loop.py*

函数(✅)(day2)、lambda表达式(方便、紧凑、简洁)(✅)
*function.py*

try except语句(✅)

内置函数(sorted, min/max/sum, len)(✅)


数据结构: 
- list(✅)(day3)
- dict(✅)
- tuple(✅)
- set(✅)
构建、方法、转化、遍历   
*data_structure.py*

list comprehension (map, filter, reduce)(✅) (各种判断质数) (day4, 2.5h)
8皇后问题


* 类(对象)(✅)、初始化(✅)、继承(✅)
  * 类/对象(模版和实例化) 成员变量(属性)、成员函数(方法)(✅)
  * 静态变量、方法(✅)
* 抽象基类(✅)、公有/保护(弱私有)/私有(强私有)(✅)(day5, 2h) chessboard习题(构建engine用于后续的桌面应用和web应用, LY compete!)
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

dataclass类: 当使用类来保存数据的时候，可以使用这个类

先从一些轻松的开始 

命名系统: 大/小写下划线 大/小驼峰 在Python的默认规范(✅)
* 大写下划线: 常量  MAX_SIZE
* 小写下划线: 变量、函数名、模块名、成员变量、成员函数 cur_size

decorator (是否带参数)可以装饰函数、类、类的成员函数  系统自带decorator(property, classmethod, staticmethod)(✅)
例子: 计时、register(✅)

file io (✅)
* open(r, w, a+) read/readlines/write (✅)
* contextmanager enter/exit (✅)
* json (✅)(day6, 2.5h)

每次先git pull 
最后git push

import package (module, package)(✅)
* absolute import file 表示当前运行python指令的路径下 file(✅)
* relative import .file .表示所在文件的相对路径(实际执行时会把相对路径转为绝对路径)(✅)
* 多个import太长可以用括号括起来，多行书写
``` python
from typing import (
    Generic,
    Iterable,
    Iterator,
)
```

(做leetcode题目)

iterable & iterator / generator(yield关键字) / for loop(✅)
[python doc][https://docs.python.org/3/glossary.html#term-iterable]


多进程/多线程 (✅)
* 数据并行处理 apply_async(✅) 
* 与函数式结合 (list comprehension的并行版) imap (✅)(day7, 2h) 

note: 再补充一下Process, map, apply (windows运行有bug, 解决了, 需要放在__main__中)
* map, imap, map_async (✅)
* apply, apply_async  (加async的是不block主程序的的, 不加是阻塞的,pool.close()+pool.join()可以等待async的任务运行完) (✅)
* p = mp.Process(target=task, args=iterable) iterable一般就是tuple (✅)
p.start() p.join() (✅)

**如何获取返回值没讲清**

正则表达式 re (详见python summary / advance_knowledge / 7)
* pattern = re.compile(r'pattern') (✅)
* result = pattern.findall(content) 可以通过()group来获取匹配后需要的部分 (✅)(day8, 3h)
[正则表达式中的特殊符号含义][https://www.w3schools.com/python/python_regex.asp] 
爬虫解析网页可以直接用beautifulsoup4, 内部已经用正则表达式实现好了常见匹配和文本提取

路径相关的package (✅)
os / glob / pathlib (非常方便, 可以替代前两个)
[glob介绍][https://blog.csdn.net/qq_42681787/article/details/127789869]
[非常好的pathlib总结，可以当作手册查看][https://zhuanlan.zhihu.com/p/475661402]

os.system(cmd) / os.popen(cmd).read() 在命令行运行指令(并获取标准输出) (✅)

sys
* sys.argv 用于获取命令行参数
* sys.path.append(path) 向sys.path中添加path, 用于import package (✅)

argparse (命令行参数解析 CLI) (✅) (day9, 2h)

type hint [知乎介绍](https://zhuanlan.zhihu.com/p/637347770), [官方文档](https://peps.python.org/pep-0484/) 程序运行并不会强制要求，是给静态类型检查器看的，然后提示代码中的类型错误
常见类型:  (✅) 
* int, str, float, bool
* List[int]
* Optional[int]
* Union[int, str]
* Any
* Tuple[int, str]
* Sequence[int]
* Callable[[int, int], int]
* Literal[1, 2, 3]
* Newtype('NewTypeName', int) # 主要是给静态类型检查器看的 [介绍](http://www.manongjc.com/detail/60-ncokloueevpddvk.html)
* Generic(泛型) # 好像是和TypeVar连用, 用于定义泛型类, 表示某一类变量，要求类的内部一致 [介绍](https://stackoverflow.com/questions/58755948/what-is-the-difference-between-typevar-and-newtype)
  
super and MRO (method resolution order)  (✅)  (day10, 50min)

梳理基本的数据结构和操作及其复杂度list/dict/set/str
进制转换bin()/oct()/hex()等
字符和ascii码的转换ord()/chr() ord是unicode ordinal的缩写,即编号; chr是character的缩写
[bisect库](https://blog.csdn.net/weixin_43955170/article/details/119085829)

做完题后总结一下用到的数据结构、接口和算法思想

important basic packages for data analysis / visualization (that's why python dominates data science programming)
* numpy 
* pandas 
* matplotlib (seaborn) [tutorial](https://matplotlib.org/stable/tutorials/index.html#tutorials), [gallery](https://matplotlib.org/stable/gallery/), [seaborn tutorial](https://seaborn.pydata.org/tutorial/distributions.html), [seaborn gallery](https://seaborn.pydata.org/examples/index.html)
[python plot gallery](https://python-graph-gallery.com/)
作图基本原理:
点/线图，画图的style(点型/线型)
坐标轴的style(刻度/刻度标签)、标题、图例
文字的style(字体/大小/颜色)
选色、配色
额外添加文字/箭头   # 添加箭头也许在ppt里比较方便

在哪、放什么(内容、样式)、怎么放

dataframe & series: 表格型数据结构, 底层数据结构采用NumPy来实现

前端 (server) (暂时不熟悉)
* html
* css
* javascript

爬虫 (暂时不熟悉)
* 根据url获取网页内容
* 解析网页内容
* 获取新的url继续爬取 (需要先了解网站结构)

数据科学/机器学习 (kaggle竞赛)
* sklearn
* pytorch
* tensorflow (暂时不熟悉)
会使用别人开发的包和仓库（经常用到）, 会阅读文档, 会查看源码

web应用程序开发框架(后端 server): django / flask (暂时不熟悉) (postman做测试, sqlite viewer查看数据库)

linux基本指令(一切靠点鼠标的操作都可以用命令行实现)
> 命令行trick: 上翻/下翻, tab补全, ctrl+a/e移动到开头/结尾    
> 查看操作(ls, vim, cat, head, tail, more)   
> 文件操作(mkdir, touch, mv, cp, vim), 查找操作(find, grep)  
> 文件权限(chmod, chown, chgrp) 会看含义 
> 文本处理(字符流处理) sed (stream editor)    
> 管道操作 |   
> 重定向 >, <, &>     
> top, htop, ps (aux), kill, nvidia-smi -l 1   
> ifconfig, ping, ssh, scp, wget     
> tmux   

grep -r "keyword" folder_path 递归查找folder_path目录下的文件中包含keyword的行
find folder_path -name "keyword" 递归查找folder_path目录下的文件名包含keyword的文件和文件夹
grep和find路径和模式匹配的顺序是反的
du -sh file/folder s表示summarize, h表示human readable, 以M为单位
top -p pid 查看pid进程的资源占用情况
top -u username 查看user`name用户的资源占用情况
按q退出top

1. 高级语言、汇编语言、机器码
    * 编译器
    * 指令集 (例如x86)
2. `面向过程的编程`、``面向对象的编程``、```函数式编程```

写程序的基本: 语法+算法
* 命名规范
* 书写格式整洁清晰
* 会看报错来debug

写软件: 项目代码规范, 设计模式/架构，可扩展性, 维护、测试、部署

[面向对象][website]的开发，除了**基本的东西**用来实现*功能*，主要是根据***功能***设计`抽象`

[website]: https://baike.baidu.com/item/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1/2262089?fr=aladdin
[magic_method_bili]: https://www.bilibili.com/video/BV1b84y1e7hG/?spm_id_from=333.788&vd_source=2e11bf5777ff070409e5bbf74862f555
<u>***underline***</u>

不熟悉包括没学习过，或学习过但没怎么用过

了解计算机的各种编程语言和开发技术等工具，然后根据需求去使用工具来实现功能，来创造价值. 看到别人对工具的需求然后造铲子，也可以创造价值.



