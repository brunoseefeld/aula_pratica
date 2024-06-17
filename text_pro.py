import sys

import string



def read_file(file_name:str):
    f=open(file_name,'r',encoding='utf8')
    text=f.read()
    return text


def lower_file(text:str):
    text=text.lower()

def jazzing(word:str)->str:
    jazz=''
    for i in word:
        if i!='r':
            jazz+=i
        else:
            jazz+='j'

    return jazz







if __name__=='__main__':

    text=read_file('free_will.txt')

    print(jazzing('bruno'))


    




