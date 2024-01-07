['MSZoning',Общая классификация зонирования.
 'Street',Тип подъезда к дороге
 'LotShape',Общая форма объекта недвижимости.+
 'LandContour', Ровность участка+
 'Utilities',Типы доступных утилит.
 'LotConfig',Конфигурация лота.+
 'LandSlope',Уклон участка.+
 'Neighborhood',Физические местоположения в пределах города Эймс.
 'Condition1', Близость к главной дороге или железной дороге.
 'BldgType',Тип жилья.+
 'HouseStyle',Стиль жилища+
 'RoofStyle', Тип крыши.
 'RoofMatl',Материал крыши
 'Exterior1st',Наружное покрытие дома.
 'Exterior2nd', Наружное покрытие дома (если более одного материала)
 'ExterQual',Качество материала экстерьера.
 'ExterCond',Текущее состояние материала снаружи.
 'Foundation',Тип фундамента
 'Heating',Тип отопления
 'HeatingQC',качество и состояние отопления.
 'CentralAir',Центральное кондиционирование.+
 'KitchenQual',Качество кухни
 'Functional',Рейтинг функциональности дома
 'PavedDrive',Асфальтированная подъездная дорога
]
default_dict = {
    'MSSubClass' : 60,'MSZoning' : 'RL','LotArea' : 5000,
    'Street' : 'Pave'
    ,'LotShape' : 'Reg',
    'LandContour' : 'Lvl',
    'Utilities' : 'AllPub',
    'LotConfig' : 'Inside'
    ,'LandSlope' : 'Gtl',
    'Neighborhood' : 'CollgCr',
    'Condition1' : 'Norm','BldgType' : '1Fam'
    ,'HouseStyle' : '2Story',
    'OverallQual' : 7,'OverallCond' : 8,
    'YearBuilt' : 1965,
    'YearRemodAdd' : 2003
    ,'RoofStyle' : 'Gable',
    'RoofMatl' : 'CompShg',
    'Exterior1st' : 'VinylSd','Exterior2nd' : 'VinylSd',
    'ExterQual' : 'Gd',
    'ExterCond' : 'TA',
    'Foundation' : 'PConc',
    'BsmtFinSF1' : 578,'BsmtFinSF2' : 668,
    'BsmtUnfSF' : 434 ,'HeatingQC' : 'Ex','CentralAir' : 'Y','1stFlrSF' : 1022,'2ndFlrSF' : 756,
    'LowQualFinSF'  : 513,'GrLivArea' : 1262,'BsmtFullBath' : 1,'BsmtHalfBath' : 1,'FullBath' : 2,
    'HalfBath' : 1,'BedroomAbvGr' : 3,'KitchenAbvGr' : 2,'KitchenQual' : 'Gd','TotRmsAbvGrd' : 9,
    'Functional' : 'Typ','Fireplaces' : 1,'GarageArea' : 548,'PavedDrive' : 'Y','WoodDeckSF' : 298,
    'OpenPorchSF' : 213,'EnclosedPorch' : 272,'3SsnPorch' : 320,'ScreenPorch' : 410,'PoolArea' : 648,
    'MiscVal' : 8300,'YrSold' : 2005
}