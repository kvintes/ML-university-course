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
print(len((70, 'C (all)', '345', 'Grvl', 'IR2', 'Low', 'AllPub', 'FR2', 'Mod', 'SawyerW', 'RRNn', '2fmCon', '1.5Unf', '5', '5', '1987', '1987', 'Flat', 'Tar&Grv', 'BrkComm', 'HdBoard', 'TA', 'Fa', 'Slab', 'BrkTil', '456', '456', '234', 'OthW', 'Fa', 'N', '4566', '2345', '2345', '2345', '2', '2', '1', '1', '5', '5', 'Ex', '14', 'Mod', '4', '324', 'N', '456', '456', '456', '456', '456', '456', '4565', '2007')))
print(sum([0 if (x == [] or x == '') else 1 for x in list(default_dict.values())]))