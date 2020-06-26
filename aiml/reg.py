__author__ = "zhou"
__date__ = "2019-04-25 20:35"


"""
正则表达式的高级应用
贪婪与懒惰    贪婪与非贪婪
非贪婪: 尽可能少的匹配
非贪婪操作符? 
这个非贪婪操作符可以使用在  *  +  ?  后边   
* 重复0次或者是多次     *?
+ 重复1次或者是多次      +?
? 重复0次或1次     ??
"""

import re

s = "greedyaiiiiiii"
# reg = "greedyai*"
reg = "greedyai+?"
# print(re.findall(reg,s))

"""
分之条件匹配
操作符  |
"""

s = "我的电话号码: 010-89832343 0431-89847345 0432-7842342"
# reg = "0\d{2}-\d{8}"
# reg = "0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7}"
# print(re.findall(reg,s))
# s1 = "010-89832343"
# s2 = "0431-89847345"
# s3 = "0432-7842342"
# reg = "^0\d{2,3}"
# print(re.findall(reg,s1))

#零宽断言
"""
(?=reg)  匹配reg前边的位置
(?<=reg)  匹配reg后边的位置
(?!=reg)  匹配后边跟的不是reg的位置
(?<!reg)  匹配前边跟的不是reg的位置
"""

s = "hellogreedyailoove"
# reg = "l{2}o(?=greedyai)"
# print(re.findall(reg,s))
reg = "(?<=greedyai)[a-z]*"
print(re.findall(reg,s))












