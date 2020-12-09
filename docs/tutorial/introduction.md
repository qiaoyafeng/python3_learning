# 3. Python 的非正式介绍

Python中的注释以井号 # 开头，并且一直延伸到该文本行结束为止。注释可以出现在一行的开头或者是空白和代码的后边，但是不能出现在字符串中间。

几个例子:

```python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

## 3.1. Python 作为计算器使用

让我们尝试一些简单的 Python 命令。启动解释器，等待界面中的提示符，>>> （这应该花不了多少时间）。


### 3.1.1. 数字

解释器就像一个简单的计算器一样：你可以在里面输入一个表达式然后它会写出答案。 表达式的语法很直接：运算符 +、-、*、/ 的用法和其他大部分语言一样（比如 Pascal 或者 C 语言）；括号 (()) 用来分组。比如:

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 /5  # division always returns a floating point number
1.6
>>>
```
除法运算 (/) 永远返回浮点数类型。如果要做 floor division 得到一个整数结果（忽略小数部分）你可以使用 // 运算符；如果要计算余数，可以使用 %

```python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3 # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
>>>
```

在Python中，可以使用 ** 运算符来计算乘方 [备注1](#备注1)

```python
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 7 # 2 to the power of 7
128
>>>
```

等号 (=) 用于给一个变量赋值。

```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>>
```

如果一个变量未定义（未赋值），试图使用它时会向你提示错误:

```python
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>>
```

Python中提供浮点数的完整支持；包含多种混合类型运算数的运算会把整数转换为浮点数:

```python
>>> 4 * 3.75 - 1
14.0
>>>
```

在交互模式下，上一次打印出来的表达式被赋值给变量 _。这意味着当你把Python用作桌面计算器时，继续计算会相对简单，比如:

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> _
113.06
>>>
```

这个变量应该被使用者当作是只读类型。不要向它显式地赋值——你会创建一个和它名字相同独立的本地变量，它会使用魔法行为屏蔽内部变量。

### 3.1.2. 字符串

除了数字，Python 也可以操作字符串。字符串有多种形式，可以使用单引号（'...'），双引号（"..."）都可以获得同样的结果 [2](#备注2)。反斜杠 \ 可以用来转义:

```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> '"Yes,"  they said.'
'"Yes,"  they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>>
```

print() 函数会生成可读性更强的输出，即略去两边的引号，并且打印出经过转义的特殊字符:

```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
>>>
```

如果你不希望前置了 \ 的字符转义成特殊字符，可以使用 原始字符串 方式，在引号前添加 r 即可:

```python
>>> print('C:\\users\nqiaoyafeng')  # here \n means newline
C:\users
qiaoyafeng
>>>
>>>
>>> print(r'C:\\users\nqiaoyafeng')  # note the r before the quote
C:\\users\nqiaoyafeng
>>>

```

字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可。如下例:

```python
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
```

将产生如下输出（注意最开始的换行没有包括进来）:

```python
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

```

字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复:

```python
>>> 3 * 'un' + 'ium'
'unununium'
>>>
```

相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.
```python
>>> "Py"  'thon'
'Python'
>>>

```

把很长的字符串拆开分别输入的时候尤其有用:
```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>>
```

只能对两个字面值这样操作，变量或表达式不行:

```python
>>> prefix = 'Py'
>>> prefix 'thon'
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ("un" * 3) 'ium'
  File "<stdin>", line 1
    ("un" * 3) 'ium'
                   ^
SyntaxError: invalid syntax
>>>
```
如果你想连接变量，或者连接变量和字面值，可以用 + 号:

```python
>>> prefix + 'thon'
'Python'
>>>
```

字符串是可以被 索引 （下标访问）的，第一个字符索引是 0。单个字符并没有特殊的类型，只是一个长度为一的字符串:

```python
>>> word = 'Python'
>>> word[0]
'P'
>>> word[3]
'h'
>>>
```

索引也可以用负数，这种会从右边开始数:

```python
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-4]
't'
>>>
```

注意 -0 和 0 是一样的，所以负数索引从 -1 开始。

除了索引，字符串还支持 切片。索引可以得到单个字符，而 切片 可以获取子字符串:

```python
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>>
```

注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s

```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>>
```

切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:

```python
>>> word[:2]
'Py'
>>> word[4:]
'on'
>>> word[-2:]
'on'
>>>
```

您也可以这么理解切片：将索引视作指向字符 之间 ，第一个字符的左侧标为0，最后一个字符的右侧标为 n ，其中 n 是字符串长度。例如:

```text
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

第一行数标注了字符串 0…6 的索引的位置，第二行标注了对应的负的索引。那么从 i 到 j 的切片就包括了标有 i 和 j 的位置之间的所有字符。

对于使用非负索引的切片，如果索引不越界，那么得到的切片长度就是起止索引之差。例如， word[1:3] 的长度为2。

试图使用过大的索引会产生一个错误:

```python
>>> word[42]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>>
```

但是，切片中的越界索引会被自动处理:
```python
>>> word[4:42]
'on'
>>> word[42:]
''
>>>
```

Python 中的字符串不能被修改，它们是 immutable 的。因此，向字符串的某个索引位置赋值会产生一个错误:

```python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

如果需要一个不同的字符串，应当新建一个:

```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>>
```

内建函数 len() 返回一个字符串的长度:

```python
>>> name = 'qiaoyafeng'
>>> len(name)
10
```


### 3.1.3. 列表

Python 中可以通过组合一些值得到多种 复合 数据类型。其中最常用的 列表 ，可以通过方括号括起、逗号分隔的一组值（元素）得到。一个 列表 可以包含不同类型的元素，但通常使用时各个元素类型相同:

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>>
```

像字符串一样，列表可以索引和切片：

```python
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3]
9
>>> squares[-3:]
[9, 16, 25]
>>>
```

所有的切片操作都返回一个新列表，这个新列表包含所需要的元素。就是说，如下的切片会返回列表的一个新的(浅)拷贝:

```python
>>> squares[:]
[1, 4, 9, 16, 25]
```

列表同样支持拼接操作:

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:

```python
>>> cubes = [1, 8, 27, 65, 125]
>>> cubes
[1, 8, 27, 65, 125]
>>> 4 ** 3
64
>>> cubes[3]
65
>>> 4 ** 3
64
>>> cubes[3] = _
>>> cubes[3]
64
>>> cubes
[1, 8, 27, 64, 125]
>>>
```

你也可以在列表末尾通过 append() 方法 来添加新元素（我们将在后面介绍有关方法的详情）:

```python
>>> cubes.append(216)
>>> cubes.append(7 ** 3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>>
```

给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:] = []
>>> letters
[]
```

内置函数 len() 也可以作用到列表上:

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

也可以嵌套列表 (创建包含其他列表的列表), 比如说:

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>>
```


## 3.2. 走向编程的第一步

斐波那契数列实例：

```python
>>> a, b = 0, 1
>>> while b < 10:
...     print(b)
...     a, b = b, a+b
...
1
1
2
3
5
8
>>>
```

print() 函数将所有传进来的参数值打印出来. 它和直接输入你要显示的表达式(比如我们之前在计算器的例子里做的)不一样， print() 能处理多个参数，包括浮点数，字符串。 字符串会打印不带引号的内容, 并且在参数项之间会插入一个空格, 这样你就可以很好的把东西格式化, 像这样:

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
>>>
```

关键字参数 end 可以用来取消输出后面的换行, 或使用另外一个字符串来结尾:

```python
>>> a, b = 0, 1
>>> while b < 1000:
...     print(b, end=',')
...     a, b = b, a+b
...
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,>>>
>>>
```


**备注**

[备注1]: 因为 ** 比 - 有更高的优先级, 所以 -3\*\*2 会被解释成 -(3\*\*2) ，因此结果是 -9. 为了避免这个并且得到结果 9, 你可以用这个式子 (-3)**2.  

[备注2]: 和其他语言不一样的是, 特殊字符比如说 \n 在单引号 ('...') 和双引号 ("...") 里有一样的意义. 这两种引号唯一的区别是，你不需要在单引号里转义双引号 " (但是你必须把单引号转义成 \') ， 反之亦然.
