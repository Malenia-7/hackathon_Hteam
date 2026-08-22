from flask import Blueprint, request, render_template
from Coffee_App.models.category import get_categories

search_bp = Blueprint("search", __name__)


# 検索画面の表示
@search_bp.route("/search")
def search_page():
    keyword = request.args.get("keyword", "")
    category = request.args.get("category", "")

    if keyword or category:
        # TODO: post.py確認後、投稿検索処理を追加
        return render_template(
            "search/search_results.html",
            keyword=keyword,
            category=category,
        )

    categories = get_categories()

    return render_template(
        "search/search.html",
        categories=categories,
    )
