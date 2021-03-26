def towers(top, frm, inter, to):
    if top == 1:
        print("disk 1 from " + frm + "to" + to)
    else:
        towers(top-1, frm, to, inter)
        print("disk" + str(top) + "from" + frm + "to" + to)
        towers(top-1, to, inter, frm)
if __name__ == "__main__":
    num = 4
    towers(num, 'A', 'B', 'C')
