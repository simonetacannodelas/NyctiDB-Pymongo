#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:41:04 2019

@author: tsukuru
"""


par_1={
        "Parameter": "Yield for the oxidative pathway of glucose to biomass",
        "Nomenclature": "Yox_XG",
        "SI_units":"g biomass/g glucose",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_2={
        "Parameter": "Yield for the reductive pathway of glucose to biomass",
        "Nomenclature": "Yred_XG",
        "SI_units":"g biomass/g glucose",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }

                         

par_3={
        "Parameter": "Yield for the oxidative pathway of ethanol to biomass",
        "Nomenclature": "Yox_XE",
        "SI_units":"g biomass/g glucose",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_4={
        "Parameter": "Yield of the need of oxygen to glucose",
        "Nomenclature": "Y_OG",
        "SI_units":"g oxygen/g glucose",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_5={
        "Parameter": "Yield of the conversion of glucose in ethanol",
        "Nomenclature": "Y_EG",
        "SI_units":"g ethanol/g glucose",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_6={
        "Parameter": "Yield of the need of oxygen to ethanol",
        "Nomenclature": "Y_OE",
        "SI_units":"g oxygen/g ethanol",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_7={
        "Parameter": "Maximal specific glucose uptake rate",
        "Nomenclature": "q_g",
        "SI_units":"g glucose/g biomass h",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
    }

par_8={
        "Parameter": "Maximal specific ethanol uptake rate",
        "Nomenclature": "q_e",
        "SI_units":"g ethanol/g biomass h",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_9={
        "Parameter": "Maximal specific oxygen uptake rate",
        "Nomenclature": "q_o",
        "SI_units":"g oxygen/g biomass h",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_10={
        "Parameter": "Lag phase time",
        "Nomenclature": "t_lag",
        "SI_units":"h",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }



par_11={
        "Parameter": "Saturation parameter for substrate uptake",
        "Nomenclature": "Ks",
        "SI_units":"g glucose/L",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch",  "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch","Rx_Fermentation_CGlutamicum_Glucose_Aerobic_Batch", "Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
}



par_12={
        "Parameter": "Saturation parameter for oxygen uptake",
        "Nomenclature": "Ko",
        "SI_units":"g oxygen/L",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
    }


par_13= {
        "Parameter": "Saturation parameter for ethanol uptake",
        "Nomenclature": "Ke",
        "SI_units":"g ethanol/L",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }


par_14= {
        "Parameter": "Inhibition parameter: free glucose inhibits ethanol uptake",
        "Nomenclature": "Ki",
        "SI_units":"g glucose/L",
        "type":"Biotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch.py"],
    }


par_15={
        "Parameter": "Concentration of saturated oxygen",
        "Nomenclature": "O_sat",
        "SI_units":"g oxygen/L",
        "type":"Abiotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch.py"],
    }

par_16= {
        "Parameter": "Mass transfer coefficient for oxygen",
        "Nomenclature": "kla",
        "SI_units":"1/h",
        "type":"Abiotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch.py"],
    }


par_17={
        "Parameter": "Mass transfer coefficient for oxygen",
        "Nomenclature": "kla",
        "SI_units":"1/h",
        "type":"Abiotic",
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch.py"],
    }


par_18={
        "Parameter": "Initial glucose concentration",
        "Nomenclature": "G0",
        "SI_units":"g glucose/L",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch",  "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch"],
    }


par_19= {
        "Parameter": "Initial ethanol concentration",
        "Nomenclature": "E0",
        "SI_units":"g ethanol/L",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch.py"],
    }



par_20={
        "Parameter": "Initial oxygen concentration",
        "Nomenclature": "O0",
        "SI_units":"g ethanol/L",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch",  "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch"],
    }


par_21= {
        "Parameter": "Initial biomass concentration",
        "Nomenclature": "X0",
        "SI_units":"g ethanol/L",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch"],
    }


par_22={
        "Parameter": "End time of the operation",
        "Nomenclature": "t_end",
        "SI_units":"h",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_CGlutamicum_Glucose_Aerobic_Batch"],
    }


par_23={
        "Parameter": "Initial volumen",
        "Nomenclature": "V0",
        "SI_units":"L",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_CGlutamicum_Glucose_Aerobic_Batch"],
    }


par_24={
        "Parameter": "Concentration of feed",
        "Nomenclature": "Cin",
        "SI_units":"g feed/L",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch.py"],
    }


par_25={
        "Parameter": "Initial feeding rate",
        "Nomenclature": "F0",
        "SI_units":"g feed/L h",
        "type":"Abiotic",#???
        "In the model": [""],
    }


par_26= {
        "Parameter": "Specific growth rate",
        "Nomenclature": "SFR",
        "SI_units":"1/h",
        "type":"Biotic",#???
        "In the model": [""],
    }


par_27= {
        "Parameter": "Specific growth rate",
        "Nomenclature": "mu",
        "SI_units":"1/h",
        "type":"Biotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch", "Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
    }


par_28= {
        "Parameter": "Degree of reduction of biomass",
        "Nomenclature": "y_x",
        "SI_units":"dimensionless",
        "type":"Biotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch", "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch"],
    }


par_29={
        "Parameter": "Decay coefficeint",
        "Nomenclature": "kd",
        "SI_units":"1/h",
        "type":"Biotic",#???
        "In the model": ["Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch"],
    }


par_30= {
        "Parameter": "Start of exponential feed",
        "Nomenclature": "t_expfb_start",
        "SI_units":"h",
        "type":"Abiotic",#???
        "In the model": ["Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch"],
    }

par_31={
        "Parameter": "Toxic power",
        "Nomenclature": "toxicpower",
        "SI_units":"adimensional",
        "type":"Biotic",#???
        "In the model": ["Rx_Fermentation_CGlutamicum_Glucose_Aerobic_Batch"],
    }


par_32 ={
        "Parameter": "Monod-type saturation constant, intracellular acetate production",
        "Nomenclature":"Kap",
        "SI_units": "adimensional",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_33 = {
        "Parameter": "Saturation parameter for acetate consumption",
        "Nomenclature":"Ksa",
        "SI_units": "g/L",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }

par_34 = {
        "Parameter": "Inhibition constant of glucose uptake by acetate",
        "Nomenclature":"Kia",
        "SI_units": "g/L",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_35 = {
        "Parameter": "Inhibition constant of acetate uptake by glucose",
        "Nomenclature": "Kis",
        "SI_units": "g/L",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_36 =  {
        "Parameter": "Specific acetate production rate",
        "Nomenclature": "pa",
        "SI_units": "g/g h",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_37 =  {
        "Parameter": "Specific acetate consumption rate",
        "Nomenclature": "qa",
        "SI_units": "g/g h",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_38 =  {
        "Parameter": "Specific maintenance coefficient",
        "Nomenclature": "qm",
        "SI_units": "g/g h",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_39 = {
        "Parameter": "Yield of biomass on substrate from auxiliary overflow routes, such as the mixed acid and pentose-phosphate pathways",
        "Nomenclature": "Yxsof",
        "SI_units": "",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }


par_40 =  {
        "Parameter": "Rate of consumption of substrate",
        "Nomenclature": "r[0,0]",
        "SI_units": "g/L h",
        "type": "Biotic",  # ???
        "In the model": ["Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch"],
        }

parameter_list = [par_1, par_2, par_3,par_4, par_5, par_6, par_7, par_8, par_9, par_10, par_11, par_12, par_13, par_14, par_15, par_16, par_17, par_18, par_19, par_20, par_21, par_22, par_23, par_24, par_25, par_26, par_27, par_28, par_29, par_30, par_31, par_32, par_33, par_34, par_35, par_36, par_37, par_38, par_39, par_40]


