"""02-add-data

Revision ID: 601e248428cb
Revises: 3f6a1736dbe3
Create Date: 2024-04-23 17:59:21.310931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '601e248428cb'
down_revision: Union[str, None] = 'aa15f1e246a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
   
    category_list_table = sa.Table(
        'categories',
        sa.MetaData(),
        sa.Column('id', sa.Integer),
        sa.Column('cat_name', sa.String)
    )
    
    
    op.bulk_insert(category_list_table, [
        {'id': 1, 'cat_name': 'Elektronikai eszköz'},
        {'id': 2, 'cat_name': 'Élelmiszer'},
        {'id': 3, 'cat_name': 'Gyógyszer'},
        {'id': 4, 'cat_name': 'Háztartási cikk'},
        {'id': 5, 'cat_name': 'Játék'},
        {'id': 6, 'cat_name': 'Könyv'},
        {'id': 7, 'cat_name': 'Kozmetikum'},
        {'id': 8, 'cat_name': 'Ruha és kiegészítő'},
        {'id': 9, 'cat_name': 'Háztartási cikk'},
        {'id': 10, 'cat_name': 'Egyéb'}
    ])


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ##
    pass