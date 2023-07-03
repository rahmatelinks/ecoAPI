from django.contrib import admin
from django.urls import path
from snippet import views as index
from snippet import views as apis
from snippet import views as create_api
from snippet import views as login
from snippet import views as docs
from snippet import views as charts
from snippet import views as signup
from snippet import views as reset_password
from snippet import views as settings
from snippet import views as help_page
from snippet import views as account
from snippet import views as notifications
from snippet import views as error_page
from snippet import views as single_api_details



urlpatterns = [
    path('', index.home),
    path('admin/', admin.site.urls),
    path('login/', login.login),
    path('signup/', signup.signup),
    path('reset_password/', reset_password.reset_password),
    path('settings/', settings.settings),
    path('docs/', docs.docs),
    path('apis/', apis.apis),
    path('create_api/', create_api.create_api),
    path('charts/', charts.charts),
    path('help_page/', help_page.help_page),
    path('account/', account.account),
    path('notifications/', notifications.notifications),
    path('error_page/', error_page.error_page),
    path('single_api_details/', single_api_details.single_api_details),
    
]


