"""alter user table

Revision ID: b219ee6f86fe
Revises: 
Create Date: 2025-10-27 11:38:14.204202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b219ee6f86fe'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""ALTER TABLE users ADD COLUMN userType VARCHAR(100) DEFAULT 'student'""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""ALTER TABLE users DROP COLUMN userType""")
    pass
