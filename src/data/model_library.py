#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:20:36 2019

@author: tsukuru
"""

model_1={
        "Package": "Rx_Fermentation_Scerevisiae_Glucose_Aerobic_Batch",
        "Why": "It is baker yeast and it is used in several process",
        "Parameters":[
                { "Yox_XG" : 0.8 ,
              "Yred_XG": 0.05,
              "Yox_XE": 0.72, 
              "Y_OG": 1.067,
              "Y_EG": 0.5, 
              "Y_OE": 1.5,
              "q_g": 3.5, 
              "q_o": 0.37, 
              "q_e": 0.32, 
              "t_lag": 4.66, 
              "Kg": 0.17,
              "Ko": 0.0001,
              "Ke": 0.56, 
              "Ki": 0.31, 
              "O_sat": 0.00755, 
              "kla":1004}
                ],
        "Process conditions": [
                {"Configuration": "Stirrer tank",
                 "Mode of operation": "Batch",
                 "Oxygen conditions": "Aerobic",
                 "Temperature (ºC)": 30,
                 "pH": 4,
                 "Product":["None","Extracellular"],
                 "Limiting substrate": "Glucose",
                 "Processes involved": 
                     ["Oxidation of glucose",
                      "Reduction of glucose",
                      "Oxidation of ethanol",
                      "Oxygen supply"],
                 "Type of microorganism": "Yeast",
                 "Filamentous growth": "No",
                }
                    ],
        "Type of model": "Mechanistic model with metabolic switch controlled by the Cabtree Effect/Overflow",#Should I put that the switch is due to the rate of oxygen
        "Literature reference":"Sonnleitner, B., & Käppeli, O. (1986). Growth of Saccharomyces cerevisiae is controlled by its limited respiratory capacity: formulation and verification of a hypothesis. Biotechnology and bioengineering, 28(6), 927-937.",
    }

model_2={
        "Package": "Rx_Fermentation_MSucciniciproducens_Glucose_Anaerobic_Batch",
        "Why": "Succinic acid is monomer for bioplastic, which has been attributed large potential to replace fossil-based plastic",
        "Parameters":[
                      { "mu_max" : 1.324 ,
                      "ms": 0.061,
                      "i": 1.301,
                      "Y_AA": 0.999,
                      "Y_FA": 1.532,
                      "Y_LA": 0.999,
                      "Y_SA": 1.310,
                      "Y_x": 0.765,
                      "Kd": 0.010,
                      "Ks": 1.123,
                      "Ki": 88.35,
                      "P_crit": 17.23,
                      "Alpha_AA": 0.626,
                      "Alpha_FA": 0.665,
                      "Alpha_LA": 0,
                      "Beta_AA": 0.124,
                      "Beta_FA": 0.105,
                      "Beta_LA": 0.210,
                      "Beta_SA": 0.355}
                      ],
         "Process conditions":[
                     {"Configuration": "Stirrer tank",
                      "Mode of operation": "Batch",
                      "Oxygen conditions":"Anaerobic",
                      "Temperature (ºC)": 39,
                      "pH": 6.5,
                      "Product":["Succinic Acid","Extracellular"],
                      "By-product": ["Acetic acid", "Formic acid", "Lactic acid"],
                      "Limiting substrate": "Glucose",
                      "Processes involved":
                       ["Microorganism growth considering inhibition under substrate and product excess",
                        "Formation of succinic acid",
                        "Formation of acetic acid",
                        "Formation of formic acid",
                        "Formation of lactic acid"],
                      "Type of microorganism": "Bacterium",
                      "Filamentous growth": "No",
                       }
                         ],
          "Type of model": "Unstructure kinetic model. The growth of the microorganisms is described by Monod equation while the Luedeking-Piret model can represent the formation of organic acids",
          "Literature reference":"Song, H., Jang, S. H., Park, J. M., & Lee, S. Y. (2008). Modeling of batch fermentation kinetics for succinic acid production by Mannheimia succiniciproducens. Biochemical Engineering Journal, 40(1), 107-115.",
#          "Considerations":"To arrive to the monomers we need to get the free acid(lower pH) generating by-products that are difficult to separate

       }

model_3={
        "Package": "Rx_Fermentation_StreptococcusThermophilus_Lactose_Anaerobic_Batch",
        "Why": "",
        "Parameters":[
                      { "mu_max" : 2.06,
                      "Kp,la": 0.24,
                      "Kla": 19.80,
                      "Y_AA": 0.999,
                      "Y_FA": 1.532,
                      "Y_LA": 0.999,
                      "Y_SA": 1.310,
                      "Y_x": 0.765,
                      "Kd": 0.010,
                      "Ks": 1.123,
                      "Ki": 88.35,
                      "P_crit": 17.23,
                      "Alpha_AA": 0.626,
                      "Alpha_FA": 0.665,
                      "Alpha_LA": 0,
                      "Beta_AA": 0.124,
                      "Beta_FA": 0.105,
                      "Beta_LA": 0.210,
                      "Beta_SA": 0.355}
                      ],
         "Process conditions":[
                     {"Configuration": "Stirrer tank",
                      "Mode of operation": "Batch",
                      "Oxygen conditions":"Anaerobic",
                      "Temperature (ºC)": 39,
                      "pH": 6.5,
                      "Product":["Succinic Acid","Extracellular"],
                      "By-product": ["Acetic acid", "Formic acid", "Lactic acid"],
                      "Limiting substrate": "Glucose",
                      "Processes involved":
                       ["Microorganism growth considering inhibition under substrate and product excess",
                        "Formation of succinic acid",
                        "Formation of acetic acid",
                        "Formation of formic acid",
                        "Formation of lactic acid"],
                      "Type of microorganism": "Bacterium",
                      "Filamentous growth": "No",
                       }
                         ],
          "Type of model": "",
          "Literature reference":"",
#          "Considerations":"To arrive to the monomers we need to get the free acid(lower pH) generating by-products that are difficult to separate

       }

model_4={
    "Package": "Rx_Fermentation_CGlutamicum_Glucose_Aerobic_Batch",
        "Why": "It is commercially one of the most important amino acids produced chiefly by fermentation. Its sodium salt is used as a flavour enhancer with a 6% growth of its production and 1.5 millions of tons stimation",
        "Parameters":[
                { "Yxs" : 0.655,
                  "Ypx":3.278,
                  "Yps":0.584,
                  "Kg": 0.164,
                  "toxicpower":1,
                  "mu_max":0.163}
                ],
        "Process conditions": [
                {"Configuration": "Stirrer tank",
                 "Mode of operation": "Batch",
                 "Oxygen conditions": "Aerobic. Dissolved oxygen tension was kept at 30% of air saturation",
                 "Temperature (ºC)": 30,
                 "pH": 7,
                 "Product":["L-glutamic acid","Extracellular"],
                 "Limiting substrate": "Glucose",
                 "Processes involved":
                     ["Growth of the Corynebacterium glutamicum with dependance of substrate and product inhibition",
                      "L-glutamic acid formation",
                      "Glucose consumption"],
                 "Type of microorganism": "Grampositive bacterium",
                 "Filamentous growth": "No",
                }
                    ],
        "Type of model": "Unsegregated unstructured Monod model in where substrate availability and product inhition effect the specific growth rate based on Levenspiel expression",#Should I put that the switch is due to the rate of oxygen
        "Literature reference":"Khan, N. S., Mishra, I. M., Singh, R. P., & Prasad, B. (2005). Modeling the growth of Corynebacterium glutamicum under product inhibition in L-glutamic acid fermentation. Biochemical Engineering Journal, 25(2), 173-178.",
#        "Considerations":"Although the microorganism present a lag phase, exponential phase, stationary phase and decline phase. Only the second and third are considered here",
    }

model_5= {
    "Package": "Rx_Fermentation_Ecoli_Glucose_Aerobic_Batch",
        "Why": "Escherichia coli is the most common host organism to mass produce important human pharmaceutical proteins or other foreign proteins. Naturally, E. coli produces and consumes acetate in batch and fed-batch cultures. Acetate produced inhibits several physiological properties of the culture, while the presence of glucose inhibites the consumption of glucose.",
        "Parameters":[
                {"Ka":0.5,#g/L
                "Kis":1.8383, #g/L
                "Ks": 0.0381, #g/L
                "Ksa" : 0.0128,#g/L affinity constant
                "qAcmax" : 0.1148 ,#g/gh
                "qm" : 0.0133, #g/gh
                "qOmax" : 13.4*31.9988/1000, #g/gh
                "qSmax" : 0.635, #g/gh
                "Yas" : 0.8938, #g/g
                "Yoa" : 0.5221, #g/g
                "Yos" : 1.562, #g/g
                "Yxa" : 0.5794, #g/g
                "Yxsa" : 0.15, #g/g
                "Yxsof" : 0.229 , # g/g
                "Yxsox" : 0.51 ,#g/g
                "pAmax" : 0.2268, #gA/gXh
                "kla" : 220,
                "H" : 1400 }
                ],
        "Process conditions": [
                {"Configuration": "Stirrer tank",
                 "Mode of operation": "Batch",
                 "Oxygen conditions": "Aerobic. Dissolved oxygen tension was kept at 30% of air saturation",
                 "Temperature (ºC)": 37,
                 "pH": 7,
                 "Product":["Acetic acid","Extracellular"],
                 "Limiting substrate": "Glucose",
                "Processes involved":
                     ["Consumption of glucose",
                      "Production of acetate",
                      "Consumption of acetate",
                      "Oxygen supply"],
                 "Type of microorganism": "Gram-negative bacterium",
                 "Filamentous growth": "Yes"
                }
                ],
        "Type of model": "Overflow metabolism considering acetate cycling. It contains modified Monod to add the inhibition effect and a set of ordinary differential equations to describe the flux",#Should I put that the switch is due to the rate of oxygen
        "Literature reference":"Anane, E., Neubauer, P., & Bournazou, M. N. C. (2017). Modelling overflow metabolism in Escherichia coli by acetate cycling. Biochemical Engineering Journal, 125, 23-30.",
#        "Considerations":"Although the microorganism present a lag phase, exponential phase, stationary phase and decline phase. Only the second and third are considered here",
    }
#The models that I am really interested to introduce are: B.subtilis, A.niger, P.chrysogenum


model_list = [model_1, model_2, model_3, model_4, model_5]