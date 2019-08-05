# -*- coding: utf-8 -*

def readFile ():
    try:
        # r: read
        f = open('./hello.txt', 'rb')
        # <open file './hello.txt', mode 'r' at 0x10f8155d0>
        print f
        print f.read()

    except IOError:
        print 'No this file'

    finally:
        # close file 
        # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
        if f:
            f.close()

readFile()

def readRB ():
    img = open('./img.png', 'rb')
    print img.read()
    img.close()

# readRB()

def writeContent ():
    f = open('./write.txt', 'w')
    f.write('wirte content')
    f.close()

writeContent()

def useWith ():
    with open('./write.txt') as f:
        print f.read()

useWith()