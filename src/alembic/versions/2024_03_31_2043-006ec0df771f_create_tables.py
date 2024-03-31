"""Create tables

Revision ID: 006ec0df771f
Revises: 
Create Date: 2024-03-31 20:43:06.137846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Date, Time, Integer, ForeignKey, PrimaryKeyConstraint, String

# revision identifiers, used by Alembic.
revision: str = '006ec0df771f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Создание таблицы Users
    op.create_table('Users',
        Column('id', Integer(), nullable=False),
        Column('chat_id', Integer(), unique=True),
        Column('user_fullname', String(), nullable=False),
        # Другие столбцы, если есть
        PrimaryKeyConstraint('id')
    )

    # Создание таблицы Organizations
    op.create_table('Organizations',
        Column('id', Integer(), nullable=False),
        Column('organization_name', String(), unique=True, nullable=False),
        Column('invite_code', String(), nullable=False),
        Column('default_slots_amount', Integer(), server_default='4'),
        Column('user_id', Integer(), ForeignKey('Users.id'), nullable=False),
        # Другие столбцы, если есть
        PrimaryKeyConstraint('id')
    )

    # Создание таблицы Users_Organizations
    op.create_table('Users_Organizations',
        Column('id', Integer(), nullable=False),
        Column('user_id', Integer(), ForeignKey('Users.id'), nullable=False),
        Column('organization_id', Integer(), ForeignKey('Organizations.id'), nullable=False),
        # Другие столбцы, если есть
        PrimaryKeyConstraint('id')
    )

    # Создание таблицы RecordingWeeks
    op.create_table('RecordingWeeks',
        Column('id', Integer(), nullable=False),
        Column('start_date', Date(), nullable=False),
        Column('end_date', Date(), nullable=False),
        # Другие столбцы, если есть
        PrimaryKeyConstraint('id')
    )

    # Создание таблицы Recordings
    op.create_table('Recordings',
        Column('id', Integer(), nullable=False),
        Column('date', Date(), nullable=False),
        Column('time', Time(), nullable=False),
        Column('slots_amount', Integer(), nullable=False),
        Column('recording_week_id', Integer(), ForeignKey('RecordingWeeks.id'), nullable=False),
        Column('organization_id', Integer(), ForeignKey('Organizations.id'), nullable=False),
        # Другие столбцы, если есть
        PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('Recordings')
    op.drop_table('RecordingWeeks')
    op.drop_table('Users_Organizations')
    op.drop_table('Organizations')
    op.drop_table('Users')

