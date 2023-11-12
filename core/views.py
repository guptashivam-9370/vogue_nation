from django.shortcuts import render, redirect, get_object_or_404
from .models import Role, Competition, Member_Detail, Team


def home(request):
    return render(request, 'core/vog_home.html')


def register(request,competition):
    if request.method == 'POST':
        team_name = request.POST.get('team_name', '')
        your_city = request.POST.get('your_city', '')
        competition = get_object_or_404(Competition,competition_name = competition)
        postal_code = request.POST.get('postal_code')
        # Process team details
        team = Team.objects.create(
            team_name=team_name,
            competition=competition,          
        )

        # Process member details
        names = request.POST.getlist('name')
        emails = request.POST.getlist('Email')
        phone_numbers = request.POST.getlist('Phone_Number')
        genders = request.POST.getlist('gender')
        role_ids = request.POST.getlist('role')
        num_participants = len(names)
        for i in range(num_participants):
            role = get_object_or_404(Role, pk=int(role_ids[i]))

            Member_Detail.objects.create(
                name=names[i],
                email=emails[i],
                phone_number=phone_numbers[i],
                your_city=your_city,
                gender=genders[i],
                competition=competition,
                role=role,
                Postal_code = postal_code,
                is_leader=(i == 0)  # First member is the leader
            )

        # if(not team_name or not your_city or not postal_code):
        #     # If the form data is not valid, return to the registration page with an error message
        #     role = Role.objects.all()
        #     competitions = Competition.objects.all()
        #     return render(request, 'core/reg_vog.html', {
        #         'roles': roles,
        #         'competitions': competitions,
        #         'error_message': 'Please fill in all required fields.',
        #     })
        return redirect('Vogue-Home')
    roles = Role.objects.all()
    competitions = Competition.objects.all()

    return render(request, 'core/reg_vog.html', {
        'roles': roles,
        'competitions': competitions,
    })
