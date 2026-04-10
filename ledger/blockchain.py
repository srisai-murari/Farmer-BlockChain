
import hashlib, json, time
from .models import Block

class Blockchain:
    def __init__(self):
        if Block.objects.count() == 0:
            self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(
            index=0,
            timestamp=time.time(),
            transactions=json.dumps(["Genesis Block"]),
            previous_hash="0",
            hash=""
        )
        genesis.hash = self.calculate_hash(genesis)
        genesis.save()

    def calculate_hash(self, block):
        block_string = json.dumps({
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": block.transactions,
            "previous_hash": block.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, transactions):
        latest = Block.objects.latest('index')
        new_block = Block(
            index=latest.index + 1,
            timestamp=time.time(),
            transactions=json.dumps(transactions),
            previous_hash=latest.hash,
            hash=""
        )
        new_block.hash = self.calculate_hash(new_block)
        new_block.save()
'''
    def is_chain_valid(self):
        blocks = Block.objects.all().order_by('index')
        for i in range(1, len(blocks)):
            current = blocks[i]
            previous = blocks[i-1]
            if current.hash != self.calculate_hash(current):
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
'''
def is_chain_valid(self):
    for i in range(1, len(self.chain)):
        current_block = self.chain[i]
        previous_block = self.chain[i - 1]

        if current_block['previous_hash'] != self.hash(previous_block):
            return False

        if self.hash(current_block) != self.hash(current_block):
            return False

    return True