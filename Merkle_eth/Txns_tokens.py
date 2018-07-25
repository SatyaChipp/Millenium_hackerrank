import sys
import pandas
import requests
import timeit
import datetime
import logging
from pip._internal import main
from web3 import Web3, HTTPProvider
from collections import OrderedDict
from code_imports import *
INFURA_PRIVATE_KEY = "****************"
ETHERSCAN_APIKEY = "*****************"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("[%(asctime)s] (%(levelname)s) %(message)s"))
logger.addHandler(handler)

def install_package(pkg):
    main(['install', pkg])

def connect_infura(network, block_number=None): #test params
    if network not in ['ropsten', 'mainnet', 'rinkeby', 'kovan']:
        logger.error("Error: Unknown network, cannot connect")
    w3 = Web3(HTTPProvider("https://{}.infura.io/{}".format(network, INFURA_PRIVATE_KEY)))
    if not block_number:
        logger.info("Block number args missing, getting latest block number...")
        block_number = w3.eth.getBlock('latest').number #get latest block number #3641651
        logger.info("Latest Block on the Block Chain : {}".format(block_number))
    logger.info("Fetching transactions for block number: {}".format(block_number))
    try:
        txns, root_txns, timestamp = get_block_transactions(w3, block_number)
        logger.info("Timestamp for the block: {}".format(timestamp))
        if len(txns) == 0 :
            logger.info("No transactions for block number : {}".format(block_number))
            return
        else:
            txn_list = []
            for itxn in txns:
                keys = ('blockNumber', 'From', 'To', 'Value', 'Time')
                values = (itxn['blockNumber'], itxn['from'], itxn['to'], itxn['value'], convert(timestamp))
                # get_time_txn(itxn['hash'])
                txn_dict = OrderedDict(zip(keys, values))
                txn_list.append(txn_dict)
            return txn_list
    except Exception as er:
        logger.error('Error while parsing transaction: {}'.format(er))

# def get_time_txn(txnhash):
#     req = requests.get(url="https://api.etherscan.io/api?module=transaction&action=getstatus&txhash={}&apikey={}".format(txnhash, ETHERSCAN_APIKEY))
#     print(req.content)
#     req2 = requests.get("https://etherscan.io/tx/{}".format(txnhash))
#     print(req2.status_code)
def get_block_transactions(w3, block_number):
    block_details = w3.eth.getBlock(block_number, full_transactions=True)
    return block_details.transactions, \
           block_details.transactionsRoot, \
           block_details.timestamp

def convert(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat(' ', 'seconds')

def check_timeit():
    return ("Time: %s"%timeit.timeit(setup=imports,
                                     stmt=code,
                                     number=1000000))

if __name__ == '__main__':
    # install_package('web3')
    # data = connect_infura(network='ropsten', block_number=3642524)
    # #3640461 #3641651 -- Block numbers for testing
    # df = pandas.DataFrame(data)
    # print(df.to_string())
    # print(check_timeit())
    install_package('erc20token')




