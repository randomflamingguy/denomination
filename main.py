def no_notes(a):
    Q = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    x = 0
    for i in range(9):
        q = Q[i]
        x = a//q
        print("Notes of {} = {}".format(q, x))
        a = a%q
amount = int(input("Enter total amount :"))
no_notes(amount)