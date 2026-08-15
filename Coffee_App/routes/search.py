from flask import Blueprint, request, render_template

search_bp = Blueprint("search", __name__)


@search_bp.route("/search")
def search():
    keyword = request.args.get("q")

    if keyword is None:
        return "キーワードがありません"
    else:
        return keyword
