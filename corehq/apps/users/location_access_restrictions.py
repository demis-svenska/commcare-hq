from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _

from corehq.apps.hqwebapp.views import no_permissions
from corehq.apps.locations import views as location_views

LOCATION_ACCESS_MSG = (
    "This project has restricted data access rules.  Please contact your "
    "project administrator to access specific data in the project"
)


class LocationAccessMiddleware(object):
    """
    Many large projects want to restrict data access by location.
    Views which handle that properly are called "location safe". This
    middleware blocks access to any non location safe features by users who
    have such a restriction. If these users do not have an assigned location,
    they cannot access anything.
    """

    def process_view(self, request, view_fn, view_args, view_kwargs):
        user = getattr(request, 'couch_user', None)
        domain = getattr(request, 'domain', None)
        if (
            user and domain
            and not user.has_permission(domain, 'access_all_locations')
            and (
                not is_location_safe(view_fn)
                or not user.get_sql_location(domain)
            )
        ):
            return no_permissions(request, message=LOCATION_ACCESS_MSG)


def is_location_safe(view_fn):
    def get_path(fn):
        return fn.__module__ + fn.__name__
    return get_path(view_fn) in [
        get_path(view) for view in LOCATION_SAFE_VIEWS
    ]


# This is a list of views which will safely restrict access based on the web
# user's assigned location where appropriate.
LOCATION_SAFE_VIEWS = (
    location_views.LocationsListView,
)
