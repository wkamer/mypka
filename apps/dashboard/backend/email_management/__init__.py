"""email_management package — Email Management (Inbox Zero) backend module.
FastAPI APIRouter mounted in main.py."""
from .db import _init_db, _migrate_drop_body_text
from .routes import router
_init_db()
_migrate_drop_body_text()
__all__ = ["router"]
