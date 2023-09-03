

class Preprocessor:
    def __init__(self, df):
        self.df = df
    
    def create_feature_columns(self):
        
        self.__data_clean()
        
        self.__create_feature_regex(
            r'([\d]+(([,]|[.])[\d]+)?[\s](MG|UI|MCG))',
            'dosagem'
        )
        self.__create_feature_regex(
            r'([X][.]?[\s][\d]+|[\d]+[\s]?(CPRS|AMPS)[.]?)',
            'comprimidos'
        )
    
    def __data_clean(self):
        self.df['Nome'] = self.df['Nome'].str.upper()
        self.df['Principio Ativo'] = self.df['Principio Ativo'].str.upper()

    def __create_feature_regex(self, expression, feature_name):
        self.df[feature_name] = self.df['Nome'].str.extract(expression)[0]
        self.df['Nome'] = self.df['Nome'].str.replace(expression, '', regex=True)


