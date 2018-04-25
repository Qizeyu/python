
import json  
  
class Employee:  
    def __init__(self,name,sex,age,salary):  
        self.name  = name  ;   #姓名  
        self.sex   = sex   ;  #性别   
        self.age = age   ;  #年龄 私有变量   
        self.salary= salary;  #薪资 按月算      
   
  
person1 = Employee('张三','男',35,4560.00)  
person2 = Employee('李婷','女',28,3000.00)  
person3 = Employee('王五','男',45,7000.00)  
  
PList = []  
PList.append(person1)  
PList.append(person2)  
PList.append(person3)  
  
def ToJson(obj):  
    return {  
    "name"  : obj.name,  
    "sex"   : obj.sex ,  
    "age"   : obj.age ,  
    "salary": obj.salary     
    }  
jstr = json.dumps(PList,default=ToJson) #高阶函数  
print('{ "data":'+jstr+'}')


