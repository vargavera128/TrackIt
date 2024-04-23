"""01-create-table

Revision ID: 3f6a1736dbe3
Revises: 
Create Date: 2024-04-23 17:40:16.039789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = '3f6a1736dbe3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tracks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('shop', sa.String),
        sa.Column('item_name', sa.String),
        sa.Column('item_price', sa.Integer)
    )

    op.create_table(
        'list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cat_name', sa.String)
    )

    op.create_table(
        'sort',
        sa.Column('track_id', sa.Integer, sa.ForeignKey('tracks.id')),
        sa.Column('list_id', sa.Integer, sa.ForeignKey('list.id'))
    )

    pass
    


def downgrade() -> None:
    pass
    
