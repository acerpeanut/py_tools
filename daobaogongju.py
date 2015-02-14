#!/usr/bin/python

import os
import sys
import time

DSTPATH = "C:/Users/Administrator/Desktop/package_v"


def copyFile(filePath, dstFile):
        if not os.path.isfile(filePath):
                return
        else:
                print("file |  "+filePath + ": => :"+ dstFile)
                if not os.path.exists(os.path.dirname(dstFile)):
                        os.makedirs(os.path.dirname(dstFile))
                a = file(filePath, "rb")
                b = file(dstFile, "wb")
                b.write(a.read())
                a.close()
                b.close()
                
def copyDir(dirPath, dstDir):
        print("dir  |  "+dirPath + ": => :"+ dstDir)
        if os.path.isdir(dirPath):
                if not os.path.exists(dstDir):
                        #print("mkdirs(%s)"%os.path.dirname(dstDir))
                        os.makedirs(dstDir)
                li = os.listdir(dirPath)
                for i in li:
                        if os.path.isdir(os.path.join(dirPath, i)):
                                copyDir(os.path.join(dirPath, i), os.path.join(dstDir, i))
                        elif os.path.isfile(os.path.join(dirPath, i)):
                                copyFile(os.path.join(dirPath, i), os.path.join(dstDir, i))

                

roots = {"app_level/res/audio":"app_level/res/audio",
         "app_level/res/pc_music":"app_level/res/pc_music",
         "app_level/res/txt":"app_level/res/txt",
         "test/alut.dll":"test/Debug/alut.dll",
         "test/Debug/Game":"test/Debug/Game",
         "test/test/Orz":"test/Debug/Orz",
         "test/Debug/freeglut.dll":"test/Debug/freeglut.dll",
         "test/Debug/glew32.dll":"test/Debug/glew32.dll",
         "test/Debug/glew32mx.dll":"test/Debug/glew32mx.dll",
         "test/Debug/test.exe":"test/Debug/test.exe"
         }

def mklnk():
        global DSTPATH
        a = file(os.path.join(DSTPATH, "test.bat"), "wb")
        a.write("cd test/Debug\r\n")
        a.write("test.exe")
        a.close()
        
def daobao():
        global roots
        global DSTPATH
        for i in roots.keys():
                if os.path.isdir(i):
                        #print(i+" : "+roots[i])
                        copyDir(i, os.path.join(DSTPATH,roots[i]))
                elif os.path.isfile(i):
                        copyFile(i, os.path.join(DSTPATH,roots[i]))
        mklnk()




if __name__ == "__main__":
        if len(sys.argv)>1:
                DSTPATH = sys.argv[1]
        t = time.gmtime()
        DSTPATH = "%s_%d_%d" %(DSTPATH, t.tm_mon, t.tm_mday)
        daobao()
