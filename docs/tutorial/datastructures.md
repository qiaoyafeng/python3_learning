# 5. 数据结构

本章将详细介绍一些您已经了解的内容，并添加了一些新内容。

## 5.1. 列表的更多特性

列表数据类型还有很多的方法。这里是列表对象方法的清单：


list.append(x)

    在列表的末尾添加一个元素。相当于 a[len(a):] = [x] 。

list.extend(iterable)

    使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable 。

list.insert(i, x)

    在给定的位置插入一个元素。第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x) 。

list.remove(x)

    移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常。

list.pop([i])

    删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。（ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。

list.clear()

    删除列表中所有的元素。相当于 del a[:] 。

list.index(x[, start[, end]])

    返回列表中第一个值为 x 的元素的从零开始的索引。如果没有这样的元素将会抛出 ValueError 异常。

    可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

list.count(x)

    返回元素 x 在列表中出现的次数。

list.sort(*, key=None, reverse=False)

    对列表中的元素进行排序（参数可用于自定义排序，解释请参见 sorted()）。

list.reverse()

    反转列表中的元素。

list.copy()

    返回列表的一个浅拷贝。相当于 a[:] 。

列表方法示例：

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>>
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
>>>
```
你可能已经注意到，像 insert ，remove 或者 sort 方法，只修改列表，没有打印出返回值——它们返回默认值 None 。[注脚1](#脚注1) 这是Python中所有可变数据结构的设计原则。

你可能会注意到的另一件事是并非所有数据或可以排序或比较。 例如，[None, 'hello', 10] 就不可排序，因为整数不能与字符串比较，而 None 不能与其他类型比较。 并且还存在一些没有定义顺序关系的类型。 例如，3+4j < 5+7j 就不是一个合法的比较。

### 5.1.1. 列表作为栈使用

### 5.1.2. 列表作为队列使用

### 5.1.3. 列表推导式

### 5.1.4. 嵌套的列表推导式

## 5.2. del 语句

## 5.3. 元组和序列

## 5.4. 集合

## 5.5. 字典

## 5.6. 循环的技巧

## 5.7. 深入条件控制

## 5.8. 序列和其它类型的比较


**脚注**

[脚注1]: 别的语言可能会返回一个可变对象，他们允许方法连续执行，例如 d->insert("a")->remove("b")->sort();。