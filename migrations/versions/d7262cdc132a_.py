"""empty message

Revision ID: d7262cdc132a
Revises: 
Create Date: 2024-04-07 18:43:40.167122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7262cdc132a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('poster', sa.String(length=150), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###