# 2. 使用 Python 解释器

## 2.1. 调用解释器

在Linux和Unix系统上Python通常安装在目录/usr/local/bin/python3.6 ，/usr/local/python 也是比较常用的备选路径。

Windows系统通常安装在C:\Python36，安装路径可以根据自己设置。

在Windows系统上，在DOS中可以输入以下命令设置Python环境： 

`set path=%path%;C:\python36`

输入 Python 后进入交互模式：

```bash
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\qiaoyafeng>set path=%path%;C:\python36

C:\Users\qiaoyafeng>python
Python 3.6.6rc1 (v3.6.6rc1:1015e38be4, Jun 12 2018, 08:38:06) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()

C:\Users\qiaoyafeng>

```

在主提示符中输入文件结束字符（在 Unix 系统中是 Control-D，Windows 系统中是 Control-Z）就退出解释器并返回退出状态为0。如果这样不管用，你还可以写这个命令退出：quit()。

### 2.1.1. 传入参数

解释器会读取命令行参数，转化为字符串列表存入 sys 模块中的 argv 变量中。

执行命令 import sys 你可以导入这个模块并访问这个列表。这个列表最少也会有一个元素；如果没有给定输入参数，sys.argv[0] 就是个空字符串。如果脚本名是 '-' （标准输入）时，sys.argv[0] 就是 '-'。

```python
C:\Users\qiaoyafeng>python
Python 3.6.6rc1 (v3.6.6rc1:1015e38be4, Jun 12 2018, 08:38:06) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.argv
['']
>>> sys.argv[0]
''
>>> quit()

C:\Users\qiaoyafeng>python -
Python 3.6.6rc1 (v3.6.6rc1:1015e38be4, Jun 12 2018, 08:38:06) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.argv
['-']
>>>
```

### 2.1.2. 交互模式

在这种模式中，它会显示 主提示符（primary prompt），提示输入下一条指令，通常用三个大于号（>>>）表示；连续输入行的时候，它会显示 次要提示符，默认是三个点（...）。进入解释器时，它会先显示欢迎信息、版本信息、版权声明，然后就会出现提示符：

```python
C:\Users\qiaoyafeng>python
Python 3.6.6rc1 (v3.6.6rc1:1015e38be4, Jun 12 2018, 08:38:06) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

多行指令需要在连续的多行中输入。比如，以 if 为例：

```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
>>>
```

## 2.2. 解释器的运行环境

### 2.2.1. 源文件的字符编码

默认情况下，Python 源码文件以 UTF-8 编码方式处理。在这种编码方式中，世界上大多数语言的字符都可以同时用于字符串字面值、变量或函数名称以及注释中——尽管标准库中只用常规的 ASCII 字符作为变量或函数名，而且任何可移植的代码都应该遵守此约定。要正确显示这些字符，你的编辑器必须能识别 UTF-8 编码，而且必须使用能支持打开的文件中所有字符的字体。

如果不使用默认编码，要声明文件所使用的编码，文件的 第一 行要写成特殊的注释。语法如下所示：

`# -*- coding: encoding -*-`

其中 encoding 可以是 Python 支持的任意一种 codecs。

比如，要声明使用 Windows-1252 编码，你的源码文件要写成：

`# -*- coding: cp1252 -*-`

关于 第一行 规则的一种例外情况是，源码以 UNIX “shebang” 行 开头。这种情况下，编码声明就要写在文件的第二行。例如：

```bash
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

备注

在Unix系统中，Python 3.x解释器默认安装后的执行文件并不叫作 python，这样才不会与同时安装的Python 2.x冲突。
