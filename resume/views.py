from datetime import datetime
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Certificate, Education, Experience, Link, Project, CustomUser
from django.http import Http404

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def get_github_projects(username, token):
    github_token = f'{token}'
    headers = {'Authorization': f'token {github_token}'}
    api_url = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            projects = response.json()
            return projects
        else:
            print(f"Failed to get projects from Github. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

pages = {
    "1":{
        "name":"About Me", # Experience
        "url":"aboutme",
    },
    "2":{
        "name":"Education",
        "url":"education",
    },
    "3":{
        "name":"Project",
        "url":"project",
    },
    "4":{
        "name":"Certificate",
        "url":"certificate",
    },
    "5":{
        "name":"Contact", # Links
        "url":"contact",
    },
}

pagesAdd = {
    "1":{
        "name":"Certificate",
        "url":"certificate",
    },
    "2":{
        "name":"Education",
        "url":"education",
    },
    "3":{
        "name":"Project",
        "url":"project",
    },
    "4":{
        "name":"Experience",
        "url":"experience",
    },
    "5":{
        "name":"Contact",
        "url":"contact",
    },
}

def certificateAdd(request):
    try:
        if request.user.is_authenticated and request.method == 'POST':
            certificate_name = request.POST["certificate_name"]
            issued_by = request.POST["issued_by"]
            acquisition_date = request.POST["acquisition_date"]
            qualification_id = request.POST["qualification_id"]
            certificate_pdf = request.FILES["certificate_pdf"]
            certificate_link = request.POST["certificate_link"]
            user = request.user

            # Convert the date string to a datetime object
            acquisition_date = datetime.strptime(acquisition_date, '%Y-%m-%d').date()

            Certificate.objects.create(
                user=user,
                certificate_name=certificate_name,
                issued_by=issued_by,
                acquisition_date=acquisition_date,
                qualification_id=qualification_id,
                certificate_pdf=certificate_pdf,
                certificate_link=certificate_link
            )
            return redirect('certificate')  # Redirect to a success page or the same page after adding the certificate
        else:
            return render(request, 'resume/certificateAdd.html', {'pagesAdd': pagesAdd})
    
    except Exception as ex:
        print(ex)
        return render(request, 'resume/certificateAdd.html', {'pagesAdd': pagesAdd})

def educationAdd(request):
    try:
        if request.user.is_authenticated and request.method == 'POST':
            school_name = request.POST["school_name"]
            education_type = request.POST["education_type"]
            start_date = request.POST["start_date"]
            end_date = request.POST["end_date"]
            location = request.POST["location"]
            education_image = request.FILES["education_image"]
            user = request.user

            # Convert the date strings to datetime objects
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            Education.objects.create(
                user=user,
                school_name=school_name,
                education_type=education_type,
                start_date=start_date,
                end_date=end_date,
                location=location,
                education_image=education_image,
            )

            return redirect('education')  # Redirect to a success page or the same page after adding the education
        else:
            return render(request, 'resume/educationAdd.html', {'pagesAdd': pagesAdd})
    except Exception as ex:
        print(ex)
        return render(request, 'resume/educationAdd.html', {'pagesAdd': pagesAdd})

def experienceAdd(request):
    try:
        if request.user.is_authenticated and request.method == 'POST':
            experience_name = request.POST["experience_name"]
            sub_description = request.POST["sub_description"]
            start_date = request.POST["start_date"]
            end_date = request.POST["end_date"]
            location = request.POST["location"]
            experience_image = request.FILES["experience_image"]
            user = request.user

            # Convert the date strings to datetime objects
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            Experience.objects.create(
                user=user,
                experience_name=experience_name,
                sub_description=sub_description,
                start_date=start_date,
                end_date=end_date,
                location=location,
                experience_image=experience_image,
            )
            return redirect('experience')  # Redirect to a success page or the same page after adding the experience
        else:
            return render(request, 'resume/experienceAdd.html', {'pagesAdd': pagesAdd})
    except Exception as ex:
        print(ex)
        return render(request, 'resume/experienceAdd.html', {'pagesAdd': pagesAdd})

def contactAdd(request):
    try:
        if request.user.is_authenticated and request.method == 'POST':
            url = request.POST["url"]
            icon = request.FILES["icon"]
            user = request.user

        
            Link.objects.create(
                user=user,
                url=url,
                icon=icon,
            )

            return redirect('contact')  # Redirect to a success page or the same page after adding the link
        else:
            return render(request, 'resume/contactAdd.html', {'pagesAdd': pagesAdd})
    except Exception as ex:
        print(ex)
        return render(request, 'resume/contactAdd.html', {'pagesAdd': pagesAdd})

def projectAdd(request):
    try:
        if request.user.is_authenticated and request.method == 'POST':
            project_name = request.POST["project_name"]
            description = request.POST["description"]
            project_link = request.POST["project_link"]
            user = request.user

            # Convert the date strings to datetime objects
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            Project.objects.create(
                user=user,
                project_name=project_name,
                description=description,
                project_link=project_link,
            )

            return redirect('project')  # Redirect to a success page or the same page after adding the project
        else:
            return render(request, 'resume/projectAdd.html', {'pagesAdd': pagesAdd})
    except Exception as ex:
        print(ex)
        return render(request, 'resume/projectAdd.html', {'pagesAdd': pagesAdd})

def resume(request):
    try:
        user = CustomUser.objects.get(id=2)
        certificate = Certificate.objects.filter(user_id=user.id).order_by('-acquisition_date')
        education = Education.objects.filter(user_id=user.id).order_by('-end_date')
        experience = Experience.objects.filter(user_id=user.id).order_by('-end_date')
        project = list(Project.objects.filter(user_id=user.id).order_by('-update_date'))
        github_projects = get_github_projects(username='dvaser', token='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')
        # print(github_projects[10])
        if github_projects:
            for project_data in github_projects:
                project_name = project_data['name']
                description = project_data['description']
                project_link = project_data['html_url']
                project_topics = project_data['topics']
                project_language = project_data['language']
                project_updated = datetime.strptime(project_data['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
                try:
                    project_item = next(project_item for project_item in project if project_item.project_name == project_name)
                    project_item.description = description
                    project_item.topics = project_topics
                    project_item.language = project_language
                    project_item.update_date = project_updated
                    if not project_item.project_link:
                        project_item.project_link = project_link
                    project_item.save()
                except StopIteration:
                    Project.objects.create(
                        user=user,
                        project_name=project_name,
                        description=description,
                        project_link=project_link,
                        update_date=project_updated,
                        language=project_language,
                        topics=project_topics,
                    )
        link = Link.objects.filter(user_id=user.id)
    except Exception as ex:
        certificate = None
        education = None
        experience = None
        project = None
        link = None
        print(ex)

    return render(request, 'resume/resume.html', {
        "pages":pages,
        "certificates":certificate,
        "educations":education,
        "experiencies":experience,
        "projects":project,
        "links":link,
        })

def delete(request, object_type, object_id):
    try:
        if object_type == 'Certificate':
            certificate = get_object_or_404(Certificate, id=object_id)
            certificate.delete()
        elif object_type == 'Education':
            education = get_object_or_404(Education, id=object_id)
            education.delete()
        elif object_type == 'Experience':
            experience = get_object_or_404(Experience, id=object_id)
            experience.delete()
        elif object_type == 'Link':
            link = get_object_or_404(Link, id=object_id)
            link.delete()
        elif object_type == 'Project':
            project = get_object_or_404(Project, id=object_id)
            project.delete()
        else:
            raise ValueError("404")
        return redirect('resume')
    except Exception as ex:
        print(ex)