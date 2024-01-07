import pickle

linearModel = None
with open("./models/LinearRegression.pickle", "rb") as file:
    linearModel = pickle.load(file)

linearModel.predict[[]]
print('hi')

# def build_all_GUI_argsList():


# def build_inputModel_list(list_include_GUI):

# categorial_list = [
# 'MSZoning','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood','Condition1','Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl','Exterior1st','Exterior2nd','ExterQual','ExterCond','Foundation','Heating','HeatingQC','CentralAir','KitchenQual','Functional','PavedDrive','SaleType','SaleCondition'
# ]