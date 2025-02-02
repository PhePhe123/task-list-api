"""“one_to_many_rel”

Revision ID: 455c123ce281
Revises: 29710204146c
Create Date: 2023-05-12 06:26:00.396935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455c123ce281'
down_revision = '29710204146c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
