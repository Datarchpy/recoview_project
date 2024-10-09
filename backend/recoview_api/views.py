from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Review

@api_view(['POST'])
def submit_review(request):
    data = request.data
    book_title = data.get('book_title')
    positive_points = data.get('positive_points')
    negative_points = data.get('negative_points')

    # レビューをデータベースに保存
    review = Review.objects.create(
        book_title=book_title,
        positive_points=positive_points,
        negative_points=negative_points
    )
    review.save()

    # 仮のレコメンド結果を返す
    recommended_book = "サンプル本タイトル"
    return Response({"recommended_book": recommended_book})
