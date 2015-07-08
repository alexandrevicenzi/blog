Title: New version of Django-PJAX
Date: 2015-07-08 15:00
Modified: 2015-07-08 15:00
Tags: django, pjax, jQuery, python
Slug: new-version-django-pjax

The Django-PJAX was discontinued by [Jacob Kaplan-Moss](http://jacobian.org/), the creator of this project. We at [Eventials](https://www.eventials.com) need to use Django-PJAX, so we decided to keep this project up-to-date.

We forked the original project to add a new feature, allow Django-PJAX to specify a container name. This is useful if you have more than one PJAX in the same template that points to the same view. For example:

    from djpjax import pjax

    @pjax("pjax.html") # This is the default template.
    @pjax("pjax_inner.html", "#pjax-inner-content") # This is the template for #pjax-inner-content.
    def my_view(request):
        return TemplateResponse(request, "template.html", {'my': 'context'})

We also add compatibility with Python 3. This new version works on Python 2 and 3 and any version of Django after 1.3.

You may be asking, is this a new project? No. It's the same. We owned the [original PyPi project](https://pypi.python.org/pypi/django-pjax), so you just need to run *pip install django-pjax --upgrade* to use this new version.

You can find the new version of Django-PJAX [here](https://github.com/eventials/django-pjax). Hope you like it.