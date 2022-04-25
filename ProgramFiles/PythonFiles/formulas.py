from asyncio.windows_events import NULL
from msilib.schema import Class
import numpy as np

class formulas(object):
    #Formulas as static Methods using NumPy
    #PassiveSingleMethods
    @staticmethod
    def calcPassiveSingleRes(volt, amp):
        return np.divide(volt,amp)
    @staticmethod
    def calcPassiveSingleVol(amp, res):
        return np.multiply(amp,res)
    @staticmethod
    def calcPassiveSingleAmp(volt, res):
        return np.divide(volt,res)

    #ActiveSingleMethods
    @staticmethod
    def calcActiveSingleRes(volt, amp):
        return np.divide(volt,amp)
    @staticmethod
    def calcActiveSingleVol(volt, amp):
        return np.divide(volt,amp)
    @staticmethod
    def calcActiveSingleAmp(volt, amp):
        return np.divide(volt,amp)

    #PassiveDualMethods
    @staticmethod
    def calcPassiveDualVolt(amp1, amp2, z1,z2,z3,z4):
        a = np.array([amp1,amp2])
        z = np.array([[z1,z2],[z3,z4]])
        v = np.dot(a,z)
        return v
        
    @staticmethod
    def calcPassiveDualAmp(volt1, volt2, z1,z2,z3,z4):
        z = np.array([[z1,z2],[z3,z4]])
        v = np.array([volt1,volt2])
        a = np.dot(z,v)
        return a
        
        