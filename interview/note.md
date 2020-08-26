## 1. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

Example 2:
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## 2.Implement Stack using Queues

Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.


Example:

```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

Notes:

- You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).


## 3. 设计一个程序，当输入一个字符串时，要求输出这个字符串的所有排列。

例如输入字符串 abc，要求输出由字母 a、b、c 所能排列出来的所有字符串 abc，acb，bac，bca，cab，cba。

## 简答题1：

现在有一场近万人在线考试，每作答一道题，获得分数会实时更新到总成绩，目前系统已知学生信息包括用户ID、姓名、学号、课程ID、当前成绩，如何设计一个按课程展示实时成绩排行榜，比如存在返回课程ID为100的这门课TOP10学生的姓名、学号、成绩。



## 简答题2：
有以下几张表：
  学生表 student(id, name, number, age)   学生ID, 学生姓名, 学号, 年龄
  教师表 teacher(id, name, number)   教师编号, 教师姓名, 教师工号
  课程表 course(id, name, course_code, teacher_id)  课程编号, 课程名称, 课程编码，教师ID
  学生成绩表 score(student_id, course_id, score) 学生ID, 课程ID, 成绩 （student_id, course_id组成主键）

测试数据如下：

```
/*
Navicat MySQL Data Transfer

Source Server         : localhost_83306
Source Server Version : 50615
Source Host           : localhost:17770
Source Database       : mylearning

Target Server Type    : MYSQL
Target Server Version : 50615
File Encoding         : 65001

Date: 2020-08-26 12:32:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `course`
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `course_code` varchar(255) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('1', '语文', 'course2009011', '1');
INSERT INTO `course` VALUES ('2', '数学', 'course2009012', '1');
INSERT INTO `course` VALUES ('3', '英语', 'course2009013', '5');

-- ----------------------------
-- Table structure for `score`
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`student_id`,`course_id`,`score`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES ('1', '1', '60');
INSERT INTO `score` VALUES ('1', '2', '40');
INSERT INTO `score` VALUES ('1', '3', '99');
INSERT INTO `score` VALUES ('2', '1', '99');
INSERT INTO `score` VALUES ('2', '2', '99');
INSERT INTO `score` VALUES ('2', '3', '99');
INSERT INTO `score` VALUES ('3', '2', '99');
INSERT INTO `score` VALUES ('3', '3', '98');
INSERT INTO `score` VALUES ('4', '1', '63');
INSERT INTO `score` VALUES ('4', '3', '100');
INSERT INTO `score` VALUES ('5', '1', '100');
INSERT INTO `score` VALUES ('6', '2', '89');

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `number` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', '学生1', '202009011', '20');
INSERT INTO `student` VALUES ('2', '学生2', '202009012', '19');
INSERT INTO `student` VALUES ('3', '学生3', '202009013', '20');
INSERT INTO `student` VALUES ('4', '学生4', '202009014', '18');
INSERT INTO `student` VALUES ('5', '学生5', '202009015', '22');
INSERT INTO `student` VALUES ('6', '学生6', '202009016', '20');

-- ----------------------------
-- Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `number` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', '老师1', '302009011');
INSERT INTO `teacher` VALUES ('2', '老师2', '302009012');
INSERT INTO `teacher` VALUES ('3', '老师3', '302009013');
INSERT INTO `teacher` VALUES ('4', '老师4', '302009014');
INSERT INTO `teacher` VALUES ('5', '老师5', '302009015');
INSERT INTO `teacher` VALUES ('6', '老师6', '302009016');

```

学生数据:

```
mysql> select * from student;
+----+-------+-----------+-----+
| id | name  | number    | age |
+----+-------+-----------+-----+
|  1 | 学生1 | 202009011 |  20 |
|  2 | 学生2 | 202009012 |  19 |
|  3 | 学生3 | 202009013 |  20 |
|  4 | 学生4 | 202009014 |  18 |
|  5 | 学生5 | 202009015 |  22 |
|  6 | 学生6 | 202009016 |  20 |
+----+-------+-----------+-----+
```


教师数据：

```
mysql> select * from teacher;
+----+-------+-----------+
| id | name  | number    |
+----+-------+-----------+
|  1 | 老师1 | 302009011 |
|  2 | 老师2 | 302009012 |
|  3 | 老师3 | 302009013 |
|  4 | 老师4 | 302009014 |
|  5 | 老师5 | 302009015 |
|  6 | 老师6 | 302009016 |
+----+-------+-----------+
```

课程表数据

```
mysql> select * from course
;
+----+------+---------------+------------+
| id | name | course_code   | teacher_id |
+----+------+---------------+------------+
|  1 | 语文 | course2009011 |          1 |
|  2 | 数学 | course2009012 |          1 |
|  3 | 英语 | course2009013 |          5 |
+----+------+---------------+------------+
```

成绩表

```
mysql> select * from score;
+------------+-----------+-------+
| student_id | course_id | score |
+------------+-----------+-------+
|          1 |         1 |    60 |
|          1 |         2 |    40 |
|          1 |         3 |    99 |
|          2 |         1 |    99 |
|          2 |         2 |    99 |
|          2 |         3 |    99 |
|          3 |         2 |    99 |
|          3 |         3 |    98 |
|          4 |         1 |    63 |
|          4 |         3 |   100 |
|          5 |         1 |   100 |
|          6 |         2 |    89 |
+------------+-----------+-------+
```

1、	请查询出语文比数学课程成绩高的所有学生的学号、姓名，展示格式如下：学号、姓名
2、	查询所有学生的所有课程的成绩以及平均成绩，并按平均成绩从高到低排序，展示格式如下：学生姓名、学号、语文成绩、数学成绩、英语成绩、平均成绩
3、	查询学习过“老师1”所教的所有课的学生的学号、姓名以及对应的课程名，展示格式如下：学号、姓名、课程名
答题：
```
1. SELECT name,number FROM student WHERE id IN (SELECT s1.student_id FROM (SELECT * FROM score WHERE course_id=1) s1,(SELECT * FROM score WHERE course_id=2)  s2 WHERE s1.student_id=s2.student_id AND s1.score>s2.score)


2.  SELECT student.`name` AS 学生姓名,student.number AS 学号,
    MAX(CASE score.course_id WHEN 1 THEN score ELSE 0 END ) 语文,
    MAX(CASE score.course_id WHEN 2 THEN score ELSE 0 END ) 数学,
    MAX(CASE score.course_id WHEN 3 THEN score ELSE 0 END ) 英语,
    AVG(score.score) AS 平均成绩 
FROM student INNER JOIN score ON student.id=score.student_id 
GROUP BY student.id 
HAVING AVG(score.score)
ORDER BY AVG(score.score) DESC;

3. 

SELECT * FROM student,course WHERE course.teacher_id IN (SELECT teacher.id FROM teacher WHERE teacher.`name`='老师1') AND student.id IN (SELECT score.student_id FROM score);


SELECT student_id,course_id FROM score WHERE course_id IN (SELECT course.id FROM course WHERE course.teacher_id IN (SELECT teacher.id FROM teacher WHERE teacher.`name`='老师1') );


```





简答题3：
有一个文本文件，里面有 100 万行。
做一个小型的 web 搜索功能。
有一个输入框，输出其中包含某些字符串的行。
会用到那些软件、那些技术、如何做？
如何添加缓存？
如何倒序展现出每天检索的关键字？
如何实现输入建议功能？
请您简单写写思路。
答题：





简答题4：
一个小型的 web 系统，方便老师保存、分享自己的课件（上课用的资料）。
会用到那些软件、那些技术、如何做？
想区分不同的版本应该如何做？
如果某个课件被分享到很多的人手里，如何确保该课件没有被篡改过。而且是最新的。
请您简单写写思路。
答题：




