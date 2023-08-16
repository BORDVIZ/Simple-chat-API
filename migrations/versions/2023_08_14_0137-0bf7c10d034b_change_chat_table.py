"""Change chat table

Revision ID: 0bf7c10d034b
Revises: 63283797c783
Create Date: 2023-08-14 01:37:02.966705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bf7c10d034b'
down_revision: Union[str, None] = '63283797c783'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('sender', sa.Integer(), nullable=True))
    op.add_column('chat', sa.Column('message', sa.String(), nullable=True))
    op.add_column('chat', sa.Column('send_time', sa.TIMESTAMP(), nullable=True))
    op.create_foreign_key(None, 'chat', 'user', ['sender'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chat', type_='foreignkey')
    op.drop_column('chat', 'send_time')
    op.drop_column('chat', 'message')
    op.drop_column('chat', 'sender')
    # ### end Alembic commands ###