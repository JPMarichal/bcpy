from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app import admin, db
from models import User, Article, News, GlossaryItem

admin_bp = Blueprint('admin_routes', __name__)

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'admin'

# Register the models with Flask-Admin
admin.add_view(SecureModelView(User, db.session))
admin.add_view(SecureModelView(Article, db.session))
admin.add_view(SecureModelView(News, db.session))
admin.add_view(SecureModelView(GlossaryItem, db.session))