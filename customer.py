from constants import *
import pandas as pd

class Customer:
    def __init__(self):
        self.customer_info = pd.read_csv(str(ASSETS_PATH.joinpath('customer_info.csv')))
        self.account_info = pd.read_csv(str(ASSETS_PATH.joinpath('account_info.csv')))

    def update_customer_info_file(self, customer_info_file_path):
        try:
            self.customer_info = pd.read_csv(customer_info_file_path)
        except:
            pass
        return

    def update_account_info_file(self, account_info_file_path):
        try:
            self.customer_info = pd.read_csv(account_info_file_path)
        except:
            pass
        return

    def customer_exists(self, customer_id):
        return customer_id in self.customer_info['customer_id'].values

    def account_exists(self, customer_id, account_id):
        if not self.customer_exists(customer_id):
            return False
        
        return account_id in self.customer_info[self.customer_info['customer_id'] == customer_id]['account_id'].values