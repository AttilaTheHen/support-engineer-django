import os
import requests

from dotenv import load_dotenv
from django.views.generic import TemplateView

load_dotenv()

class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_name = os.getenv("FLY_APP_NAME")
        machine_id = os.getenv("FLY_ALLOC_ID")
        api_token = os.getenv("FLY_API_TOKEN")
        url = f"https://api.machines.dev/v1/apps/{app_name}/machines/{machine_id}"
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            context["machines"] = response.json()
            
        return context
