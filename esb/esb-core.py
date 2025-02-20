from kombu import Connection, Exchange, Queue

class ESB:
    def __init__(self):
        self.connection = Connection('amqp://guest:guest@localhost//')
        self.exchange = Exchange('esb_exchange', type='direct')
    
    def send_message(self, service_name, message):
        with self.connection.Producer() as producer:
            producer.publish(message, exchange=self.exchange, routing_key=service_name)
    
    def receive_message(self, service_name, callback):
        queue = Queue(name=service_name, exchange=self.exchange, routing_key=service_name)
        with self.connection.Consumer(queue, callbacks=[callback]) as consumer:
            while True:
                self.connection.drain_events()

# To simulate the ESB running
if __name__ == '__main__':
    esb = ESB()
    print("ESB is running...")
    