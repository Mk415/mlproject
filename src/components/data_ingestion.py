import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging
from components.data_transformation import DataTransformation
from components.data_transformation import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from components.model_trainer import ModelTrainer
from components.model_trainer import ModelTrainerConfig
@dataclass
class Dataingestionconfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class Dataingestion:
    def __init__(self):
        self.ingestion_config=Dataingestionconfig()
    def init_data_ingestion(self):
        logging.info("starting to ingest data")
        try:
            df=pd.read_csv("notebook/data/stud.csv")
            logging.info("read the dataset")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("started train test split")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingestion of data completed")
            return(self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    obj=Dataingestion()
    # obj.init_data_ingestion()
    train_data,test_data=obj.init_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.init_data_transformation(train_data,test_data)
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

