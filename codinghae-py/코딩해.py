import sys

"""
예시코드:

넣어정수0에5
넣어정수1에8
더해0하고1해서2에
말해2
빼1하고0해서2에
말해2
곱해0하고1해서2에
말해2
나눠1하고0해서2에
말해2
나눠몫만1하고0해서2에
말해2
나눠나머지만1하고0해서2에
말해2

출력:
13
3
40
1.6
1
3

"""
class codinghae():
    def __init__(self):
        self.data = [0]*256
    def type(self,code):
        if '넣어정수' in code and '에' in code:
            return 'defineint'
        elif '넣어소수' in code and '에' in code:
            return 'definefloat'
        elif '넣어문자' in code and '에' in code:
            return 'definestr'
        elif '더해' in code and '하고' in code and '에' in code:
            return 'plus'
        elif '빼' in code and '하고' in code and '에' in code:
            return 'minus'
        elif '곱해' in code and '하고' in code and '에' in code:
            return 'mul'
        elif '나눠몫만' in code and '하고' in code and '에' in code:
            return 'divdiv'
        elif '나눠나머지만' in code and '하고' in code and '에' in code:
            return 'percent'
        elif '나눠' in code and '하고' in code and '에' in code:
            return 'div'
        elif '말해' in code:
            return 'print'
        elif '받아정수' in code and '에':
            return 'inputint'
        elif '받아소수' in code and '에':
            return 'inputfloat'
        elif '받아문자' in code and '에':
            return 'inputstr'
    def compileline(self,code:str):
        if code == '':
            return None
        TYPE = self.type(code)
        if TYPE == 'defineint':
            code = code.replace('넣어정수','')
            index,num = int(code.split('에')[0]),int(code.split('에')[1])
            self.data[index] = num
        elif TYPE == 'definefloat':
            code = code.replace('넣어소수','')
            index,num = int(code.split('에')[0]),float(code.split('에')[1])
            self.data[index] = num
        elif TYPE == 'definestr':
            code = code.replace('넣어문자','')
            index,str = int(code.split('에')[0]),code.split('에')[1]
            self.data[index] = str
        elif TYPE == 'plus':
            code = code.replace('더해','')
            code = code.replace('에','')
            index,index2,index3 = int(code.split('하고')[0]),int(code.split('하고')[1].split('해서')[0]),int(code.split('하고')[1].split('해서')[1])
            self.data[index3] = self.data[index]+self.data[index2]
        elif TYPE == 'minus':
            code = code.replace('빼','')
            code = code.replace('에','')
            index,index2,index3 = int(code.split('하고')[0]),int(code.split('하고')[1].split('해서')[0]),int(code.split('하고')[1].split('해서')[1])
            self.data[index3] = self.data[index]-self.data[index2]
        elif TYPE == 'mul':
            code = code.replace('곱해','')
            code = code.replace('에','')
            index,index2,index3 = int(code.split('하고')[0]),int(code.split('하고')[1].split('해서')[0]),int(code.split('하고')[1].split('해서')[1])
            self.data[index3] = self.data[index]*self.data[index2]
        elif TYPE == 'div':
            code = code.replace('나눠','')
            code = code.replace('에','')
            index,index2,index3 = int(code.split('하고')[0]),int(code.split('하고')[1].split('해서')[0]),int(code.split('하고')[1].split('해서')[1])
            self.data[index3] = self.data[index]/self.data[index2]
        elif TYPE == 'divdiv':
            code = code.replace('나눠몫만','')
            code = code.replace('에','')
            index,index2,index3 = int(code.split('하고')[0]),int(code.split('하고')[1].split('해서')[0]),int(code.split('하고')[1].split('해서')[1])
            self.data[index3] = self.data[index]//self.data[index2]
        elif TYPE == 'percent':
            code = code.replace('나눠나머지만','')
            code = code.replace('에','')
            index,index2,index3 = int(code.split('하고')[0]),int(code.split('하고')[1].split('해서')[0]),int(code.split('하고')[1].split('해서')[1])
            self.data[index3] = self.data[index]%self.data[index2]
        elif TYPE == 'print':
            code = code.replace('말해','')
            index = int(code)
            print(self.data[index])
        elif TYPE == 'inputint':
            code = code.replace('받아정수','')
            index,num = int(code.split('에')[0]),int(input())
            self.data[index] = num
        elif TYPE == 'inputfloat':
            code = code.replace('받아소수','')
            index,num = int(code.split('에')[0]),float(input())
            self.data[index] = num
        elif TYPE == 'inputstr':
            code = code.replace('받아문자','')
            index,strr = int(code.split('에')[0]),input()
            self.data[index] = strr
    def compile(self,code:list):
        for i in code:
            self.compileline(i)
    def compilePath(self):
        with open(str(sys.argv[1]),encoding='utf-8') as f:
            code = f.readlines()
            for i in range(len(code)):
                if i != len(code):
                    code[i] = code[i].replace('\n','')
            self.compile(code)

코드 = codinghae()
코드.compilePath()
