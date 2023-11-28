from django.shortcuts import render, redirect, get_object_or_404
from .models import Role, Competition, Member_Detail, Team
from django.contrib import messages

def home(request):
    return render(request, 'core/vog_home.html')


def register(request,competition_name):
    if request.method == "POST":
        team_name = request.POST.get('team_name')
        your_city = request.POST.get('your_city')
        competition = get_object_or_404(Competition,competition_name=competition_name)
        postal_code = request.POST.get('postal_code')
        # Process team details
        # if not team_name:
        #     messages.error(request, "Team name is required")

        # Validate city
        # if not your_city:
        #     messages.error(request, "City is required")
        # Process member details
        names = request.POST.getlist('name')
        emails = request.POST.getlist('Email')
        phone_numbers = request.POST.getlist('Phone_Number')
        genders = request.POST.getlist('gender')
        role_ids = request.POST.getlist('role')
        num_participants = len(names)
        # for i in range(len(names)):
        #     name = names[i]
        #     email = emails[i]
        #     phone_number = phone_numbers[i]
        #     gender = genders[i]
        #     role_id = role_ids[i]

        #     # Validate name
        #     if not name:
        #         messages.error(request, f"Member {i + 1} name is required")

        #     # Validate email
        #     if not (email):
        #         messages.error(request, f"Member {i + 1} email is invalid")

        #     # Validate phone number
        #     if not phone_number:
        #         messages.error(request, f"Member {i + 1} phone number is invalid")

        #     # Validate role
        #     try:
        #         role = Role.objects.get(pk=role_id)
        #     except Role.DoesNotExist:
        #         messages.error(request, f"Member {i + 1} role is invalid")
        #     # Form is invalid, return to the registration page with error messages
        # #     return render(request, 'core/reg_vog.html', {
        # #         'roles': roles,
        # #         'competitions': competitions,
        # # })
        team = Team.objects.create(
            team_name=team_name,
            competition=competition,          
        )
        team.save()
        for i in range(num_participants):
            role = get_object_or_404(Role, pk=int(role_ids[i]))

            memberdetails = Member_Detail.objects.create(
                name=names[i],
                email=emails[i],
                phone_number=phone_numbers[i],
                your_city=your_city,
                gender=genders[i],
                competition=competition,
                role=role,
                Postal_code=postal_code if postal_code else None,
                is_leader=(i == 0)  # First member is the leader
            )
            memberdetails.save()

        messages.success(request,f'you have successfully logged in')
        return redirect('Vogue-Home')
    
    roles = Role.objects.all()
    competitions = Competition.objects.all()

    return render(request, 'core/reg_vog.html', {
        'roles': roles,
        'competitions': competitions,
    })
