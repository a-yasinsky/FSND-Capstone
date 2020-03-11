"""empty message

Revision ID: 86d3bcb73a07
Revises: beda3de0d754
Create Date: 2020-03-04 09:40:01.779006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86d3bcb73a07'
down_revision = 'beda3de0d754'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photos', sa.Column('housing_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'photos', 'housing', ['housing_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'photos', type_='foreignkey')
    op.drop_column('photos', 'housing_id')
    # ### end Alembic commands ###
