import pandas as pd
from modules.preprocessing import Preprocessor
from modules.writing import ProdWriter


def main():
    
    anvisa = pd.read_csv('data_med.csv')
    brasindice = pd.read_csv('data_med_brasindice.csv')


    df = pd.concat([anvisa, brasindice], axis=0)

    preprocessor = Preprocessor(df)

    df = preprocessor.create_feature_columns()

    df = df.rename(columns={
        'Principio Ativo': 'active_ingredients',
        'Nome': 'complement',
        'dosagem': 'dosage',
        'comprimidos': 'format'
    }).drop(['Status'], axis=1)

    writer = ProdWriter()
    
    writer.write_data(df, 'remedies')


main()




