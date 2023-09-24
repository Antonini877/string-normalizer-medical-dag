

class Preprocessor:
    def __init__(self, df):
        self.df = df
    
    def create_feature_columns(self):
        
        self.__to_upper()
        
        self.__create_feature_regex(
            r'(([\d]+(([,]|[.])[\d]+)?[\s]([M]?[C]?G(/ML)?|UI|ML)[.]?[\s]?[+]?[\s]?){1,2})',
            'dosagem'
        )
        self.__create_feature_regex(
            r'([X][.]?[\s][\d]+|[\d]+[\s]?(CPRS|AMPS|CAPS|X|DOSES)[.]?)',
            'comprimidos'
        )

        self.__data_clean()

        return self.df
    
    def __to_upper(self):
        self.df['Nome'] = self.df['Nome'].str.upper()
        self.df['Principio Ativo'] = self.df['Principio Ativo'].str.upper()

    def __data_clean(self):
        self.df['Nome'] = self.df['Nome'].str.strip()
        self.df['Principio Ativo'] = self.df['Principio Ativo'].str.strip()

    def __create_feature_regex(self, expression, feature_name):
        self.df[feature_name] = self.df['Nome'].str.extract(expression)[0]
        self.df['Nome'] = self.df['Nome'].str.replace(expression, '', regex=True)


