from django.conf import settings
import requests

 
class PayStack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    base_url = 'https://api.paystack.co'  # Corrected URL
    
    def verify_payment(self, ref, amount):
        path = f"transaction/verify/{ref}"
        
        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}/{path}"  # Construct the full URL
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']
    