from posts.models import Topic

def topic(request):
    all_topics = Topic.objects.all()
    return {'topics':all_topics}