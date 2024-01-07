default_dict = {
    'MSSubClass' : 60,'MSZoning' : 'RL','LotArea' : 5000,'Street' : 'Pave'
    ,'LotShape' : 'Reg','LandContour' : 'Lvl','Utilities' : 'AllPub','LotConfig' : 'Inside'
    ,'LandSlope' : 'Gtl','Neighborhood' : 'CollgCr','Condition1' : 'Norm','BldgType' : '1Fam'
    ,'HouseStyle' : '2Story','OverallQual' : 7,'OverallCond' : 8,'YearBuilt' : 1965,'YearRemodAdd' : 2003
    ,'RoofStyle' : 'Gable','RoofMatl' : 'CompShg','Exterior1st' : 'VinylSd','Exterior2nd' : 'VinylSd',
    'ExterQual' : 'Gd','ExterCond' : 'TA','Foundation' : 'PConc','BsmtFinSF1' : 578,'BsmtFinSF2' : 668,
    'BsmtUnfSF' : 434 ,'HeatingQC' : 'Ex','CentralAir' : 'Y','1stFlrSF' : 1022,'2ndFlrSF' : 756,
    'LowQualFinSF'  : 513,'GrLivArea' : 1262,'BsmtFullBath' : 1,'BsmtHalfBath' : 1,'FullBath' : 2,
    'HalfBath' : 1,'BedroomAbvGr' : 3,'KitchenAbvGr' : 2,'KitchenQual' : 'Gd','TotRmsAbvGrd' : 9,
    'Functional' : 'Typ','Fireplaces' : 1,'GarageArea' : 548,'PavedDrive' : 'Y','WoodDeckSF' : 298,
    'OpenPorchSF' : 213,'EnclosedPorch' : 272,'3SsnPorch' : 320,'ScreenPorch' : 410,'PoolArea' : 648,
    'MiscVal' : 8300,'YrSold' : 2005
}

model_dict = {
    MSSubClass
LotArea
OverallQual
OverallCond
YearBuilt
YearRemodAdd
BsmtFinSF1
BsmtFinSF2
BsmtUnfSF
1stFlrSF
2ndFlrSF
LowQualFinSF
GrLivArea
BsmtFullBath
BsmtHalfBath
FullBath
HalfBath
BedroomAbvGr
KitchenAbvGr
TotRmsAbvGrd
Fireplaces
GarageArea
WoodDeckSF
OpenPorchSF
EnclosedPorch
3SsnPorch
ScreenPorch
PoolArea
MiscVal
YrSold
MSZoning_C (all)
MSZoning_FV
MSZoning_RH
MSZoning_RL
MSZoning_RM
Street_Grvl
Street_Pave
LotShape_IR1
LotShape_IR2
LotShape_IR3
LotShape_Reg
LandContour_Bnk
LandContour_HLS
LandContour_Low
LandContour_Lvl
Utilities_AllPub
Utilities_NoSeWa
LotConfig_Corner
LotConfig_CulDSac
LotConfig_FR2
LotConfig_FR3
LotConfig_Inside
LandSlope_Gtl
LandSlope_Mod
LandSlope_Sev
Neighborhood_Blmngtn
Neighborhood_Blueste
Neighborhood_BrDale
Neighborhood_BrkSide
Neighborhood_ClearCr
Neighborhood_CollgCr
Neighborhood_Crawfor
Neighborhood_Edwards
Neighborhood_Gilbert
Neighborhood_IDOTRR
Neighborhood_MeadowV
Neighborhood_Mitchel
Neighborhood_NAmes
Neighborhood_NPkVill
Neighborhood_NWAmes
Neighborhood_NoRidge
Neighborhood_NridgHt
Neighborhood_OldTown
Neighborhood_SWISU
Neighborhood_Sawyer
Neighborhood_SawyerW
Neighborhood_Somerst
Neighborhood_StoneBr
Neighborhood_Timber
Neighborhood_Veenker
Condition1_Artery
Condition1_Feedr
Condition1_Norm
Condition1_PosA
Condition1_PosN
Condition1_RRAe
Condition1_RRAn
Condition1_RRNe
Condition1_RRNn
BldgType_1Fam
BldgType_2fmCon
BldgType_Duplex
BldgType_Twnhs
BldgType_TwnhsE
HouseStyle_1.5Fin
HouseStyle_1.5Unf
HouseStyle_1Story
HouseStyle_2.5Fin
HouseStyle_2.5Unf
HouseStyle_2Story
HouseStyle_SFoyer
HouseStyle_SLvl
RoofStyle_Flat
RoofStyle_Gable
RoofStyle_Gambrel
RoofStyle_Hip
RoofStyle_Mansard
RoofStyle_Shed
RoofMatl_ClyTile
RoofMatl_CompShg
RoofMatl_Membran
RoofMatl_Metal
RoofMatl_Roll
RoofMatl_Tar&Grv
RoofMatl_WdShake
RoofMatl_WdShngl
Exterior1st_AsbShng
Exterior1st_AsphShn
Exterior1st_BrkComm
Exterior1st_BrkFace
Exterior1st_CBlock
Exterior1st_CemntBd
Exterior1st_HdBoard
Exterior1st_ImStucc
Exterior1st_MetalSd
Exterior1st_Plywood
Exterior1st_Stone
Exterior1st_Stucco
Exterior1st_VinylSd
Exterior1st_Wd Sdng
Exterior1st_WdShing
Exterior2nd_AsbShng
Exterior2nd_AsphShn
Exterior2nd_Brk Cmn
Exterior2nd_BrkFace
Exterior2nd_CBlock
Exterior2nd_CmentBd
Exterior2nd_HdBoard
Exterior2nd_ImStucc
Exterior2nd_MetalSd
Exterior2nd_Other
Exterior2nd_Plywood
Exterior2nd_Stone
Exterior2nd_Stucco
Exterior2nd_VinylSd
Exterior2nd_Wd Sdng
Exterior2nd_Wd Shng
ExterQual_Ex
ExterQual_Fa
ExterQual_Gd
ExterQual_TA
ExterCond_Ex
ExterCond_Fa
ExterCond_Gd
ExterCond_Po
ExterCond_TA
Foundation_BrkTil
Foundation_CBlock
Foundation_PConc
Foundation_Slab
Foundation_Stone
Foundation_Wood
Heating_Floor
Heating_GasA
Heating_GasW
Heating_Grav
Heating_OthW
Heating_Wall
HeatingQC_Ex
HeatingQC_Fa
HeatingQC_Gd
HeatingQC_Po
HeatingQC_TA
CentralAir_N
CentralAir_Y
KitchenQual_Ex
KitchenQual_Fa
KitchenQual_Gd
KitchenQual_TA
Functional_Maj1
Functional_Maj2
Functional_Min1
Functional_Min2
Functional_Mod
Functional_Sev
Functional_Typ
PavedDrive_N
PavedDrive_P
PavedDrive_Y
}









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