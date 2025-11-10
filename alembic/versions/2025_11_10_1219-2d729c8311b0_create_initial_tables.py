"""create initial tables

Revision ID: 2d729c8311b0
Revises: 
Create Date: 2025-11-10 12:19:47.924631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2d729c8311b0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema (CREATE TABLES and ENUMs)."""
    
    # 1. MANUAL FIX: Create ENUM types first (if not already existing)
    op.execute("CREATE TYPE prioritylevel AS ENUM ('LOW', 'MEDIUM', 'HIGH');")
    op.execute("CREATE TYPE todostatus AS ENUM ('PENDING', 'IN_PROGRESS', 'COMPLETED');")
    
    # 2. CREATE 'users' table (Referenced table - MUST COME FIRST)
    op.create_table('users',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('username', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
        sa.Column('full_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
        sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('users_pkey')),
        sa.UniqueConstraint('username', name=op.f('users_username_key'))
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    
    # 3. CREATE 'todo' table (Referencing table - MUST COME SECOND)
    op.create_table('todo',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('todo_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column('description', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
        # NOTE: ENUMs here must reference the types created above
        sa.Column('priority', postgresql.ENUM('LOW', 'MEDIUM', 'HIGH', name='prioritylevel', create_type=False), autoincrement=False, nullable=False),
        sa.Column('creation_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column('status', postgresql.ENUM('PENDING', 'IN_PROGRESS', 'COMPLETED', name='todostatus', create_type=False), autoincrement=False, nullable=True),
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name=op.f('todo_owner_id_fkey')),
        sa.PrimaryKeyConstraint('id', name=op.f('todo_pkey'))
    )
    op.create_index(op.f('ix_todo_id'), 'todo', ['id'], unique=False)

def downgrade() -> None:
    """Downgrade schema (DROP TABLES and ENUMs)."""
    
    # 1. DROP 'todo' table first (Referencing table - MUST COME FIRST)
    op.drop_index(op.f('ix_todo_id'), table_name='todo')
    op.drop_table('todo')
    
    # 2. DROP 'users' table second (Referenced table - MUST COME SECOND)
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    
    # 3. MANUAL FIX: Drop ENUM types last
    op.execute("DROP TYPE todostatus;")
    op.execute("DROP TYPE prioritylevel;")