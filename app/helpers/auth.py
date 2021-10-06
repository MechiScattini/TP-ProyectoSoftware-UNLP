from app.models.user import User

def authenticated(session):
    return session.get("user")

def check_permission(user_id, permission):
    return User.has_permission(user_id, permission)
