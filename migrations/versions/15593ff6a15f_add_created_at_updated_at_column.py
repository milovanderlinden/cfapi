"""Added created_at and updated_at columns to issues

Revision ID: 15593ff6a15f
Revises: 219963bb18dc
Create Date: 2015-10-29 02:37:46.752752

"""

# revision identifiers, used by Alembic.
revision = '15593ff6a15f'
down_revision = '219963bb18dc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('issue', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('issue', sa.Column('updated_at', sa.DateTime(), nullable=True))

def downgrade():
    op.drop_column('issue', 'updated_at')
    op.drop_column('issue', 'created_at')
