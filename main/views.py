from django.http import JsonResponse
from .models import ExpertProfile

def expert_profile_list(request):
    experts = ExpertProfile.objects.all()
    data = [
        {
            "id": expert.id,
            "name": expert.name,
            "bio": expert.short_bio,
            "expertise": expert.expertise
        }
        for expert in experts
    ]
    return JsonResponse(data, safe=False)

def expert_profile_detail(request, pk):
    try:
        expert = ExpertProfile.objects.get(pk=pk)
        data = {
            "id": expert.id,
            "name": expert.name,
            "bio": expert.short_bio,
            "expertise": expert.expertise,
            "contact_info": expert.contact_info,
            "institution": expert.institution
        }
        return JsonResponse(data)
    except ExpertProfile.DoesNotExist:
        return JsonResponse({"error": "Expert not found"}, status=404)

