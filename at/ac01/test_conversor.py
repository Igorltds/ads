#import pytest
from conversor import converte

#I
def test_converteI():
    assert converte('I')== 1
def test_converteII():
    assert converte('II')== 2
def test_converteIII():
    assert converte('III')== 3

#V
def test_converteV():
    assert converte('V')== 5
def test_converteVI():
    assert converte('VI')== 6
def test_converteVII():
    assert converte('VII')== 7
def test_converteVIII():
    assert converte('VIII')== 8
def test_converteIV():
    assert converte('IV')== 4
#def test_converteIIV():
#    assert converte('IIV')== False
#def test_converteIIIV():
#    assert converte('IIIV')== False


#X
def test_converteX():
    assert converte('X')== 10
def test_converteXV():
    assert converte('XV')== 15 
def test_converteXX():
    assert converte('XX')== 20
def test_converteXXV():
    assert converte('XXV')== 25 
def test_converteXXVII(): 
    assert converte('XXVII')== 27  
def test_converteIX():
    assert converte('IX')== 9
    
#def test_converteXXVX():
#    assert converte('XXVX')== False
                                    


#input type error
def test_converteINT():
    assert converte(10) == "input type error"
def test_converteFLOAT():
    assert converte(7.7) == "input type error"

#input str invalid
def test_converteSTRint():
    assert converte("10") == "input str invalid" 
