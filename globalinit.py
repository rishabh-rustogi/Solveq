from os import read
from readConfigure import readConfigure

configure = readConfigure()

def init():
    global pics
    pics = []

def checkUserPass(username, password):
    return configure.checkUserPass(username, password)
    
def retMathpixKeys():
    return configure.retMathpixKeys()

def retWolfAppID():
    return configure.retWolfAppID()