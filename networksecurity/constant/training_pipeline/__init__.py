import os
import sys
import numpy as np
import pandas as pd


"""
defining common constant variable for training pipeline

"""
TARGET_COLUMN="Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACTS_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

""" 
Data Ingestion related constant start with DATA_INGESTION VAR Name

"""

DATA_INGENSTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGENSTION_DATABASE_NAME: str = "NAGI_MONGO"
DATA_INGENSTION_DIR_NAME: str = "data_ingestion"
DATA_INGENSTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGENSTION_INGESTED_DIR: str = "ingested"
DATA_INGENSTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
    
    