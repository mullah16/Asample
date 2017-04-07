def product_matrix(value):
    fmt_str = "{:>4}"
    print fmt_str.format("*"),

    i=1
    while i<=n:
        print fmt_str.format(i),
        i+=1
    print

    i=1

    while i<=n:
        print fmt_str.format(i),
        j=1
        while j<=n:
            print fmt_str.format(i*j),
            j = j+1
        print
        i=i+1



n= int(raw_input("enter the number"))

product_matrix(n)