# -*- coding: utf-8 -*-
import string
eq=str(input())
for var in string.ascii_lowercase:
    if var in eq:
        break
eq=eq.replace("0"+var,"0*"+var).replace("1"+var,"1*"+var).replace("2"+var,"2*"+var).replace("3"+var,"3*"+var).replace("4"+var,"4*"+var).replace("5"+var,"5*"+var).replace("6"+var,"6*"+var).replace("7"+var,"7*"+var).replace("8"+var,"8*"+var).replace("9"+var,"9*"+var)
def s(eq,var):
    r=eval(eq.replace('=','-(')+')',{var:1j})
    return -r.real/r.imag

print("%c=%.3f" % (var,s(eq,var)) )