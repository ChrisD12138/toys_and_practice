import chat_service_pb2_grpc
import grpc
from concurrent import futures
import logging
import chat_service_pb2
from grpc_reflection.v1alpha import reflection


def repeat_request(request: str):
  return request


class ChatServicer(chat_service_pb2_grpc.ChatServiceServicer):

  def __init__(self):
    pass

  def RepeatRequest(self, request, context):
    logging.info(f"Received request for RepeatRequest: {request}")
    return repeat_request(request=request)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  chat_service_pb2_grpc.add_ChatServiceServicer_to_server(
      ChatServicer(), server)
  # the reflection service
  SERVICE_NAMES = (
      chat_service_pb2.DESCRIPTOR.services_by_name['ChatService'].full_name,
      reflection.SERVICE_NAME,
  )
  reflection.enable_server_reflection(SERVICE_NAMES, server)
  server.add_insecure_port("[::]:50051")
  server.start()
  logging.info("start listening on port 50051...")
  server.wait_for_termination()


if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  serve()
