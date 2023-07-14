import grpc
import example_pb2
import example_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = example_pb2_grpc.MyServiceStub(channel)

    name = input("Введите ваше имя: ")

    request = example_pb2.RequestMessage(name=name)
    response = stub.MyMethod(request)

    print("Ответ сервера:", response.greeting)

if __name__ == '__main__':
    run_client()