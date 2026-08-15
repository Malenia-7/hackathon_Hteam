from flask import Blueprint, request, render_template


search_bp = Blueprint('search', __name__)
@search_bp.route('/search')
def search():
  return '検索ページ'