from Coffee_App.models.comment import Comment
from flask import Blueprint, request, render_template

search_bp = Blueprint("search", __name__)


@search_bp.route("/search")
def search():
    keyword = request.args.get("q", "")

    if keyword:
        comments = Comment.query.filter(Comment.content.like(f"%{keyword}%")).all()
    else:
        comments = []

    return render_template("search/search.html", comments=comments, keyword=keyword)
