from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View 
from django.views.generic import ListView, CreateView, DetailView
from .models import Post # 같은 경로의 models에서 Post 가져옴.
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# 블로그 안에 있는 views.py를 열었다.
# models - urls - views 순서로 하는 거에서 끝 단계까지 왔다.

'''
웹 요청을 받는다. url + method로 받는다.
요청을 처리하고 디비에서 필요한 값이 있다면 가져온다.
가져온 값을 가공, 정리해서 응답 형태로 만들어준다.
응답을 반환한다.
그 전에 urls에서 맵핑을 해주는게 우선이다.

fbv 함수 기반 뷰 - 얘가 우선 이해가 되어야 클래스 기반이 이해가 된다.
cbv 클래스 기반 뷰
'''

# 요청에 대한 응답을 리턴하는 곳
# 요청은 그 종류를 무조건 구분을 해줘야 한다.
# 애초에 요청이 Url + method 이기 때문이다.
# 메소드 값을 확인하면서 구별을 해줘야된다.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('index page GET')
#     # 나머지 요청등에 대해서는
#     # 에러 예외처리 등을 해줘야 한다.
#     return HttpResponse('No!!!')
# # 이렇게 해놓고 url에서 맵핑 해줘야 한다.


# 클래스로 동일하게 다시한 번 만들어보자.
class Index(View):
    def get(self, request):
        # return HttpResponse('index page GET class')
        
        # 디비에 접근해서 값을 가져와아 한다.
        # 게시판에 글을 보여줘야되기 때문에 디비에서 값 조회
    
        post_objs = Post.objects.all()
        context = {
            "posts": post_objs
            # "posts": None
        }

        # 렌더의 정석적 인자값 3개
        return render(request, 'blog/board.html', context)



# ============================================ write
# write - 요청에 대한 응답을 만드는 함수로 리퀘스트가
# 반드시 들어와야 한다.
# form - 클라이언트가 서버에 값을 전송하는 것
def write(request):
    if request.method == 'POST':
        # form을 확인해줘야 한다.
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:list')

    else: # 요청된 값이 없을때는,
        form = PostForm()
        return render(request, 'blog/write.html', { 'form': form })
        # blog/write.html은 템플릿 지정하는 곳이고 주소 저장하는 곳이 아니다.
        # 템플릿 자체가 들어가야 한다.
        

# django 자체에 클래스 뷰 기능이 강력하고 편리하다.

# 많이 사용.
# model, template_name, context_object_name,
# paginate_by - 페이지를 어떻게 끊어줄 것인지.
# form_class, form_valid(), get_queryset()

# generic view -> ListView
class List(ListView):
    model = Post # 모델 설정
    template_name = 'blog/post_list.html' # 어떤 템플릿
    
    # 템플릿을 나타내는게 아니다.
    context_object_name = 'posts' # 변수 값의 이름 - post_list의 posts


class Write(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:list')


class Detail(DetailView):
    model = Post # 모델 설정
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# 수정 페이지 진행예정 - 상세페이지에서 수정하면 자연스럽다.


