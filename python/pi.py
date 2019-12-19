#_*_ coding=utf-8 *_*
## {{{ http://code.activestate.com/recipes/578130/ (r5)
def pi(places=10):
  """Computes pi to given number of decimal places
    参数places表示要返回的pi的小数点后位数  
    方法：先整体扩大10**8（10的八次方）倍，然后计算完成后再缩小10的八次方倍
  """
   
  # 3 + 3*(1/24) + 3*(1/24)*(9/80) + 3*(1/24)*(9/80)*(25/168)
  # The numerators 1, 9, 25, ... are given by (2x + 1) ^ 2
  # The denominators 24, 80, 168 are given by (16x^2 -24x + 8)
  extra = 8
  one = 10 ** (places+extra)
  t, c, n, na, d, da = 3*one, 3*one, 1, 0, 0, 24
  #这里的n 和d 分别为每一项的分子与分母 ,na 和 da 分别为分子和分分母后一项比前一项增加的数值
  #这里的//可不是C++中的注释,而是除的意思
  while t > 1: 
    n, na, d, da = n+na, na+8, d+da, da+32
    t = t * n // d
    c += t
  return c // (10 ** extra)
 
def picirc(radius, aspect_ratio=5):
  """Display the digit of pi in a circle of given radius
    radius:显示的半径
    aspect_ratio：调节显示的比率参数
  """
  #display_width为各行的显示长度
  display_width = int(radius * aspect_ratio + 10)
  pi_str = repr(pi(int(2 * radius ** 2 * aspect_ratio)))
  pos = 0
  #cols为每一行中要显示的数字个数
  for i in range(2 * radius):
    cols = int(0.5 + aspect_ratio * (radius**2 - (radius-(i+0.5))**2) ** 0.5)
    print(pi_str[pos:pos+cols].center(display_width)) #将产生的pi数值生成的文本列表中相应的位数取出来显示在当前行
    pos += cols
 
if __name__ == '__main__':
   
  picirc(16)
## end of http://code.activestate.com/recipes/578130/ }}}