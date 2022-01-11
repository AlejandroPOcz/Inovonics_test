"""Elements URLs."""

# Django
from django.urls import path

# Views
from elements import views
from elements import utils

urlpatterns = [
    path(
        route='',
        view=views.home,
        name='home'
    ),
    path(
        route='elements/',
        view=utils.elements,
        name='display_elements'
    ),
    path(
        route='elements/add/beginning/<int:num>/',
        view=utils.add_beginning,
        name='add_beginning'
    ),
    path(
        route='elements/add/end/<int:num>/',
        view=utils.add_end,
        name='add_end'
    ),
    path(
        route='elements/add/before/<int:old_num>/<int:new_num>/',
        view=utils.add_before,
        name='add_before'
    ),
    path(
        route='elements/add/after/<int:old_num>/<int:new_num>/',
        view=utils.add_after,
        name='add_after'
    ),
    path(
        route='elements/index/<int:num>/',
        view=utils.index,
        name='index'
    ),
]
