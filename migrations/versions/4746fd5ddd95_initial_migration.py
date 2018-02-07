"""Initial Migration

Revision ID: 4746fd5ddd95
Revises: 
Create Date: 2018-02-06 00:05:27.478789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4746fd5ddd95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('nickname', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('pickupline', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('interview', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('Submission')
    op.drop_table('Profile')
    # ### end Alembic commands ###