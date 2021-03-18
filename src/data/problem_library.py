#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:33:35 2019

@author: tsukuru
"""

pro_1={
        "Description": "Cooling system is not working",
        "Variableaffected": "CoolingOn",
        "Effect":{"coolingOn":0},
        "Probability":"0.1",
        "Solution":["Turn on the cooling water"],
        }


pro_2={
        "Description": "Wrong of the temperature set point",
        "Variableaffected": "Tset",
        "Effect":{"Tset":("0.75*T")},
        "Probability":"0.25",
        "Solution":"Turn on the cooling water",
        }


pro_3={
        "Description": "Wrong of the temperature set point",
        "Variableaffected": "Tset",
        "Effect":{"Tset":("0.75*T")},
        "Probability":"0.25",
        "Solution":"Turn on the cooling water",
        }


pro_4={
        "Description": "Contamination by lactic acid bacteria ",
        "Variableaffected": "r[0,0]",
        "Effect":{"r[0,0]":("1.5*r[0,0]")},
        "Probability":"0.25",
        "Solution":"Early stop of the batch in order to not use all the substrate",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
        }

pro_5={
        "Description": "Inhibition by furfural and acetic acid",
        "Variableaffected": "Y_EG",
        "Effect":{"Y_EG":("0.80*Y_EG")},
        "Probability":"0.25",
        "Solution":"Control of the feed rate, to ensure the concentrations of inhibitors remain under a certain threshold",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
        }
problem_list = [pro_1, pro_2, pro_3, pro_4, pro_5]