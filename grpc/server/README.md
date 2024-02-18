###  generate the gRPC client and server interface ###
python3 -m grpc_tools.protoc -I ./ --python_out=. --pyi_out=. --grpc_python_out=. ./chat_service.proto

### debug with grpcurl
```
grpcurl -plaintext -d '{"request":"hello world"}' localhost:50051 chatService.ChatService.RepeatRequest
```