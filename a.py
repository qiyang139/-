import os
from pathlib import Path
import csv
from eth_account import Account

def create_wallets(n, file_name):
    file_path = Path(file_name).with_suffix('.csv')
    if file_path.exists():
        print("文件已存在，请换个名字：")
        return

    with file_path.open('w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Address', 'PrivateKey', 'Mnemonic', 'Index'])

        for j in range(1, n + 1):
            Account.enable_unaudited_hdwallet_features()
            account, mnemonic = Account.create_with_mnemonic()
            writer.writerow([account.address, account.key.hex(), mnemonic, j])
            print(f'第{j}个钱包创建成功')

if __name__ == '__main__':
    file_name = input('请输入文件名:')
    n = int(input('请输入需要创建的钱包数：'))
    create_wallets(n, file_name)
