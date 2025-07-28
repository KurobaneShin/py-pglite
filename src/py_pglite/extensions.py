"""Extension management for py-pglite.

This module provides a registry of supported PGlite extensions and the
necessary JavaScript import details for each.
"""

SUPPORTED_EXTENSIONS: dict[str, dict[str, str]] = {
    "pgvector": {"module": "@electric-sql/pglite/vector", "name": "vector"},
    "uuid_ossp": {"module": "@electric-sql/pglite/contrib/uuid_ossp", "name": "uuid_ossp"},
    # Additional extensions can be registered here in the future.
    # Example:
    # "pg_trgm": {"module": "@electric-sql/pglite/contrib/pg_trgm", "name": "pg_trgm"},
}
