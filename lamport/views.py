from django.shortcuts import render, redirect
from .models import LamportUser
import hashlib
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')


def login(request):
    hash_iterations = None

    if request.method == 'POST':
        username = request.POST['username']
        client_response = request.POST['client_response']

        try:
            user = LamportUser.objects.get(username=username)
            hash_iterations = user.hash_iterations
            server_password = user.password_hash
            if server_password == hashlib.sha256(client_response.encode()).hexdigest():
                # Authentication successful, redirect to a success page
                if hash_iterations == 1:
                    return redirect('set_new_password', username=username)
                else:
                    user.hash_iterations -= 1
                user.password_hash = client_response
                user.save()
                return render(request, 'success.html')
            else:
                # Authentication failed, redirect to a failure page
                return render(request, 'failure.html')
        except LamportUser.DoesNotExist:
            # User not found, redirect to a failure page
            return render(request, 'failure.html')

    return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        hash_iterations = int(request.POST['hash_iterations'])
        hashed_password = request.POST['hashed_password']

        LamportUser.objects.create(username=username, hash_iterations=hash_iterations, password_hash=hashed_password)

        # Redirect to a success page or login page after successful signup
        return render(request, 'signup_success.html')

    return render(request, 'signup.html')


def get_hash_iterations(request):
    username = request.GET.get('username', '')
    try:
        user = LamportUser.objects.get(username=username)
        hash_iterations = user.hash_iterations
        return JsonResponse({'hash_iterations': hash_iterations})
    except LamportUser.DoesNotExist:
        return JsonResponse({'error': 'User not found'})


def set_new_password(request, username):
    user = LamportUser.objects.get(username=username)

    if request.method == 'POST':
        new_password = request.POST['new_password']
        new_hash_iterations = int(request.POST['new_hash_iterations'])

        # Update user record with new password and hash iteration
        user.password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        user.hash_iterations = new_hash_iterations
        user.save()

        return render(request, 'success.html', {'hash_iterations': new_hash_iterations})

    return render(request, 'set_new_password.html', {'username': username, 'current_hash_iterations': user.hash_iterations})