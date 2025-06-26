from django.http import HttpResponseForbidden

def employer_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_employer:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not allowed here.")
    return _wrapped_view
