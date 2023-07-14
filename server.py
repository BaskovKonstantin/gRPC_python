import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures


class MyServiceServicer(example_pb2_grpc.MyServiceServicer):
    def MyMethod(self, request, context):
        name = request.name
        greeting = f"Hello, {name}!"
        return example_pb2.ResponseMessage(greeting=greeting)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
