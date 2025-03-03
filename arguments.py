def arguments(*argv, **kwargs):
    for arg in argv:
        print(arg)
    
    for k, value in kwargs:
        print(k + " " + "is" + " " + value)
        

arguments("tanmay", "chinmay", "davis", s2="tanmay", s3="chionmau")
