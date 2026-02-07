from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # API Endpoints
    # Documentation endpoints
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("auth/", include("apps.authentication.urls")),
    path("jobs/", include("apps.jobs.urls")),
    # path('search/', include('search.urls')),
    path("profiles/", include("apps.profiles.urls")),
    path("apply/", include("apps.applications.urls")),
]
