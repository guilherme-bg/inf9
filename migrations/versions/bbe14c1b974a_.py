"""empty message

Revision ID: bbe14c1b974a
Revises: 
Create Date: 2019-09-19 21:00:52.490007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbe14c1b974a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('livros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=True),
    sa.Column('autor', sa.String(length=100), nullable=True),
    sa.Column('isbn', sa.String(length=100), nullable=True),
    sa.Column('ano', sa.String(length=4), nullable=True),
    sa.Column('editora', sa.String(length=100), nullable=True),
    sa.Column('sinopse', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('livros')
    # ### end Alembic commands ###
