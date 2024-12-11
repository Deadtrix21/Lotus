from pymongo import MongoClient
from dotenv import load_dotenv
import os


class database_handler:
    def __init__(self) -> None:
        self.connected = None
        self.connect()
    
    def get_cluster(self):
        try:
            if load_dotenv():
                return os.getenv("DATABASE")
        except Exception as E:
            print("No DataBase Key")
    
    def connect(self):
        self.connected = MongoClient(
            self.get_cluster(), 
            serverSelectionTimeoutMS=5000
            )
        self.test_connection()
        
    def test_connection(self):
        try:
            self.connected.server_info()
            print("Connected")
        except Exception:
            print("Unable to connect to the server.")