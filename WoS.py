import sys
import os
import bson
import gris
from formatting import *

reload(sys)
sys.setdefaultencoding("utf-8")

class Wos(dict):
    def __init__(self, path):
        for ris_file in os.listdir(path):
            ris = gris.readris(path + '/' + ris_file)
            for each in ris:
                paper_id = bson.objectid.ObjectId()
                self[paper_id] = Paper(each)
                self[paper_id].format()

class Paper(dict):
    def __init__(self, wos_source):
        for entry in wos_source:
            self[entry] = wos_source[entry]
    
    def format(self):
        for each in self.keys():
            if each in ['LA','PY','NR','GA','UT','PI','BP','RP','EP','VL','CY','IS','PD','HO','AR','PN','SI','CA','MA']:
                self[each] = self[each].strip()
            elif each in ['TI','SO','PA']:
                self[each] = format_ti(self[each])
            elif each in ['AF','AU','BF','BA']: self[each] = format_af(self[each])
            elif each == 'CR': self[each] = format_cr(self[each])
            elif each in ['TC']: self[each] = self[each][0].strip()
            elif each == 'WC': self[each] = format_wc(self[each])
            elif each == 'DT': self[each] = format_dt(self[each])
            elif each == 'SC': self[each] = format_sc(self[each])
            elif each in ['AB','CT','JI','SP','SE','FX']: self[each] = format_ab(self[each])
            elif each in ['SN','DI','CL','BN']: self[each] = format_sn(self[each])
            elif each in ['DE','ID']: self[each] = format_de(self[each])
            elif each in ['EM']: self[each] = format_em(self[each])
            elif each in ['BE','FU']: self[each] = [x for x in unlist(self[each])]
            elif each == 'GP': self[each] = format_gp(self[each])
            elif each == 'RI': self[each] = format_ri(self[each])

if __name__ == '__main__':
    pass