"""rename department

Revision ID: 5d4cf8365508
Revises: 2f979294dc19
Create Date: 2024-01-31 00:11:34.251569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d4cf8365508'
down_revision = '2f979294dc19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("department", "departments")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("departments", "department")
    # ### end Alembic commands ###
