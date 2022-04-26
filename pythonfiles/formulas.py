import numpy as np

class formulas(object):
    #Formulas as static Methods using NumPy
    #PassiveSingleMethods
    @staticmethod
    def calcPassiveSingleRes(volt, amp):
        volt = np.double(volt)
        amp = np.double(amp)
        return np.divide(volt,amp)
    @staticmethod
    def calcPassiveSingleVol(res, amp):
        res = np.double(res)
        amp = np.double(amp)
        return np.multiply(res,amp)
    @staticmethod
    def calcPassiveSingleAmp(volt, res):
        volt = np.double(volt)
        res = np.double(res)
        return np.divide(volt,res)

    #ActiveSingleMethods
    @staticmethod
    def calcActiveSingleRes(volt, amp):
        volt = np.double(volt)
        amp = np.double(amp)
        return np.divide(volt,amp)
    @staticmethod
    def calcActiveSingleVol(res, amp):
        res = np.double(res)
        amp = np.double(amp)
        return np.multiply(res,amp)
    @staticmethod
    def calcActiveSingleAmp(volt, res):
        volt = np.double(volt)
        res = np.double(res)
        return np.divide(volt,res)

    #PassiveDualMethods
    @staticmethod
    def calcPassiveDualCon(amp1, amp2, vol1, vol2):
        amp1 = np.double(amp1)
        amp2 = np.double(amp2)
        vol1 = np.double(vol1)
        vol2 = np.double(vol2)
        y1 = np.divide(amp1,vol1)
        y2 = np.divide(amp1,vol2)
        y3 = np.divide(amp2,vol1)
        y4 = np.divide(amp2,vol2)
        y = np.array([[y1,y2],[y3,y4]])
        return y
        

    @staticmethod
    def calcPassiveDualRes(amp1, amp2, vol1, vol2):
        amp1 = np.double(amp1)
        amp2 = np.double(amp2)
        vol1 = np.double(vol1)
        vol2 = np.double(vol2)
        z1 = np.divide(vol1,amp1)
        z2 = np.divide(vol1,amp2)
        z3 = np.divide(vol2,amp1)
        z4 = np.divide(vol2,amp2)
        z = np.array([[z1,z2],[z3,z4]])
        return z
        
    @staticmethod
    def calcPassiveDualVolt(amp1, amp2, z1,z2,z3,z4):
        amp1 = np.double(amp1)
        amp2 = np.double(amp2)
        z1 = np.double(z1)
        z2 = np.double(z2)
        z3 = np.double(z3)
        z4 = np.double(z4)
        a = np.array([amp1,amp2])
        z = np.array([[z1,z2],[z3,z4]])
        v = np.dot(a,z)
        return v
        
    @staticmethod
    def calcPassiveDualAmp(volt1, volt2, z1,z2,z3,z4):
        volt1 = np.double(volt1)
        volt2 = np.double(volt2)
        z1 = np.double(z1)
        z2 = np.double(z2)
        z3 = np.double(z3)
        z4 = np.double(z4)
        z = np.array([[z1,z2],[z3,z4]])
        v = np.array([volt1,volt2])
        a = np.dot(z,v)
        return a
        
    #AcitveDualMethods
    @staticmethod
    def calcActiveDualVolt(amp1, amp2, z1,z2,z3,z4):
        amp1 = np.double(amp1)
        amp2 = np.double(amp2)
        z1 = np.double(z1)
        z2 = np.double(z2)
        z3 = np.double(z3)
        z4 = np.double(z4)
        a = np.array([amp1,amp2])
        z = np.array([[z1,z2],[z3,z4]])
        v = np.dot(a,z)
        return v
        
    @staticmethod
    def calcActiveDualAmp(volt1, volt2, z1,z2,z3,z4):
        volt1 = np.double(volt1)
        volt2 = np.double(volt2)
        z1 = np.double(z1)
        z2 = np.double(z2)
        z3 = np.double(z3)
        z4 = np.double(z4)
        z = np.array([[z1,z2],[z3,z4]])
        v = np.array([volt1,volt2])
        a = np.dot(z,v)
        return a    