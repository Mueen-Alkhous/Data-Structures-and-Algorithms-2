import random
from matplotlib import pyplot as plt

"""
This Module implements solution for the knapsak problem in the three most basic methods
1 - Profit and Weight ratio i.e Pi/Wi
2 - Maximum Profit
3 - Minimum Weight
"""


def min_wi_sort(wi, pi):
  lst = sorted(list(zip(wi, pi)))
  for i in range(len(lst) - 1):
    if(lst[i][0] == lst[i+1][0]):
      if(lst[i][1] < lst[i+1][1]):
        lst[i], lst[i+1] = lst[i+1], lst[i]
  return lst


def max_pi_sort(pi, wi):
  lst = sorted(list(zip(pi, wi)), reverse=True)
  for i in range(len(lst) - 1):
    if(lst[i][0] == lst[i+1][0]):
      if(lst[i][1] > lst[i+1][1]):
        lst[i], lst[i+1] = lst[i+1], lst[i]
  return lst


def PiWi(n, c, pi, wi):
  pi_div_wi = []
  for i in range(n):
    pi_div_wi.append((pi[i]/wi[i], pi[i], wi[i]))
  pi_div_wi.sort(reverse=True)
  print(pi_div_wi)
  sum = 0
  for i in range(n):
    if (c == 0):
      break
    elif(pi_div_wi[i][2] <= c):
      c = c-pi_div_wi[i][2]
      sum += pi_div_wi[i][1]
    else:
      partial = c/pi_div_wi[i][2]
      sum += pi_div_wi[i][1]*partial
      break
  return sum


def max_profit(n, c, pi, wi):
  pi_wi = max_pi_sort(pi, wi)
  sum = 0
  for i in range(n):
    if(c == 0):
      break
    elif(pi_wi[i][1] <= c):
      c -= pi_wi[i][1]
      sum += pi_wi[i][0]
    else:
      partial = c/pi_wi[i][1]
      sum += pi_wi[i][0]*partial
      break
  return sum


def min_weight(n, c, pi, wi):
  wi_pi = min_wi_sort(wi, pi)
  sum = 0
  for i in range(n):
    if(c == 0):
      break
    elif(wi_pi[i][0] <= c):
      c -= wi_pi[i][0]
      sum += wi_pi[i][1]
    else:
      partial = c/wi_pi[i][0]
      sum += wi_pi[i][1]*partial
      break
  return sum

def comparison(n, c , pi, wi):
  print("Pi/Wi = {:>9}".format(str(PiWi(n, c, pi, wi))))
  print("Max_Profit = " + str(max_profit(n, c, pi, wi)))
  print("Min_Profit = " + str(min_weight(n, c, pi, wi)))



n=7
c = 80
pi = [70,20,39,37,7,5,10]
wi = [31,10,20,19,4,3,6]
comparison(n, c, pi, wi)




""" 
n=7
c=16
pi = [10, 15, 12, 4, 6, 16, 8]
wi = [2, 4, 5, 4, 2, 3, 3]
comparison(n, c, pi, wi)
"""



""" 
n=7
c=16
pi = [10, 15, 12, 4, 6, 16, 8]
wi = [2, 4, 5, 4, 2, 3, 3]
comparison(n, c, pi, wi)
"""

def trail():
  n = random.randint(10, 21)
  c = random.randint(50, 151)
  P = []
  W = []
  for i in range(n):
    P.append(random.randint(1, 41))
    W.append(random.randint(1, 41))
  return n, c, P, W

def play(n):
  ratio = []
  max_p = []
  min_w = []
  for i in range(n):
    x = trail()
    ratio.append(PiWi(x[0], x[1], x[2], x[3])/10)
    max_p.append(max_profit(x[0], x[1], x[2], x[3])/10)
    min_w.append(min_weight(x[0], x[1], x[2], x[3])/10)
  return ratio, max_p, min_w


# Scatter plot

# t = play(20)
# x=[i for i in range(1, len(t[0])+1)]
# plt.scatter(x, t[0], marker='^',c="g")
# plt.scatter(x, t[1], marker='o',c="r")
# plt.scatter(x, t[2], marker='*',c="b")
# plt.plot(x, t[0],c="g")
# plt.plot(x, t[1],c="r")
# plt.plot(x, t[2],c="b")
# plt.show()


# Bar plot

# t = play(1000)
# ratio = 0
# maxim = 0
# minim = 0
# all_eq = 0
# min_eq_r = 0
# max_eq_r = 0
# max_eq_min = 0
# for i in range(1000):
#   if (t[0][i] > t[1][i] and t[0][i] > t[2][i]):
#     ratio += 1
#   elif(t[1][i] > t[0][i] and t[1][i] > t[2][i]):
#     maxim += 1
#   elif(t[2][i] > t[0][i] and t[2][i] > t[1][i]):
#     minim += 1
#   elif(t[2][i] == t[1][i] and t[2][i] == t[0][i] and t[1][i]==t[0][i]):
#     all_eq += 1
#   elif(t[2][i] == t[1][i]):
#     max_eq_min += 1
#   elif(t[1][i] == t[0][i]):
#     max_eq_r += 1
#   elif(t[2][i] == t[0][i]):
#     min_eq_r += 1

# cases = ["Ratio", "Max", "Min", "Max=Min", "Max=Ratio", "Min=Ratio", "All Equal"]
# counts = [ratio, maxim, minim, max_eq_min, max_eq_r, min_eq_r, all_eq]
# colors = ["tab:green", "tab:red", "tab:blue", "tab:green", "tab:red", "tab:blue", "tab:pink"]
# p = plt.bar(cases, counts, color=colors)
# plt.bar_label(p, counts)
# plt.show()
