from flask import Blueprint, render_template, request
from flask_login import login_required
from app import cache, db
from models import Article, News, GlossaryItem

content_bp = Blueprint('content', __name__)

@content_bp.route('/')
@cache.cached(timeout=300)
def index():
    articles = Article.query.order_by(Article.created_at.desc()).limit(5).all()
    news = News.query.order_by(News.created_at.desc()).limit(3).all()
    return render_template('content/index.html', articles=articles, news=news)

@content_bp.route('/articles')
def articles():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.order_by(Article.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('content/articles.html', articles=articles)

@content_bp.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('content/article.html', article=article)

@content_bp.route('/news')
def news():
    page = request.args.get('page', 1, type=int)
    news = News.query.order_by(News.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('content/news.html', news=news)

@content_bp.route('/glossary')
def glossary():
    category = request.args.get('category', 'all')
    if category == 'all':
        items = GlossaryItem.query.order_by(GlossaryItem.term).all()
    else:
        items = GlossaryItem.query.filter_by(category=category).order_by(GlossaryItem.term).all()
    return render_template('content/glossary.html', items=items, category=category)
