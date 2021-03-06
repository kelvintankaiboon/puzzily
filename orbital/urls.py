"""orbital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from attendance import views
from accounts import views as accounts_views

urlpatterns = [
	# path('attendance/', include('attendance.urls')),
	# path('accounts/', include('accounts.urls')),
    path('', login_required(views.TutorialListView.as_view()), name='home'),
    # path('', views.tutoriallist, name='tutoriallist'),
    path('<slug:group>', views.sessions, name='sessions'),
    path('search/', views.search, name='search'),
    path('addtutorial/', views.AddTutorial, name='addtutorial'),
    path('addsession/', views.AddSession, name='addsession'),
    path('<slug:group>/<str:date>', views.attlist, name='attlist'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('signup/student/', accounts_views.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/tutor/', accounts_views.TutorSignUpView.as_view(), name='tutor_signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
