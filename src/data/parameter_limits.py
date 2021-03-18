#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:01:50 2019

@author: tsukuru
"""

parlimit_1= {
        "Nomenclature": "Yox_XG",
        "Keyword": ["Oxidation","Glucose", "Fermentation"],
        "Limit":[-0.01, 0.8 ],
        "Why":"They are a thermodynamic maximum biomass yield. In the case of the glucose, the maximum mass yield is 0.8 and it is due to the fraction of available electrons transferred from the substrate to oxygen, to the fraction available transferred to the biomass and the fraction available transferred to the product.",
        "Uncertainity":"0.01",
        "Literature":"Doran, P. M. (1995). Bioprocess Engineering Priciples. Academic Press, London.",
        }



parlimit_2={
        "Nomenclature": "Yred_XG",
        "Keyword": ["Reduction","Glucose", "Fermentation"],
        "Limit":[-0.01, 0.8 ],
        "Why":"They are a thermodynamic maximum biomass yield. In the case of the glucose, the maximum mass yield is 0.8 and it is due to the fraction of available electrons transferred from the substrate to oxygen, to the fraction available transferred to the biomass and the fraction available transferred to the product.",
        "Uncertainity":"0.01",
        "Literature":"Doran, P. M. (1995). Bioprocess Engineering Priciples. Academic Press, London.",
        }


parlimit_3={
        "Nomenclature": "Ypx_XE",
        "Keyword": ["Oxidation","Ethanol", "Fermentation"],
        "Limit":[-0.01, 0.8 ],
        "Why":"They are a thermodynamic maximum biomass yield. In the case of the glucose, the maximum mass yield is 0.8 and it is due to the fraction of available electrons transferred from the substrate to oxygen, to the fraction available transferred to the biomass and the fraction available transferred to the product.",
        "Uncertainity":"0.01",
        "Literature":"Doran, P. M. (1995). Bioprocess Engineering Priciples. Academic Press, London.",
        }


parlimit_4= {
        "Nomenclature": "Ks",
        "Keyword": ["Oxidation","Glucose", "Scerevisiae"],
        "Limit":[-0.01, 0.025],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of saccharomyces cerevisiae having glucose as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_5={
        "Nomenclature": "Ks",
        "Keyword": ["Glucose", "Ecoli"],
        "Limit":[-0.01, 0.004],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of escherichia coli having glucose as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",
        }


parlimit_6= {
        "Nomenclature": "Ks",
        "Keyword": ["Lactose", "Ecoli"],
        "Limit":[-0.01, 0.02],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of escherichia coli having lactose as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",
        }


parlimit_7= {
        "Nomenclature": "Ks",
        "Keyword": ["Phosphate", "Ecoli"],
        "Limit":[-0.01, 0.0016],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of escherichia coli having phosphate as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",
        }



parlimit_8= {
        "Nomenclature": "Ks",
        "Keyword": ["Glucose", "Aspergillus"],
        "Limit":[-0.01, 0.005],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of aspergillus niger having glucose as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",
        }


parlimit_9={
        "Nomenclature": "Ks",
        "Keyword": ["Glycerol", "Candida"],
        "Limit":[-0.01, 0.0045],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of candida having glycerol as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_10= {
        "Nomenclature": "Ks",
        "Keyword": ["Oxygen", "Candida"],
        "Limit":[-0.01, 0.000042],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of candida having oxygen as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }

parlimit_11= {
        "Nomenclature": "Ks",
        "Keyword": ["Methanol", "Pseudomonas"],
        "Limit":[-0.01, 0.0007],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of Pseudomonas having methanol as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_12= {
        "Nomenclature": "Ks",
        "Keyword": ["Methane", "Pseudomonas"],
        "Limit":[-0.01, 0.0004],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of Pseudomonas having methane as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_13= {
        "Nomenclature": "Ks",
        "Keyword": ["Carbon dioxide", "Klebsiella"],
        "Limit":[-0.01, 0.0004],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of Klebsiella having carbon dioxide as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_14= {
        "Nomenclature": "Ks",
        "Keyword": ["Magnesium", "Klebsiella"],
        "Limit":[-0.01, 0.00056],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of Klebsiella having magnesium as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_15= {
        "Nomenclature": "Ks",
        "Keyword": ["Potassium", "Klebsiella"],
        "Limit":[-0.01, 0.00039],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of Klebsiella having potassium as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }


parlimit_16={
        "Nomenclature": "Ks",
        "Keyword": ["Sulphate", "Klebsiella"],
        "Limit":[-0.01, 0.0027],
        "Why":"Ks is an intrinsic parameter of the cell-substrate system. Therefore this value is specific for the combination of Klebsiella having sulphate as limiting substrate",
        "Uncertainity":"0.01",
        "Literature":"Fermentation and enzyme technology by Daniel L C Wang, Charles L Cooney, Arnold L Demain, Peter Dunnill, Arthur E Humphrey, and Malcolm D Lilley, pp 374. John Wiley & Sons Ltd, Chichester and New York. 1979.",

        }

parlimit_list= [parlimit_1, parlimit_2, parlimit_3, parlimit_4, parlimit_5, parlimit_6,parlimit_7,parlimit_8,parlimit_9,parlimit_10,parlimit_11,parlimit_12,parlimit_13,parlimit_14,parlimit_15]