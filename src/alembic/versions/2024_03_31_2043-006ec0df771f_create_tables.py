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
    # Создание таблицы Role
    op.create_table(
        'Roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title')
    )

    # Создание таблицы User
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('chat_id', sa.Integer(), nullable=True),
        sa.Column('user_fullname', sa.String(), nullable=False),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('Roles.id'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('chat_id')
    )

    # Создание таблицы Organization
    op.create_table(
        'Organizations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('organization_name', sa.String(), nullable=False),
        sa.Column('invite_code', sa.String(), nullable=False),
        sa.Column('default_slots_amount', sa.Integer(), nullable=True, server_default=sa.text('4')),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('Users.id'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('organization_name')
    )

    # Создание таблицы User_Organization
    op.create_table(
        'Users_Organizations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('Users.id'), nullable=False),
        sa.Column('organization_id', sa.Integer(), sa.ForeignKey('Organizations.id'), nullable=False),
        sa.Column('is_current_organization', sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.PrimaryKeyConstraint('id')
    )

    # Создание таблицы RecordingWeek
    op.create_table(
        'RecordingWeeks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Создание таблицы Recording
    op.create_table(
        'Recordings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('time', sa.Time(), nullable=False),
        sa.Column('slots_amount', sa.Integer(), nullable=False),
        sa.Column('recording_week_id', sa.Integer(), sa.ForeignKey('RecordingWeeks.id'), nullable=False),
        sa.Column('organization_id', sa.Integer(), sa.ForeignKey('Organizations.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    # Удаление таблиц
    op.drop_table('Recordings')
    op.drop_table('RecordingWeeks')
    op.drop_table('Users_Organizations')
    op.drop_table('Organizations')
    op.drop_table('Users')
    op.drop_table('Roles')