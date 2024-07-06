from app import authdb
from .user import user_organization

class Organization(authdb.Model):
    orgId = authdb.Column(authdb.String(50), unique=True)
    name = authdb.Column(authdb.String(50), unique=True, nullable=False)
    description = authdb.Column(authdb.String(50))

    users = authdb.relationship('User', secondary=user_organization, back_populates='organizations')

