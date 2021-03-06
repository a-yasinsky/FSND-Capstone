"""empty message

Revision ID: 3a6555e5f398
Revises: d316ad2e3926
Create Date: 2020-03-09 04:31:03.323450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a6555e5f398'
down_revision = 'd316ad2e3926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('housing_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'contacts', 'housing', ['housing_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'housing_id')
    # ### end Alembic commands ###
