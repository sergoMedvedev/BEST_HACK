import asyncio

from grpc import aio

from services.db.dataBase import MessagesTable
from services.master.protos import master_pb2_grpc
from services.master.protos.master_pb2 import CreateMessageRespons
from services.master.protos.master_pb2_grpc import MasterServiceServicer
from services.master.protos.settings import PORT


class CreaterService(MasterServiceServicer):

    def CreateMessage(self, request, context):
        print(request)
        # message = MessagesTable.insert(
        #     MessagesTable(
        #         id=request.id,
        #         message=request.message,
        #         user_id=request.user_id,
        #         channel_id=request.channel_id,
        #         created_at=request.created_at,
        #         updated_at=request.updated_at,
        #         root_id=request.root_id,
        #         edited_at=request.edited_at,
        #         delete_at=request.delete_at,
        #         is_pinned = request.is_pinned,
        #         original_id = request.original_id
        #     )
        # )
        # print(f"сущность создана {message}")
        print("тест")
        return CreateMessageRespons(status="В обработке")
async def run():
    await MessagesTable.create_table(if_not_exists=True)
    server = aio.server()
    master_pb2_grpc.add_MasterServiceServicer_to_server(
        MasterServiceServicer(), server
    )
    server.add_insecure_port(PORT)
    print(f"run server {PORT}")
    await server.start()
    await server.wait_for_termination()


