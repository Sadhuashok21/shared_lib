import random, string

def unique_id():
    characters = string.ascii_uppercase + string.digits

    random_string = ''.join(random.choices(characters, k=20))

    return random_string

def get_client_ip(request):
    """Extracts client IP, even behind proxies."""
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # first IP in the list
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
