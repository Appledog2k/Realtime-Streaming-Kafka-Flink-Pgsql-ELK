import random
from faker import Faker
from confluent_kafka import SerializingProducer
from datetime import datetime

fake = Faker()
def generate_sales_transactions():
    user = fake.simple_profile()
    return {
        "transactionId": fake.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),
        "productName": random.choice(['laptop', 'mobile', 'tablet', 'watch', 'headphone', 'speaker']),
        'productCategory': random.choice(['electronic', 'fashion', 'grocery', 'home', 'beaty', 'sports']),
        'productPrice': round(random.uniform(10, 1000), 2),
        'productQuantity': random.randint(1, 10),
        'productBrand': random.choice(['apple', 'samsung', 'sony', 'mi', 'boat', 'sony']),
        'currency': random.choice(['USD', 'GBP']),
        'customerName': user['name'],
        'transactionDate': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        'paymentMethod': random.choice(['credit', 'debit', 'online_transfer'])
    }
    
    def main():
        topic = 'financial_transactions'
        