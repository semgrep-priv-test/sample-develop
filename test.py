def danger2(request):
    # ruleid: command-injection-os-system
    image = request.POST['image']
    os.system("./face-recognize %s --N 24" % image)
