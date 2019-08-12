import unittest
from types_pb2 import Transaction
from aelf import AElf


class AElfTest(unittest.TestCase):
    _url = 'http://127.0.0.1:8000'
    _private_key = 'b344570eb80043d7c5ae9800c813b8842660898bf03cbd41e583b4e54af4e7fa'

    def setUp(self):
        self.chain = AElf(self._url)
        self.chain_with_private_key = AElf(self._url, self._private_key)

    def test_chain_api(self):
        chain_status = self.chain.get_chain_status()
        print('# get_chain_status', chain_status)
        self.assertTrue(chain_status[0] > 0)

    def test_block_api(self):
        block_height = self.chain.get_block_height()
        print('# get_block_height', block_height)
        self.assertTrue(block_height > 0)

        block = self.chain.get_block_by_height(1, include_transactions=True)
        print('# get_block_by_height', block)
        self.assertTrue(block['Header']['Height'] == 1)

        block2 = self.chain.get_block(block['BlockHash'], include_transactions=False)
        print('# get_block', block2)
        self.assertTrue(block['Header']['Height'] == 1)

    def test_transaction_result_api(self):
        block = self.chain.get_block_by_height(1, include_transactions=True)
        transaction_result = self.chain.get_transaction_result(block['Body']['Transactions'][0])
        print('# get_transaction_result', transaction_result)
        self.assertTrue(transaction_result['Status'] == 'MINED')
        transaction_results = self.chain.get_transaction_results(block['BlockHash'])
        print('# get_transaction_results', transaction_results)

    def test_raw_transaction_api(self):
        transaction = {
            "From": self.chain_with_private_key.get_from_address_string(),
            "To": self.chain_with_private_key.get_system_contract_address_string("AElf.ContractNames.Consensus"),
            "RefBlockNumber": 0,
            "RefBlockHash": "b344570eb80043d7c5ae9800c813b8842660898bf03cbd41e583b4e54af4e7fa",
            "MethodName": "GetCurrentMinerList",
            "Params": '{}'
        }
        raw_transaction = self.chain_with_private_key.create_raw_transaction(transaction)
        signature = self.chain_with_private_key.sign(bytes.fromhex(raw_transaction['RawTransaction']))
        transaction_1 = {
            "RawTransaction": raw_transaction['RawTransaction'],
            "Signature": signature.hex()
        }
        # test execute_raw_transaction
        print('# execute_raw_transaction', self.chain_with_private_key.execute_raw_transaction(transaction_1))

        # test send_raw_transaction
        transaction_2 = {
            "Transaction": raw_transaction['RawTransaction'],
            'Signature': signature.hex(),
            'ReturnTransaction': True
        }
        print('# send_raw_transaction', self.chain_with_private_key.send_raw_transaction(transaction_2))

    def test_send_transaction_api(self):
        current_height = self.chain.get_block_height()
        block = self.chain.get_block_by_height(current_height, include_transactions=False)
        transaction = Transaction()
        transaction.From.CopyFrom(self.chain_with_private_key.get_from_address())
        transaction.To.CopyFrom(self.chain_with_private_key.get_system_contract_address("AElf.ContractNames.Consensus"))
        transaction.RefBlockNumber = current_height
        transaction.RefBlockPrefix = bytes.fromhex(block['BlockHash'])[0:4]
        transaction.MethodName = 'GetCurrentMinerList'
        transaction.Signature = self.chain_with_private_key.sign(transaction.SerializeToString())
        result = self.chain_with_private_key.send_transaction(transaction.SerializePartialToString().hex())
        print('# send_transaction', result)
        self.assertTrue(result['TransactionId'] != "")

    def test_tx_pool_api(self):
        tx_pool_status = self.chain.get_transaction_pool_status()
        print('# get_transaction_pool_status', tx_pool_status)
        self.assertTrue(tx_pool_status['Queued'] >= 0)

    def test_task_queue_api(self):
        task_queue_status = self.chain.get_task_queue_status()
        print('# get_task_queue_status', task_queue_status)
        self.assertTrue(len(task_queue_status) > 0)

    def test_network_api(self):
        print('# get_network_info', self.chain.get_network_info())
        print('# remove_peer')
        self.assertTrue(self.chain.remove_peer('127.0.0.1:6801'))
        print('# add_peer')
        self.assertTrue(self.chain.add_peer('127.0.0.1:6801'))

    def test_miner_api(self):
        miners = self.chain_with_private_key.get_current_miners()
        self.assertTrue(len(miners) > 0)
        print('# get_current_miners')
        for miner in miners:
            print('  > miner:', miner['public_key'], miner['address'])

        candidates = self.chain_with_private_key.get_candidates()
        print('# get_candidates')
        self.assertTrue(len(candidates) >= 0)
        for candidate in candidates:
            print('  > candidate:', candidate['public_key'], candidate['address'])


if __name__ == '__main__':
    unittest.main()
