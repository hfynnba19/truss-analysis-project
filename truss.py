# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:49:20 2026

@author: user
"""

import numpy as np
joints = {}
joints['A'] = (0,0)
joints['B'] = (0,2)
joints['C'] = (1,2)

members = []
members.append(('A', 'B'))
members.append(('B', 'C'))
members.append(('A', 'C'))

#All loads are in kN (Fx, Fy)
loads = {}
loads['A'] = (7, 10)
loads['B'] = (0, -5)
loads['C'] = (0, 10)

print('Setup of truss complete')
print('Number of members:', len(members))
print('Number of joints:', len(joints))

