from sklearn import tree #导入决策树
from sklearn.datasets import load_iris #导入datasets创建数组
iris = load_iris()#鸢尾花数据集
iris_data=iris.data #选择训练数组
iris_target=iris.target #选择对应标签数组

clf = tree.DecisionTreeClassifier() #创建决策树模型
clf=clf.fit(iris_data,iris_target) #拟合模型
import graphviz #导入决策树可视化模块
dot_data = tree.export_graphviz(clf, out_file=None) #以DOT格式导出决策树
print(dot_data)
# digraph Tree {
# node [shape=box, fontname="helvetica"] ;
# edge [fontname="helvetica"] ;
# 0 [label="X[3] <= 0.8\ngini = 0.667\nsamples = 150\nvalue = [50, 50, 50]"] ;
# 1 [label="gini = 0.0\nsamples = 50\nvalue = [50, 0, 0]"] ;
# 0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
# 2 [label="X[3] <= 1.75\ngini = 0.5\nsamples = 100\nvalue = [0, 50, 50]"] ;
# 0 -> 2 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
# 3 [label="X[2] <= 4.95\ngini = 0.168\nsamples = 54\nvalue = [0, 49, 5]"] ;
# 2 -> 3 ;
# 4 [label="X[3] <= 1.65\ngini = 0.041\nsamples = 48\nvalue = [0, 47, 1]"] ;
# 3 -> 4 ;
# 5 [label="gini = 0.0\nsamples = 47\nvalue = [0, 47, 0]"] ;
# 4 -> 5 ;
# 6 [label="gini = 0.0\nsamples = 1\nvalue = [0, 0, 1]"] ;
# 4 -> 6 ;
# 7 [label="X[3] <= 1.55\ngini = 0.444\nsamples = 6\nvalue = [0, 2, 4]"] ;
# 3 -> 7 ;
# 8 [label="gini = 0.0\nsamples = 3\nvalue = [0, 0, 3]"] ;
# 7 -> 8 ;
# 9 [label="X[2] <= 5.45\ngini = 0.444\nsamples = 3\nvalue = [0, 2, 1]"] ;
# 7 -> 9 ;
# 10 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2, 0]"] ;
# 9 -> 10 ;
# 11 [label="gini = 0.0\nsamples = 1\nvalue = [0, 0, 1]"] ;
# 9 -> 11 ;
# 12 [label="X[2] <= 4.85\ngini = 0.043\nsamples = 46\nvalue = [0, 1, 45]"] ;
# 2 -> 12 ;
# 13 [label="X[0] <= 5.95\ngini = 0.444\nsamples = 3\nvalue = [0, 1, 2]"] ;
# 12 -> 13 ;
# 14 [label="gini = 0.0\nsamples = 1\nvalue = [0, 1, 0]"] ;
# 13 -> 14 ;
# 15 [label="gini = 0.0\nsamples = 2\nvalue = [0, 0, 2]"] ;
# 13 -> 15 ;
# 16 [label="gini = 0.0\nsamples = 43\nvalue = [0, 0, 43]"] ;
# 12 -> 16 ;
# }
print("\n")
graph = graphviz.Source(dot_data)
print(graph.source)
# graph.render('test-output/test-table.gv', view=True) #使用garphviz将决策树转存PDF存放到桌面，文件名叫iris
# dot.render('test-output/test-table.gv', view=True)

# digraph Tree {
# node [shape=box, fontname="helvetica"] ;
# edge [fontname="helvetica"] ;
# 0 [label="X[3] <= 0.8\ngini = 0.667\nsamples = 150\nvalue = [50, 50, 50]"] ;
# 1 [label="gini = 0.0\nsamples = 50\nvalue = [50, 0, 0]"] ;
# 0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
# 2 [label="X[3] <= 1.75\ngini = 0.5\nsamples = 100\nvalue = [0, 50, 50]"] ;
# 0 -> 2 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
# 3 [label="X[2] <= 4.95\ngini = 0.168\nsamples = 54\nvalue = [0, 49, 5]"] ;
# 2 -> 3 ;
# 4 [label="X[3] <= 1.65\ngini = 0.041\nsamples = 48\nvalue = [0, 47, 1]"] ;
# 3 -> 4 ;
# 5 [label="gini = 0.0\nsamples = 47\nvalue = [0, 47, 0]"] ;
# 4 -> 5 ;
# 6 [label="gini = 0.0\nsamples = 1\nvalue = [0, 0, 1]"] ;
# 4 -> 6 ;
# 7 [label="X[3] <= 1.55\ngini = 0.444\nsamples = 6\nvalue = [0, 2, 4]"] ;
# 3 -> 7 ;
# 8 [label="gini = 0.0\nsamples = 3\nvalue = [0, 0, 3]"] ;
# 7 -> 8 ;
# 9 [label="X[2] <= 5.45\ngini = 0.444\nsamples = 3\nvalue = [0, 2, 1]"] ;
# 7 -> 9 ;
# 10 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2, 0]"] ;
# 9 -> 10 ;
# 11 [label="gini = 0.0\nsamples = 1\nvalue = [0, 0, 1]"] ;
# 9 -> 11 ;
# 12 [label="X[2] <= 4.85\ngini = 0.043\nsamples = 46\nvalue = [0, 1, 45]"] ;
# 2 -> 12 ;
# 13 [label="X[0] <= 5.95\ngini = 0.444\nsamples = 3\nvalue = [0, 1, 2]"] ;
# 12 -> 13 ;
# 14 [label="gini = 0.0\nsamples = 1\nvalue = [0, 1, 0]"] ;
# 13 -> 14 ;
# 15 [label="gini = 0.0\nsamples = 2\nvalue = [0, 0, 2]"] ;
# 13 -> 15 ;
# 16 [label="gini = 0.0\nsamples = 43\nvalue = [0, 0, 43]"] ;
# 12 -> 16 ;
# }