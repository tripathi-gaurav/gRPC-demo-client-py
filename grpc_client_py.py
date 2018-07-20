import grpc
import HelloDroidTLS_pb2
import HelloDroidTLS_pb2_grpc
with open('server.crt', 'rb') as f:
    trusted_certs = f.read()


creds = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
channel = grpc.secure_channel('localhost:8443', creds)
stub = HelloDroidTLS_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(HelloDroidTLS_pb2.HelloRequest(name='yourname'))
print("Greeter client received: " + response.message)

