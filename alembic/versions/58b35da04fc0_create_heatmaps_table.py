"""create heatmaps table

Revision ID: 58b35da04fc0
Revises: 
Create Date: 2022-02-19 12:59:33.893413

"""
from alembic import op
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58b35da04fc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_heatmaps',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column('x', sa.Integer),
        sa.Column('y', sa.Integer),
        sa.Column('user_id', UUID(as_uuid=True), nullable=False),
        sa.Column('page_id', UUID(as_uuid=True), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('test_heatmaps')
    pass
