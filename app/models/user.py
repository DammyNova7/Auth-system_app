from app import authdb

user_organization = authdb.Table('user_organization',
    authdb.Column('user_id', authdb.String, authdb.ForeignKey('user.userId')),
    authdb.Column('org_id', authdb.String, authdb.ForeignKey('organization.organizationId'))
    )

class User(authdb.Model):
    userId = authdb.Column(authdb.String(50), unique=True, nullable=False)
    firstName = authdb.Column(authdb.String(50), nullable=False)
    lastName = authdb.Column(authdb.String(50), nullable=False)
    email = authdb.Column(authdb.String(50), unique=True, nullable=False)
    password = authdb.Column(authdb.String(50), nullable=False)
    phone = authdb.Column(authdb.String(50), nullable=False)

    organizations = authdb.relationship('Organization', secondary=user_organization, back_populates='users')

