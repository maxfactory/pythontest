"""定义了函数print_models()，包含两个形参：一个需要打印的设计列表和一个打印好的模型列表，
给定这两个列表，这个函数模拟打印每个设计的过程：
将设计逐个地从未打印的设计列表中取出，并加入到打印好的模型列表中。"""
def print_models(unprinted_designs,completed_models):
	"""模拟打印每个设计，直到没有要打印的设计为止，
	打印每个设计后，都将其移到completed_models中"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# 模拟根据制作3D打印模型的过程
		print("Print model:" + current_design)
		completed_models.append(current_design)

"""定义函数show_completed_models()，包含一个形参：打印好的模型列表。
给定这个列表，函数show_completed_models()显示打印出来的每个模型的名称。"""
def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t" + completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)	# 如果想要保留原列表，只需将此行代码改为：print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
