"""empty message

Revision ID: 513df8fc9f1e
Revises: 4c4f1e068e99
Create Date: 2020-06-07 12:49:24.732123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513df8fc9f1e'
down_revision = '4c4f1e068e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags_fandoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('fandom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fandom_id'], ['fandom.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('tag', sa.Column('tag_type', sa.Enum('General', 'Characters', 'Relationship'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tag', 'tag_type')
    op.drop_table('tags_fandoms')
    # ### end Alembic commands ###
