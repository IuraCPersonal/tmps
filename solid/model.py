# Open-Closed Principle
class ImportData(ABC):
    @abstractmethod
    def read(self, path):
        pass

class ReadLocal(ImportData):
    def read(self, path):
        return pd.read_csv(path)

class ReadExternal(ImportData):
    def read(self, path):
        response = urlopen(path)
        return json.loads(response.read())

# Single Responsability Principle
class PreProcess:
    def __init__(self, df):
        self.__df = df

    def normalize(self):
        columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

        for column in columns:
            self.__df[column] = (self.__df[column] - self__df[column].min()) / (self.__df[column].max() - self.__df[column].min())

    def one_hot_encoding(self):
        cleanup = {
            "sex": {
                0: "female",
                1: "male"
            },
            "cp": {
                0: "asymptomatic",
                1: "atypical angina",
                2: "non-anginal pain",
                3: "typical angina"
            },
            "restecg": {
                0: "left ventricular hypertrophy",
                1: "normal",
                2: "ST-T wave abnormality"
            }, 
            "slope": {
                0: "negative",
                1: "zero",
                2: "positive"
            },
            "thal": {
                0: "nothing",
                1: "fixed defect",
                2: "normal",
                3: "reversable defect"
            }
        }

        self.__df = self.__df.replace(cleanup)

    def get_df(self):
        return self.__df


class SplitData:
    def __init__(self, df):
        self.__df = df

    def train(self):
        x = self.__df.drop('target', axis=1)
        y = self.__df['target']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=6)
        
        return [x_train, x_test, y_train, y_test]


class Train():
    def __init__(self, train_test_data):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_data 

    def evaluate(self):
        pass

class LogisticRegression(Train):
    def evaluate(self):
        self.__logreg = LogisticRegression()
        self.__logreg.fit(Train.x_train, Train.y_train)

        return self.__logreg


class KNN(Train):
    def evaluate(self):
        pass


class Predict:
    def __init__(self, model):
        self.__model = model

    def accuracy_score(self):
        y_pred = self.__model.predict(self.__model.x_test)

        return accuracy_score(self.__model.y_test, y_pred)

