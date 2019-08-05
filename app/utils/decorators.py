#!coding: utf-8

def conditional_cache(decorator):
    """ Returns decorated view if user is not admin. Un-decorated otherwise """

    def _decorator(view):
        decorated_view = decorator(view)  # This holds the view with cache decorator

        def _view(request, *args, **kwargs):
            if request.user.is_authenticated:     # If user is logged in
                return view(request, *args, **kwargs)  # view without @cache
            else:
                return decorated_view(request, *args, **kwargs) # view with @cache

        return _view

    return _decorator
