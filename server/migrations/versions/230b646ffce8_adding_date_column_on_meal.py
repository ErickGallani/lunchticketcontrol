"""Adding date column on meal

Revision ID: 230b646ffce8
Revises: 0ba2c7c09215
Create Date: 2018-01-16 00:54:13.739307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '230b646ffce8'
down_revision = '0ba2c7c09215'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('availabilities', sa.Column('time', sa.DateTime(), nullable=False))
    op.add_column('meals', sa.Column('date', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meals', 'date')
    op.drop_column('availabilities', 'time')
    # ### end Alembic commands ###
