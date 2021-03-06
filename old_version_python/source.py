element = [['铁矿', '铜矿', '硅矿', '钛矿', '石矿', '煤矿', '原油', '', '', '', '水', '临界光子'],
           ['铁块', '铜块', '高纯硅块', '钛块', '石材', '高能石墨', '精炼油', '塑料', '石墨烯', '', '', ''],
           ['磁铁', '磁线圈', '晶格硅', '钛合金', '玻璃', '金刚石', '氢', '有机晶体', '可燃冰', '液氢燃料棒', '氘核燃料棒', '反物质燃料棒'],
           ['钢材', '电动机', '', '钛化玻璃', '棱镜', '', '', '', '钛晶石', '推进器', '加力推进器', '奇异物质'],
           ['齿轮', '电磁涡轮', '', '电路板', '引力透镜', '硫酸', '重氢', '位面过滤器', '碳纳米管', '物流运输机', '星际物流运输船', '小型运载火箭'],
           ['电浆激发器', '超级磁场环', '粒子宽带', '处理器', '卡西米尔晶体', '粒子容器', '空间翘曲器', '', '', '太阳帆', '框架材料', '戴森球组件'],
           ['光子合并器', '', '微晶原件', '量子芯片', '', '', '', '反物质', '湮灭约束球', '', '', ''],
           ['电磁矩阵', '能量矩阵', '结构矩阵', '信息矩阵', '引力矩阵', '宇宙矩阵', '', '', '', '', '', '地基'],
           ['传送带', '高速传送带', '极速传送带', '分拣器', '高速分拣器', '极速分拣器', '制造台 Mk.I', '制造台 Mk.II', '制造台 Mk.III', '电弧熔炉', '', '']]

# Format: [[production speed (no./min)], ['resource', 'amount'], ..]
production = dict()
production['铁矿'] = [[180]]
production['铜矿'] = [[180]]
production['硅矿'] = [[180]]
production['钛矿'] = [[180]]
production['石矿'] = [[180]]
production['煤矿'] = [[180]]
production['原油'] = [[120]]
production['水'] = [[60]]
production['临界光子'] = [[3]]
# ---------------------------------------------
production['铁块'] = [[60], ['铁矿', 1]]
production['铜块'] = [[60], ['铜矿', 1]]
production['高纯硅块'] = [[30], ['硅矿', 2]]
production['钛块'] = [[30], ['钛矿', 2]]
production['石材'] = [[60], ['石矿', 1]]
production['高能石墨'] = [[30], ['煤矿', 2]]
production['精炼油'] = [[30]]
production['塑料'] = [[20], ['精炼油', 2], ['高能石墨', 1]]
production['石墨烯'] = [[40], ['高能石墨', 1.5], ['硫酸', 0.5]]
production['可燃冰'] = [[60]]
# ---------------------------------------------
production['磁铁'] = [[40], ['铁矿', 1]]
production['磁线圈'] = [[120], ['磁铁', 1], ['铜块', 0.5]]
production['晶格硅'] = [[30], ['高纯硅块', 1]]
production['钛合金'] = [[20], ['钛块', 1], ['钢材', 1], ['硫酸', 2]]
production['玻璃'] = [[30], ['石矿', 2]]
production['金刚石'] = [[30], ['高能石墨', 1]]
production['氢'] = [[15]]
production['有机晶体'] = [[10], ['塑料', 2], ['精炼油', 1], ['水', 1]]
production['石墨烯2'] = [[60], ['可燃冰', 1], ['氢', -0.5]]
production['液氢燃料棒'] = [[20], ['钛块', 1], ['氢', 5]]
production['氘核燃料棒'] = [[10], ['钛合金', 1], ['重氢', 10], ['超级磁场环', 1]]
production['反物质燃料棒'] = [[5], ['反物质', 10], ['氢', 10], ['湮灭约束球', 1], ['钛合金', 1]]
# ---------------------------------------------
production['钢材'] = [[20], ['铁块', 3]]
production['电动机'] = [[30], ['铁块', 2], ['齿轮', 1], ['磁线圈', 1]]
production['钛化玻璃'] = [[24], ['玻璃', 1], ['钛块', 1], ['水', 1]]
production['棱镜'] = [[60], ['玻璃', 1.5]]
production['钛晶石'] = [[15], ['有机晶体', 1], ['钛块', 3]]
production['推进器'] = [[15], ['钢材', 2], ['铜块', 3]]
production['加力推进器'] = [[10], ['钛合金', 5], ['电磁涡轮', 5]]
production['奇异物质'] = [[7.5], ['粒子容器', 2], ['铁块', 2], ['重氢', 10]]
# ---------------------------------------------
production['齿轮'] = [[60], ['铁块', 1]]
production['电磁涡轮'] = [[30], ['电动机', 2], ['磁线圈', 2]]
production['电路板'] = [[120], ['铁块', 1], ['铜块', 0.5]]
production['引力透镜'] = [[10], ['金刚石', 4], ['奇异物质', 1]]
production['硫酸'] = [[40], ['精炼油', 1.5], ['石矿', 2], ['水', 1]]
production['重氢'] = [[60], ['氢', 2]]
production['位面过滤器'] = [[5], ['卡西米尔晶体', 1], ['钛化玻璃', 2]]
production['碳纳米管'] = [[30], ['石墨烯', 1.5], ['钛块', 0.5]]
production['物流运输机'] = [[15], ['铁块', 5], ['处理器', 2], ['推进器', 2]]
production['星际物流运输船'] = [[10], ['钛合金', 10], ['处理器', 10], ['加力推进器', 2]]
production['物流运输机'] = [[15], ['铁块', 5], ['处理器', 2], ['推进器', 2]]
production['小型运载火箭'] = [[10], ['戴森球组件', 2], ['氘核燃料棒', 2], ['量子芯片', 2]]
# ---------------------------------------------
production['电浆激发器'] = [[30], ['磁线圈', 4], ['棱镜', 2]]
production['超级磁场环'] = [[20], ['电磁涡轮', 2], ['磁铁', 3], ['高能石墨', 1]]
production['粒子宽带'] = [[7.5], ['碳纳米管', 2], ['晶格硅', 2], ['塑料', 1]]
production['处理器'] = [[20], ['电路板', 2], ['微晶原件', 2]]
production['卡西米尔晶体'] = [[15], ['钛晶石', 1], ['石墨烯', 2], ['氢', 12]]
production['粒子容器'] = [[15], ['电磁涡轮', 2], ['铜块', 2], ['石墨烯', 2]]
production['空间翘曲器'] = [[6], ['引力透镜', 1]]
production['太阳帆'] = [[30], ['石墨烯', 0.5], ['光子合并器', 0.5]]
production['框架材料'] = [[10], ['碳纳米管', 4], ['钛合金', 1], ['高纯硅块', 1]]
production['戴森球组件'] = [[7.5], ['框架材料', 3], ['太阳帆', 3], ['处理器', 3]]
# ---------------------------------------------
production['光子合并器'] = [[20], ['棱镜', 2], ['电路板', 1]]
production['微晶原件'] = [[30], ['高纯硅块', 2], ['铜块', 1]]
production['量子芯片'] = [[10], ['处理器', 2], ['位面过滤器', 2]]
production['反物质'] = [[60], ['临界光子', 1], ['氢', -1]]
production['湮灭约束球'] = [[3], ['粒子容器', 1], ['处理器', 1]]
# ---------------------------------------------
production['电磁矩阵'] = [[20], ['磁线圈', 1], ['电路板', 1]]
production['能量矩阵'] = [[10], ['高能石墨', 2], ['氢', 2]]
production['结构矩阵'] = [[7.5], ['金刚石', 1], ['钛晶石', 1]]
production['信息矩阵'] = [[6], ['处理器', 2], ['粒子宽带', 1]]
production['引力矩阵'] = [[5], ['引力透镜', 0.5], ['量子芯片', 0.5]]
production['宇宙矩阵'] = [[4], ['电磁矩阵', 1], ['能量矩阵', 1], ['结构矩阵', 1], ['信息矩阵', 1], ['引力矩阵', 1], ['反物质', 1]]
production['地基'] = [[60], ['石材', 3], ['钢材', 1]]
# ---------------------------------------------
production['传送带'] = [[180], ['铁块', 2/3], ['齿轮', 1/3]]
production['高速传送带'] = [[180], ['传送带', 1], ['电磁涡轮', 1/3]]
production['极速传送带'] = [[180], ['高速传送带', 1], ['超级磁场环', 1/3], ['石墨烯', 1/3]]
production['分拣器'] = [[60], ['铁块', 1], ['电路板', 1]]
production['高速分拣器'] = [[120], ['分拣器', 1], ['电动机', 0.5]]
production['极速分拣器'] = [[120], ['高速分拣器', 1], ['电磁涡轮', 0.5]]
production['制造台 Mk.I'] = [[30], ['铁块', 4], ['齿轮', 8], ['电路板', 4]]
production['制造台 Mk.II'] = [[20], ['制造台 Mk.I', 1], ['石墨烯', 8], ['处理器', 4]]
production['制造台 Mk.III'] = [[15], ['制造台 Mk.II', 1], ['粒子宽带', 8], ['量子芯片', 2]]
production['电弧熔炉'] = [[20], ['铁块', 4], ['石材', 2], ['电路板', 4], ['磁线圈', 2]]

# Special Supporters
# The element in this list should be produced directly.
# The element in this list should not be an ingredient in "production" list,
# Format: [resource: str, second_production_amount: float, can_be_negative: bool]
support = dict()
support['可燃冰'] = [['氢', 0.5, True], ['石墨烯', 1, False]]

# Special raw material (two second_production)
# The element in this list should be produced directly.
# The element in this list should not be an ingredient in "production" list,
# Format: [resource: str, second_production_amount: float]
bi_material = dict()
bi_material['原油'] = [['氢', 0.5], ['精炼油', 1]]


# def check_eq_production_element():
#     # Check if every element is in the production dictionary.
#     for row in element:
#         for elem in row:
#             if elem != '':
#                 assert(production[elem])
#     # Validate the existence of the all elements in the production.
#     for _, v in production.items():
#         for elem in v[1:]:
#             assert(production[elem[0]])
#
#
# check_eq_production_element()
#
#
# def sort_element():
#     import networkx as nx
#     relations = []
#     for k, v in production.items():
#         if len(v) > 1:
#             for elem in v[1:]:
#                 relations.append((k, elem[0], elem[1]))
#     graph = nx.DiGraph()
#     graph.add_weighted_edges_from(relations)
#     # sort element
#     raw_element = [x for a in element for x in a if x != '']
#
#     def my_cmp(a, b):
#         a_list = list(nx.dfs_postorder_nodes(graph, source=a))
#         if b in a_list:
#             return -1
#         else:
#             return 1
#
#     ret = []
#     while raw_element:
#         foo = raw_element.pop()
#         for i in range(len(ret)):
#             if my_cmp(foo, ret[i]) == -1:
#                 ret.insert(i, foo)
#                 foo = None
#                 break
#         if foo is not None:
#             ret.append(foo)
#     return ret
#
#
# sorted_element = sort_element()
# print(sorted_element)

# Hard coded.
sorted_element = ['电弧熔炉', '制造台 Mk.III', '制造台 Mk.II', '制造台 Mk.I', '极速分拣器', '高速分拣器', '分拣器',
                  '极速传送带', '高速传送带', '传送带', '地基', '宇宙矩阵', '引力矩阵', '信息矩阵', '结构矩阵', '能量矩阵', '电磁矩阵',
                  '反物质燃料棒', '湮灭约束球', '反物质', '小型运载火箭', '量子芯片', '戴森球组件', '星际物流运输船', '物流运输机',
                  '处理器', '微晶原件', '太阳帆', '光子合并器', '框架材料', '空间翘曲器', '引力透镜', '奇异物质', '粒子容器', '位面过滤器',
                  '卡西米尔晶体', '粒子宽带', '氘核燃料棒', '超级磁场环', '电浆激发器', '碳纳米管', '重氢', '加力推进器', '钛合金', '石墨烯',
                  '硫酸', '电路板', '电磁涡轮', '电动机', '齿轮', '推进器', '钛晶石', '棱镜', '钛化玻璃', '钢材', '液氢燃料棒',
                  '有机晶体', '塑料', '精炼油', '氢', '金刚石', '玻璃', '晶格硅', '磁线圈', '磁铁', '高能石墨', '石材', '钛块', '高纯硅块',
                  '铜块', '铁块', '临界光子', '水', '原油', '煤矿', '石矿', '钛矿', '硅矿', '铜矿', '铁矿', '可燃冰']


