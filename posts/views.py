from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from posts.models import Post
import json


# Create your views here.

@require_http_methods(["POST"])
def create_post(request):
    body = json.loads(request.body.decode('utf-8'))

    new_post = Post.objects.create(
        writer = body['writer'],
        title = body['title'],
        contents = body['contents'],
    )

    new_post_json = {
        "id" : new_post.id,
        "writer" : new_post.writer,
        "title" : new_post.title,
        "contents" : new_post.contents,
        
    }

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 목록 조회 성공',
        'data' : new_post_json
    })

@require_http_methods(["GET"])
def get_post_all(request) :    
        post_all = Post.objects.all()

        post_json_all = []

        for post in post_all :
            post_json = {
                "id" : post.id,
                "writer" : post.writer,
                "title" : post.title,
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 조회 성공',
            'data' : post_json_all
        })
    
@require_http_methods(["DELETE"])
def delete_post(request, id) : 
    delete_post = get_object_or_404(Post, pk=id)
    delete_post.delete()

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 삭제 성공',
        'data' : None
    })
'''
1. 방명록 작성하기
2. 방명록 리스트 보여주기
3. 방명록 삭제
'''