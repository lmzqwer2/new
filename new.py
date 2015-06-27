#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lmzqwer2'

from os import path
import sys
import shutil
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    import json
except ImportError:
    import simplejson as json

def newFile(newFileName):

    if path.exists(newFileName):
        return 
    newFileExtName = path.splitext(newFileName)[1]
    
    userFolder = path.expanduser('~')
    configFolder = path.join(userFolder,'Templates/')
    configFileName = '.config.json'
    configFilePath = path.join(configFolder,configFileName)
#    print configFilePath

    try:
        with open(configFilePath,'r') as f:
            data = json.load(f)
    except:
        print 'What\'s wrong with your config.json?'
        data = {}
#    print data
#    print newFileExtName
    try:
        templateName = data[newFileExtName[1:]]
    except:
        templateName = 'emptyFile'
    templateNamePath = path.join(configFolder, templateName)
#    print templateNamePath
    if path.exists(templateNamePath):
        shutil.copy(templateNamePath, newFileName)
    else:
        try:
            with open(newFileName, 'w') as f:
                pass
        except IOError:
            print 'Can\'t create this file or folder...'
        
if __name__ == '__main__':
    args = sys.argv
    if (len(args)==1):
        fileName = raw_input('Input FileName: ')
    else:
        fileName = args[1]
    newFile(fileName)
