from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """Cache FAQs for faster responses."""
        cache_key = f"faq_list_{request.GET.get('lang', 'en')}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)  # Return cached data directly

        # If no cached data, fetch from DB
        response = super().list(request, *args, **kwargs)
        
        # Cache the response for future requests
        cache.set(cache_key, response.data, timeout=600)  # Cache for 10 minutes

        return response  # Ensure 'response' is always returned

