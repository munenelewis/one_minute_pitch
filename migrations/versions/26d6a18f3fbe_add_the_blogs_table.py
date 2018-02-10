"""add the blogs table

Revision ID: 26d6a18f3fbe
Revises: 507a5b22ae64
Create Date: 2018-02-10 23:48:37.906912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d6a18f3fbe'
down_revision = '507a5b22ae64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vote', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitches_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('time_posted', sa.DateTime(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'username')
    op.drop_column('comments', 'votes')
    op.add_column('pitch', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitch', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitch', type_='foreignkey')
    op.drop_column('pitch', 'category_id')
    op.add_column('comments', sa.Column('votes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'time_posted')
    op.drop_table('votes')
    op.drop_table('categories')
    # ### end Alembic commands ###
