def user_avatar_path(instance, filename):
    return f'avatars/user_{instance.user.id}/{filename}'

def user_media_path(instance, filename):
    return f'post_images/user_{instance.user.id}/{filename}'