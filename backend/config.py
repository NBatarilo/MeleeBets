"""Flask configuration variables."""


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:secret@localhost:5432/melee-bets'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False