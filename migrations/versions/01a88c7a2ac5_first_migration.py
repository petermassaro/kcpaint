"""First migration

Revision ID: 01a88c7a2ac5
Revises: 
Create Date: 2018-08-10 20:26:51.484004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01a88c7a2ac5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('street', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('zip_code', sa.String(length=120), nullable=True),
    sa.Column('stripe_id', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_User_email'), 'User', ['email'], unique=True)
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('stripe_id', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stripe_id')
    )
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_table('QuoteRequests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('submit_time', sa.DateTime(), nullable=True),
    sa.Column('street', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('zip_code', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('time_requested', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=240), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.Column('misc', sa.String(length=200), nullable=True),
    sa.Column('stripe_id', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_QuoteRequests_customer'), 'QuoteRequests', ['customer'], unique=False)
    op.create_index(op.f('ix_QuoteRequests_email'), 'QuoteRequests', ['email'], unique=False)
    op.create_table('JobData',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('estimate', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quote_id'], ['QuoteRequests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('JobNote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(length=500), nullable=True),
    sa.Column('image_name', sa.String(length=500), nullable=True),
    sa.Column('time_submitted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['quote_id'], ['QuoteRequests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('JobNote')
    op.drop_table('JobData')
    op.drop_index(op.f('ix_QuoteRequests_email'), table_name='QuoteRequests')
    op.drop_index(op.f('ix_QuoteRequests_customer'), table_name='QuoteRequests')
    op.drop_table('QuoteRequests')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_table('customer')
    op.drop_index(op.f('ix_User_email'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###
