# 导入整个模块
# import pizza
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 导入特定模块，可根据需要从模块中导入任意数量的函数，以逗号（,）号分隔
# from pizza import make_pizza
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')

# 使用as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定别名
# from pizza import make_pizza as mp
# mp(16,'pepperoni')
# mp(12,'mushrooms','green peppers','extra cheese')

# 给模块指定别名
# import pizza as p
# p.make_pizza(16,'pepperoni')
# p.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 导入模块中的所有函数，使用（*）
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
