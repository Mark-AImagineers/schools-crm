from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
import os

class TenantRoutingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Skip middleware for unauthenticated users or for requests to the login page
        if not request.user.is_authenticated or request.path == '/login/':
            return None

        tenant_id = request.session.get('tenant_id')
        ON_HEROKU = 'DATABASE_URL' in os.environ

        if tenant_id:
            # Determine the domain based on the environment
            domain = 'schoolscrm.aimagineers.io' if ON_HEROKU else 'localhost:8000'
            
            # Determine the protocol
            protocol = 'https' if ON_HEROKU else 'http'
            redirect_url = f"{protocol}://{tenant_id}.{domain}/dashboard/"

            # Redirect if the current host doesn't start with the tenant_id
            if not request.get_host().startswith(f"{tenant_id}."):
                return redirect(redirect_url)
        else:
            # If tenant_id is not set, redirect to a tenant selection page
            # Make sure to adjust or implement this as necessary
            return redirect('login')