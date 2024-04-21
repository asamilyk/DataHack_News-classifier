from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'news/index.html')


def get_cats_tags(request):
    if request.method == 'POST':
        title = request.POST.get('text_1', '')  # Получаем значение из поля с именем 'text_1'
        description = request.POST.get('text_2', '')  # Получаем значение из поля с именем 'text_2'
        text = request.POST.get('text_3', '')  # Получаем значение из поля с именем 'text_3'

        print(title, description, text)

        tags = [title, description, text]
        category = 'some_category'

        response_data = {
            'tags': tags,
            'category': category
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)


def get_tags(request):
    if request.method == 'POST':
        title = request.POST.get('text_1', '')  # Получаем значение из поля с именем 'text_1'
        description = request.POST.get('text_2', '')  # Получаем значение из поля с именем 'text_2'
        text = request.POST.get('text_3', '')  # Получаем значение из поля с именем 'text_3'

        print(title, description, text)

        tags = [title, description, text]
        category = 'some_category'

        response_data = {
            'tags': tags,
            'category': category
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)


def get_category(request):
    if request.method == 'POST':
        title = request.POST.get('text_1', '')  # Получаем значение из поля с именем 'text_1'
        description = request.POST.get('text_2', '')  # Получаем значение из поля с именем 'text_2'
        text = request.POST.get('text_3', '')  # Получаем значение из поля с именем 'text_3'

        print(title, description, text)

        tags = [title, description, text]
        category = 'some_category'

        response_data = {
            'tags': tags,
            'category': category
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)


def get_picture(request):
    if request.method == 'POST':
        title = request.POST.get('text_1', '')  # Получаем значение из поля с именем 'text_1'
        description = request.POST.get('text_2', '')  # Получаем значение из поля с именем 'text_2'
        text = request.POST.get('text_3', '')  # Получаем значение из поля с именем 'text_3'

        tags = [title, description, text]
        category = 'some_category'

        response_data = {
            'tags': tags,
            'category': category
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)
