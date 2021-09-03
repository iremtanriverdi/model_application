import requests

url = 'http://localhost:3000/predict_ap'
r = requests.post(url,json={'emp_nonemp':2, 'bin_BL_gender':2, 'bin_BL_marital2':2,
                            'bin_BL_education':1, 
                            'age_group':2, 'BL_F6':1,'Labour_market_A4':6,'FU_B1_imputed':2, 
                            'BL_Difference_G':2, 'bin_BL_marital2':2,'bin_BL_education':1, 
                            'BL_B6_13':2, 'FU_A10_imputed':1,'FU_A14_imputed':6,"BL_A4_groupped":1})

