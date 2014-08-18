# vim: set ts=4 noet:
#
import sorting

def allPermu(l, lp=[], p=0):
    if p >= len(l):
        lp.append(''.join(l))
        return

    for i in range(p, len(l)):
      	sorting.swap(l, p, i)
        allPermu(l, lp, p+1)
      	sorting.swap(l, p, i)

