"""Added Item, ItemImage, and ImageDerivative models

Revision ID: de0968aefcb0
Revises: 
Create Date: 2016-09-25 13:03:49.145071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de0968aefcb0'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('detail_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(), nullable=True),
    sa.Column('checksum', sa.String(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('image_s3_url', sa.String(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_derivatives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('original_image', sa.Integer(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('image_s3_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['original_image'], ['item_images.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_derivatives')
    op.drop_table('item_images')
    op.drop_table('items')
    ### end Alembic commands ###
