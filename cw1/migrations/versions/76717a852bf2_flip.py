"""flip

Revision ID: 76717a852bf2
Revises: e65ce8d4856e
Create Date: 2023-11-05 18:49:40.410797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76717a852bf2'
down_revision = 'e65ce8d4856e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('make_exp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('desc', sa.String(length=400), nullable=True),
    sa.Column('inc_type', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.drop_index('ix_property_address')

    op.drop_table('property')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('address', sa.VARCHAR(length=500), nullable=True),
    sa.Column('start_date', sa.DATETIME(), nullable=True),
    sa.Column('duration', sa.INTEGER(), nullable=True),
    sa.Column('rent', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.create_index('ix_property_address', ['address'], unique=False)

    op.drop_table('make_exp')
    # ### end Alembic commands ###
