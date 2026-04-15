def args_logger(*args, **kwargs):
    counter = 1
    for arg in args:
        print(f"{counter}. {arg}")
        counter +=1 


    for key, value in sorted(kwargs.items()):
        print("* {0}: {1}".format(key,value))
        
