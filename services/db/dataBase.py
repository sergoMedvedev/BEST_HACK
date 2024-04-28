from piccolo.columns import Integer, Column, Text, Boolean, Varchar
from piccolo.engine.postgres import PostgresEngine
from piccolo.table import Table

DB = PostgresEngine(config={
    'host': 'localhost',
    'port': 15432,
    'database': 'test',
    'user': 'postgres',
    'password': 'password'
})


class MessagesTable(Table, db=DB):
    message_id = Integer(db_column_name='message_id')
    message = Text(db_column_name='message')
    user_id = Integer(db_column_name='user_id')
    channel_id = Integer(db_column_name='channel_id')
    create_at = Integer(db_column_name='create_at')
    update_at = Integer(db_column_name='update_at')
    root_id = Integer(db_column_name='root_id')
    edit_at = Integer(db_column_name='edit_at')
    delete_at = Integer(db_column_name='delete_at')
    is_pinned = Boolean(db_column_name='is_pinned')
    original_id = Integer(db_column_name='original_id')
    category = Varchar(db_column_name='category', length=50)
