import numpy as np
import matplotlib as plt

def mati():
    up=np.ones(1024)
    down=np.zeros(1024)
    zeroes=np.zeros(17408)
    t1=np.linspace(0,2047,2048)
    diag1=1-t1/(4096*5)
    t2=np.linspace(2048,2048+2047,2048)
    diag2=0.8-t2/(4096*5)
    t3=np.linspace(4096,4096+2047,2048)
    diag3=1-t3/(4096*5)
    t4=np.linspace(6144,6144+1023,1024)
    diag4=0.8-t4/(4096*5)
    diag5=list(reversed(diag4))
    diag6=list(reversed(diag3))
    diag7=list(reversed(diag2))
    diag8=list(reversed(diag1))
    return np.concatenate((zeroes,down,up,down,up,down,up,down,up,diag1,diag2,diag3,diag4,diag5,diag6,diag7,diag8,up,down,up,down,up,down,up,down,zeroes))

def jime():
    up1=0.3*np.ones(1024)
    up2=0.2*np.ones(1024)
    up3=0.9*np.ones(1024)
    down=np.zeros(1024)
    end=np.zeros(18432)
    return np.concatenate((up1,down,up1,down,up1,down,up1,down,up1,down,up1,down,up1,down,up1,down,up2,down,up2,down,up2,down,up2,down,up2,down,up2,down,up2,down,up3,down,up3,down,up3,down,up3,down,up3,down,up3,down,up3,down,up3,down,end))
