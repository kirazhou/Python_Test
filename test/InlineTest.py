from test import data
import my_code
import test
S='We are Yang'
#print test.boy
print S[0]
name = 'mathboy'
dic = {'mo': 99,
    'linlin': 98,
    'mathboy': 100}
print dic.get('linlin')
print dic.get('wm')

def set(a,b):
    a = 3.14
    b = [1,2,3]
    return a,b

x = 6.28
y = [4,5,6]
x,y = set(x,y)
print x
print y
for x in range(5):
    print x
#���������ʽ�����б����һ����������������Բ����()�ж����Ƿ�����[]��
for num in (x**2 for x in range(5)):
    print num,
