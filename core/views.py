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
        names = request.POST.getlist('name')
        emails = request.POST.getlist('Email')
        phone_numbers = request.POST.getlist('Phone_Number')
        genders = request.POST.getlist('gender')
        role_ids = request.POST.getlist('role')
        num_participants = len(names)
        team = Team.objects.create(
            team_name=team_name,
            competition=competition,          
        )
        competitionss = Competition.objects.get(competition_name=competition_name)
        roles = Role.objects.filter(competitions=competitionss)
        competitions = Competition.objects.all()
        role_counts = {}
        for i in range(len(names)):
            name = names[i]
            email = emails[i]
            phone_number = phone_numbers[i]

            # Validate name
            if not name or not (email) or not phone_number or not team_name or  not phone_number.isdigit():
                messages.error(request, f"Please enter All nessacary details properly")

                return render(request, 'core/reg_vog.html', {
                'competition' : competition_name,
                'roles': roles,
                'competitions': competitions,
                })
        for role in roles:
            role_counts[role]=0
        for i in range(num_participants):
            role = get_object_or_404(Role, pk=int(role_ids[i]))
            role_counts[role]+=1
        for role, count in role_counts.items():
            if count < role.min_member:
                messages.error(request, f'The role {role} requires at least {role.min_member} participants.')
                return render(request, 'core/reg_vog.html', {
                'roles': roles,
                'competitions': competitions,
                })
        team.save()
        for i in range(num_participants):
            memberdetails = Member_Detail.objects.create(
                name=names[i],
                email=emails[i],
                phone_number=phone_numbers[i],
                your_city=your_city,
                gender=genders[i],
                competition=competition,
                role=role,
                team=team,
                Postal_code=postal_code if postal_code else None,
                is_leader=(i == 0)  # First member is the leader
            )
            memberdetails.save()
        

        messages.success(request,f'you have successfully logged in')
        return redirect('Vogue-Home')
    
    competitions = Competition.objects.all()
    competitionss = Competition.objects.get(competition_name=competition_name)
    roles = Role.objects.filter(competitions=competitionss)
    return render(request, 'core/reg_vog.html', {
        'competition' : competition_name,
        'roles': roles,
        'competitions': competitions,
    })
