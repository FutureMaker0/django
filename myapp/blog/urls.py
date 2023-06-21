from django.urls import path
from . import views
# from blog.views import Index

app_name = 'blog'

urlpatterns = [
    # path(패턴, 맵핑)
    # path("", views.index) # 아무것도 안적으면 인덱스 페이지 의미한다. FBV
    
    # 글 목록조회 - 데이터베이스에 저장하고 불러오는 작업
    # path("", views.Index.as_view(), name='list'),
    # ""는 /하나 들어가 있는 디폴트 상태다.
    path("", views.List.as_view(), name='list'),
    
    # 글 상세조회
    path("detail/<int:pk>/", views.Detail.as_view(), name='detail'),
    
    # 글 작성
    # path("write/", views.write, name='write'), # views에 write 함수.
    path("write/", views.Write.as_view(), name='write'), # views에 write 함수.


    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제

]

# 여기에 정의하는 애들은 서버주소/blog에 정의가 되는 애들이다.

# 함수기반, 클래스기반 뷰의 표기 바업ㅂ이 다르다.
# 캡슐화, 상속 가능.

