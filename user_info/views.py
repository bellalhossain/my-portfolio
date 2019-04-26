from django.shortcuts import render
 
 
def show_user_info(request):
    """
    A django view to show user's Information
    """
    print("request data: ", request.POST)
    if request.method == 'POST':
        user_name = request.POST["user_name"]
        context = {"name": user_name}
        return render(request, 'user_info/user_info.html', context)
    return render(request, 'user_info/user_info.html')