# # 在函数中修改列表

# # 首先创建一个列表，其中包含一些要打印的设计
# unprited_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []

# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移动到列表 completed_models 中：
# while unprited_designs:
# 	current_design = unprited_designs.pop()
# 	print("Print model:" + current_design)
# 	completed_models.append(current_design)

# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
# 	print("\t" + completed_model)

#--------------------------------------------------------------------
def print_models(unprited_designs,completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移动到列表 completed_models 中：
	"""
	while unprited_designs:
		current_design = unprited_designs.pop()
		print("Print model:" + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t" + completed_model)

unprited_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprited_designs,completed_models)
show_completed_models(completed_models)
