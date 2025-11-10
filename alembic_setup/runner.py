from alembic.config import Config
from alembic import command

def run_upgrade_head():
    """ Programmatically run 'alembic upgrade hhead' 
    This function can be called to upgrade the database from the root directory.
    """
    alembic_config = Config("alembic.ini")
    print("Running database migrations....")
    try:
        command.upgrade(alembic_config, "head")
        print("Migration completed.")
    except Exception as e:
        print(f"Migration failed: {e}")
      