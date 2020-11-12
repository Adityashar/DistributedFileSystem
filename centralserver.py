from concurrent import futures
import logging

import grpc

import pb.central_pb2 as centralpb
import pb.central_pb2_grpc as central_grpc


class Central(central_grpc.CentralServicer):

    def GiveFS(self, request, context):
        print("Received a request for FS list by client with PID {}.".format(request.name))
        fs = centralpb.Response()
        fs.num = 3
        port_i = 4000
        init = "FS"
        for i in range(0, fs.num):
            server = fs.serv.add()
            server.port = str(port_i + i)
            server.id = init + str(i + 1)

        return fs           
        # PROTO MESSAGE
        # serialized response with respect to the proto


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    central_grpc.add_CentralServicer_to_server(Central(), server)

    server.add_insecure_port('[::]:50051')
    try :
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down the server.")


if __name__ == '__main__':
    logging.basicConfig()
    serve()
