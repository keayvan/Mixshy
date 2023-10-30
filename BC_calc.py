#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:43:49 2023

@author: k1
"""

import pandas as pd
def v_calc(mDot, rho, l_in, depth):
    vel = mDot/rho/l_in/0.001/depth
    return vel

def Reynolds(rho, v, l_in, depth, mhu):
    re = rho*v*(4*l_in*depth*0.001/(l_in*0.001+depth))/mhu
    return re

def intensity_turb(re):
    intensity = 0.16*re**(-1/8)
    return intensity

def k_turb (intensity, v):
    k = 3/2*(intensity*v)**2
    return k
prop_file = './BC_prop.csv'
prop = pd.read_csv(prop_file)

depth = 0.004
mDot_air, rho_air,l_in_air,mhu_air = prop.iloc[0,[2,3,4,7]]
mDot_fuel, rho_fuel,l_in_fuel,mhu_fuel = prop.iloc[1,[2,3,4,7]]

vel_air = v_calc(mDot_air,
                 rho_air,
                 l_in_air,
                 depth)

vel_fuel = v_calc(mDot_fuel,
                    rho_fuel,
                    l_in_fuel,
                    depth)

reynolds_air = Reynolds(rho_air, vel_air, l_in_air, depth, mhu_air)
reynolds_fuel = Reynolds(rho_fuel, vel_fuel, l_in_fuel, depth, mhu_fuel)

air_turbulent_int = intensity_turb(reynolds_air)
fuel_turbulent_int = intensity_turb(reynolds_fuel)

k_air = k_turb(air_turbulent_int, vel_air)
k_fuel = k_turb(fuel_turbulent_int, vel_fuel)


