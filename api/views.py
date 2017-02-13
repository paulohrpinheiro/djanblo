"""
Views for api app.
"""

from django.http import JsonResponse

import blog.models


def index(request):
    """API Help message."""
    base = request.build_absolute_uri('/api/posts')
    data = {
        'status': 'success',
        'message': '',
        'posts_listing': base,
        'post_content': '{}/{}'.format(base, '{path}'),
    }

    return JsonResponse(data)


def fail(message, status):
    """Returns a JSON for fail situations."""
    data = {
        'status': 'fail',
        'message': message,
    }

    return JsonResponse(data, status=status)


def post_info(request, post, put_content=False):
    """Return a hash with post fields (content is omitted for performance)."""
    data = {
        'title': post.title,
        'subject': post.subject,
        'publication_date': post.pub_date,
        'author': post.author.username,
        'path': post.path,
        'ref': request.build_absolute_uri('/api/posts/{}'.format(post.path)),
        'link': request.build_absolute_uri('/post/{}'.format(post.path)),
    }

    if put_content:
        data['content'] = post.content

    return data


def get_post(request, path):
    """Get one post."""
    try:
        post = blog.models.Post.objects.get(path=path)
    except blog.models.Post.DoesNotExist:
        return fail('The required post path not exist.', 404)
    except:
        return fail('Internal error. Please, try later.', 503)

    data = {
        'status': 'success',
        'message': '',
        'post': post_info(request, post, put_content=True),
    }

    return JsonResponse(data)


def list_posts(request):
    """List posts."""
    try:
        posts = blog.models.Post.objects\
                                .defer('content')\
                                .all()\
                                .order_by('-pub_date')
    except:
        return fail('Internal error. Please, try later.', 503)

    data = {
        'status': 'success',
        'message': '',
        'posts': [post_info(request, post) for post in posts],
    }

    data['posts_count'] = len(data['posts'])

    return JsonResponse(data)
