from django.db import models

CLUSTER = (
    (0,	"Miscellaneous#824820"),
    (1,	"Miscellaneous#824820"),
    (2,	"Miscellaneous#824820"),
    (3,	"Miscellaneous#824820"),
    (4,	"Microglia#333333"),
    (5,	"Microglia#333333"),
    (6,	"Microglia#333333"),
    (7,	"Microglia#333333"),
    (8,	"Microglia#333333"),
    (9,	"Microglia#333333"),
    (10, "Microglia#333333"),
    (11, "Microglia#333333"),
    (12, "Microglia#333333"),
    (13, "Vascular#4D4D4D"),
    (14, "Vascular#4D4D4D"),
    (15, "Vascular#4D4D4D"),
    (16, "Vascular#4D4D4D"),
    (17, "Vascular#4D4D4D"),
    (18, "Vascular#4D4D4D"),
    (19, "Vascular#4D4D4D"),
    (20, "Vascular#4D4D4D"),
    (21, "Vascular#4D4D4D"),
    (22, "Vascular#4D4D4D"),
    (23, "Vascular#4D4D4D"),
    (24, "Fibroblast#666666"),
    (25, "Fibroblast#666666"),
    (26, "Fibroblast#666666"),
    (27, "Fibroblast#666666"),
    (28, "Fibroblast#666666"),
    (29, "Fibroblast#666666"),
    (30, "Fibroblast#666666"),
    (31, "Fibroblast#666666"),
    (32, "Oligodendrocyte precursor#737373"),
    (33, "Oligodendrocyte precursor#737373"),
    (34, "Oligodendrocyte precursor#737373"),
    (35, "Oligodendrocyte precursor#737373"),
    (36, "Oligodendrocyte precursor#737373"),
    (37, "Committed oligodendrocyte precursor#7F7F7F"),
    (38, "Committed oligodendrocyte precursor#7F7F7F"),
    (39, "Committed oligodendrocyte precursor#7F7F7F"),
    (40, "Oligodendrocyte#999999"),
    (41, "Committed oligodendrocyte precursor#7F7F7F"),
    (42, "Committed oligodendrocyte precursor#7F7F7F"),
    (43, "Committed oligodendrocyte precursor#7F7F7F"),
    (44, "Oligodendrocyte#999999"),
    (45, "Oligodendrocyte#999999"),
    (46, "Oligodendrocyte#999999"),
    (47, "Oligodendrocyte#999999"),
    (48, "Oligodendrocyte#999999"),
    (49, "Oligodendrocyte#999999"),
    (50, "Oligodendrocyte#999999"),
    (51, "Bergmann glia#A6A6A6"),
    (52, "Astrocyte#B3B3B3"),
    (53, "Astrocyte#B3B3B3"),
    (54, "Astrocyte#B3B3B3"),
    (55, "Astrocyte#B3B3B3"),
    (56, "Astrocyte#B3B3B3"),
    (57, "Astrocyte#B3B3B3"),
    (58, "Astrocyte#B3B3B3"),
    (59, "Astrocyte#B3B3B3"),
    (60, "Astrocyte#B3B3B3"),
    (61, "Astrocyte#B3B3B3"),
    (62, "Astrocyte#B3B3B3"),
    (63, "Astrocyte#B3B3B3"),
    (64, "Astrocyte#B3B3B3"),
    (65, "Ependymal#CCCCCC"),
    (66, "Ependymal#CCCCCC"),
    (67, "Ependymal#CCCCCC"),
    (68, "Ependymal#CCCCCC"),
    (69, "Ependymal#CCCCCC"),
    (70, "Ependymal#CCCCCC"),
    (71, "Ependymal#CCCCCC"),
    (72, "Ependymal#CCCCCC"),
    (73, "Ependymal#CCCCCC"),
    (74, "Ependymal#CCCCCC"),
    (75, "Committed oligodendrocyte precursor#7F7F7F"),
    (76, "Choroid plexus#E5E5E5"),
    (77, "Choroid plexus#E5E5E5"),
    (78, "Choroid plexus#E5E5E5"),
    (79, "Choroid plexus#E5E5E5"),
    (80, "Choroid plexus#E5E5E5"),
    (81, "Choroid plexus#E5E5E5"),
    (82, "Choroid plexus#E5E5E5"),
    (83, "Deep-layer near-projecting#D32D1F"),
    (84, "Deep-layer corticothalamic and 6b#D55124"),
    (85, "Deep-layer near-projecting#D32D1F"),
    (86, "Deep-layer near-projecting#D32D1F"),
    (87, "Deep-layer near-projecting#D32D1F"),
    (88, "Deep-layer near-projecting#D32D1F"),
    (89, "Deep-layer near-projecting#D32D1F"),
    (90, "Deep-layer near-projecting#D32D1F"),
    (91, "Deep-layer near-projecting#D32D1F"),
    (92, "Deep-layer near-projecting#D32D1F"),
    (93, "Deep-layer near-projecting#D32D1F"),
    (94, "Deep-layer near-projecting#D32D1F"),
    (95, "Deep-layer near-projecting#D32D1F"),
    (96, "Deep-layer near-projecting#D32D1F"),
    (97, "Deep-layer corticothalamic and 6b#D55124"),
    (98, "Deep-layer corticothalamic and 6b#D55124"),
    (99, "Deep-layer corticothalamic and 6b#D55124"),
    (100, "Deep-layer corticothalamic and 6b#D55124"),
    (101, "Deep-layer corticothalamic and 6b#D55124"),
    (102, "Deep-layer corticothalamic and 6b#D55124"),
    (103, "Deep-layer corticothalamic and 6b#D55124"),
    (104, "Deep-layer corticothalamic and 6b#D55124"),
    (105, "Deep-layer corticothalamic and 6b#D55124"),
    (106, "Deep-layer corticothalamic and 6b#D55124"),
    (107, "Deep-layer corticothalamic and 6b#D55124"),
    (108, "Deep-layer corticothalamic and 6b#D55124"),
    (109, "Deep-layer corticothalamic and 6b#D55124"),
    (110, "Deep-layer corticothalamic and 6b#D55124"),
    (111, "Deep-layer corticothalamic and 6b#D55124"),
    (112, "Deep-layer corticothalamic and 6b#D55124"),
    (113, "Miscellaneous#824820"),
    (114, "Miscellaneous#824820"),
    (115, "Hippocampal CA1-3#DA8C32"),
    (116, "Miscellaneous#824820"),
    (117, "Miscellaneous#824820"),
    (118, "Miscellaneous#824820"),
    (119, "Hippocampal CA1-3#DA8C32"),
    (120, "Upper-layer intratelencephalic#E2CE45"),
    (121, "Upper-layer intratelencephalic#E2CE45"),
    (122, "Upper-layer intratelencephalic#E2CE45"),
    (123, "Upper-layer intratelencephalic#E2CE45"),
    (124, "Upper-layer intratelencephalic#E2CE45"),
    (125, "Upper-layer intratelencephalic#E2CE45"),
    (126, "Upper-layer intratelencephalic#E2CE45"),
    (127, "Upper-layer intratelencephalic#E2CE45"),
    (128, "Upper-layer intratelencephalic#E2CE45"),
    (129, "Upper-layer intratelencephalic#E2CE45"),
    (130, "Upper-layer intratelencephalic#E2CE45"),
    (131, "Upper-layer intratelencephalic#E2CE45"),
    (132, "Miscellaneous#824820"),
    (133, "Upper-layer intratelencephalic#E2CE45"),
    (134, "Upper-layer intratelencephalic#E2CE45"),
    (135, "Upper-layer intratelencephalic#E2CE45"),
    (136, "Deep-layer intratelencephalic#C1E248"),
    (137, "Deep-layer intratelencephalic#C1E248"),
    (138, "Upper-layer intratelencephalic#E2CE45"),
    (139, "Deep-layer intratelencephalic#C1E248"),
    (140, "Deep-layer intratelencephalic#C1E248"),
    (141, "Deep-layer intratelencephalic#C1E248"),
    (142, "Deep-layer intratelencephalic#C1E248"),
    (143, "Deep-layer intratelencephalic#C1E248"),
    (144, "Deep-layer intratelencephalic#C1E248"),
    (145, "Deep-layer intratelencephalic#C1E248"),
    (146, "Deep-layer intratelencephalic#C1E248"),
    (147, "Deep-layer intratelencephalic#C1E248"),
    (148, "Deep-layer intratelencephalic#C1E248"),
    (149, "Deep-layer intratelencephalic#C1E248"),
    (150, "Deep-layer intratelencephalic#C1E248"),
    (151, "Deep-layer intratelencephalic#C1E248"),
    (152, "Deep-layer intratelencephalic#C1E248"),
    (153, "Amygdala excitatory#91E245"),
    (154, "Amygdala excitatory#91E245"),
    (155, "Amygdala excitatory#91E245"),
    (156, "Amygdala excitatory#91E245"),
    (157, "Amygdala excitatory#91E245"),
    (158, "Amygdala excitatory#91E245"),
    (159, "Amygdala excitatory#91E245"),
    (160, "Amygdala excitatory#91E245"),
    (161, "Amygdala excitatory#91E245"),
    (162, "Amygdala excitatory#91E245"),
    (163, "Hippocampal CA1-3#DA8C32"),
    (164, "Miscellaneous#824820"),
    (165, "Miscellaneous#824820"),
    (166, "Miscellaneous#824820"),
    (167, "Miscellaneous#824820"),
    (168, "Miscellaneous#824820"),
    (169, "Hippocampal CA1-3#DA8C32"),
    (170, "Miscellaneous#824820"),
    (171, "Amygdala excitatory#91E245"),
    (172, "Amygdala excitatory#91E245"),
    (173, "Amygdala excitatory#91E245"),
    (174, "Amygdala excitatory#91E245"),
    (175, "Amygdala excitatory#91E245"),
    (176, "Miscellaneous#824820"),
    (177, "Miscellaneous#824820"),
    (178, "Miscellaneous#824820"),
    (179, "Hippocampal CA1-3#DA8C32"),
    (180, "Hippocampal CA1-3#DA8C32"),
    (181, "Hippocampal CA1-3#DA8C32"),
    (182, "Hippocampal CA1-3#DA8C32"),
    (183, "Hippocampal CA1-3#DA8C32"),
    (184, "Hippocampal CA1-3#DA8C32"),
    (185, "Hippocampal CA1-3#DA8C32"),
    (186, "Hippocampal CA1-3#DA8C32"),
    (187, "Hippocampal CA1-3#DA8C32"),
    (188, "Hippocampal CA1-3#DA8C32"),
    (189, "Hippocampal CA1-3#DA8C32"),
    (190, "Hippocampal CA4#70E044"),
    (191, "Hippocampal CA4#70E044"),
    (192, "Hippocampal CA4#70E044"),
    (193, "Hippocampal CA4#70E044"),
    (194, "Hippocampal CA4#70E044"),
    (195, "Hippocampal CA4#70E044"),
    (196, "Hippocampal CA4#70E044"),
    (197, "Hippocampal CA4#70E044"),
    (198, "Hippocampal CA4#70E044"),
    (199, "Hippocampal dentate gyrus#69E048"),
    (200, "Hippocampal dentate gyrus#69E048"),
    (201, "Hippocampal dentate gyrus#69E048"),
    (202, "Hippocampal dentate gyrus#69E048"),
    (203, "Hippocampal dentate gyrus#69E048"),
    (204, "Hippocampal dentate gyrus#69E048"),
    (205, "Hippocampal dentate gyrus#69E048"),
    (206, "Medium spiny neuron#69E06E"),
    (207, "Medium spiny neuron#69E06E"),
    (208, "Medium spiny neuron#69E06E"),
    (209, "Medium spiny neuron#69E06E"),
    (210, "Medium spiny neuron#69E06E"),
    (211, "Medium spiny neuron#69E06E"),
    (212, "Medium spiny neuron#69E06E"),
    (213, "Medium spiny neuron#69E06E"),
    (214, "Medium spiny neuron#69E06E"),
    (215, "Medium spiny neuron#69E06E"),
    (216, "Medium spiny neuron#69E06E"),
    (217, "Medium spiny neuron#69E06E"),
    (218, "Medium spiny neuron#69E06E"),
    (219, "Medium spiny neuron#69E06E"),
    (220, "Medium spiny neuron#69E06E"),
    (221, "Medium spiny neuron#69E06E"),
    (222, "Eccentric medium spiny neuron#68E2A6"),
    (223, "Eccentric medium spiny neuron#68E2A6"),
    (224, "Eccentric medium spiny neuron#68E2A6"),
    (225, "Eccentric medium spiny neuron#68E2A6"),
    (226, "Eccentric medium spiny neuron#68E2A6"),
    (227, "Eccentric medium spiny neuron#68E2A6"),
    (228, "Eccentric medium spiny neuron#68E2A6"),
    (229, "Eccentric medium spiny neuron#68E2A6"),
    (230, "Eccentric medium spiny neuron#68E2A6"),
    (231, "Eccentric medium spiny neuron#68E2A6"),
    (232, "Eccentric medium spiny neuron#68E2A6"),
    (233, "Eccentric medium spiny neuron#68E2A6"),
    (234, "Eccentric medium spiny neuron#68E2A6"),
    (235, "Splatter#68E2E3"),
    (236, "MGE interneuron#459FE0"),
    (237, "Splatter#68E2E3"),
    (238, "Splatter#68E2E3"),
    (239, "MGE interneuron#459FE0"),
    (240, "MGE interneuron#459FE0"),
    (241, "MGE interneuron#459FE0"),
    (242, "MGE interneuron#459FE0"),
    (243, "MGE interneuron#459FE0"),
    (244, "MGE interneuron#459FE0"),
    (245, "MGE interneuron#459FE0"),
    (246, "MGE interneuron#459FE0"),
    (247, "MGE interneuron#459FE0"),
    (248, "MGE interneuron#459FE0"),
    (249, "MGE interneuron#459FE0"),
    (250, "MGE interneuron#459FE0"),
    (251, "MGE interneuron#459FE0"),
    (252, "MGE interneuron#459FE0"),
    (253, "MGE interneuron#459FE0"),
    (254, "MGE interneuron#459FE0"),
    (255, "MGE interneuron#459FE0"),
    (256, "MGE interneuron#459FE0"),
    (257, "MGE interneuron#459FE0"),
    (258, "MGE interneuron#459FE0"),
    (259, "MGE interneuron#459FE0"),
    (260, "MGE interneuron#459FE0"),
    (261, "MGE interneuron#459FE0"),
    (262, "MGE interneuron#459FE0"),
    (263, "MGE interneuron#459FE0"),
    (264, "LAMP5-LHX6 and Chandelier#205EDE"),
    (265, "LAMP5-LHX6 and Chandelier#205EDE"),
    (266, "LAMP5-LHX6 and Chandelier#205EDE"),
    (267, "LAMP5-LHX6 and Chandelier#205EDE"),
    (268, "LAMP5-LHX6 and Chandelier#205EDE"),
    (269, "LAMP5-LHX6 and Chandelier#205EDE"),
    (270, "LAMP5-LHX6 and Chandelier#205EDE"),
    (271, "LAMP5-LHX6 and Chandelier#205EDE"),
    (272, "LAMP5-LHX6 and Chandelier#205EDE"),
    (273, "LAMP5-LHX6 and Chandelier#205EDE"),
    (274, "LAMP5-LHX6 and Chandelier#205EDE"),
    (275, "LAMP5-LHX6 and Chandelier#205EDE"),
    (276, "CGE interneuron#0024DD"),
    (277, "CGE interneuron#0024DD"),
    (278, "CGE interneuron#0024DD"),
    (279, "CGE interneuron#0024DD"),
    (280, "CGE interneuron#0024DD"),
    (281, "CGE interneuron#0024DD"),
    (282, "CGE interneuron#0024DD"),
    (283, "CGE interneuron#0024DD"),
    (284, "CGE interneuron#0024DD"),
    (285, "CGE interneuron#0024DD"),
    (286, "CGE interneuron#0024DD"),
    (287, "CGE interneuron#0024DD"),
    (288, "CGE interneuron#0024DD"),
    (289, "CGE interneuron#0024DD"),
    (290, "CGE interneuron#0024DD"),
    (291, "CGE interneuron#0024DD"),
    (292, "CGE interneuron#0024DD"),
    (293, "CGE interneuron#0024DD"),
    (294, "CGE interneuron#0024DD"),
    (295, "CGE interneuron#0024DD"),
    (296, "CGE interneuron#0024DD"),
    (297, "Upper rhombic lip#251CDD"),
    (298, "Cerebellar inhibitory#6822DD"),
    (299, "Cerebellar inhibitory#6822DD"),
    (300, "Cerebellar inhibitory#6822DD"),
    (301, "Cerebellar inhibitory#6822DD"),
    (302, "Cerebellar inhibitory#6822DD"),
    (303, "Cerebellar inhibitory#6822DD"),
    (304, "Cerebellar inhibitory#6822DD"),
    (305, "Cerebellar inhibitory#6822DD"),
    (306, "Cerebellar inhibitory#6822DD"),
    (307, "Cerebellar inhibitory#6822DD"),
    (308, "Upper rhombic lip#251CDD"),
    (309, "Upper rhombic lip#251CDD"),
    (310, "Upper rhombic lip#251CDD"),
    (311, "Upper rhombic lip#251CDD"),
    (312, "Upper rhombic lip#251CDD"),
    (313, "Splatter#68E2E3"),
    (314, "Miscellaneous#824820"),
    (315, "Lower rhombic lip#A82DDE"),
    (316, "Lower rhombic lip#A82DDE"),
    (317, "Lower rhombic lip#A82DDE"),
    (318, "Lower rhombic lip#A82DDE"),
    (319, "Lower rhombic lip#A82DDE"),
    (320, "Lower rhombic lip#A82DDE"),
    (321, "Lower rhombic lip#A82DDE"),
    (322, "Lower rhombic lip#A82DDE"),
    (323, "Mammillary body#D334C9"),
    (324, "Mammillary body#D334C9"),
    (325, "Mammillary body#D334C9"),
    (326, "Mammillary body#D334C9"),
    (327, "Mammillary body#D334C9"),
    (328, "Mammillary body#D334C9"),
    (329, "Mammillary body#D334C9"),
    (330, "Mammillary body#D334C9"),
    (331, "Mammillary body#D334C9"),
    (332, "Mammillary body#D334C9"),
    (333, "Mammillary body#D334C9"),
    (334, "Splatter#68E2E3"),
    (335, "Splatter#68E2E3"),
    (336, "Splatter#68E2E3"),
    (337, "Splatter#68E2E3"),
    (338, "Splatter#68E2E3"),
    (339, "Splatter#68E2E3"),
    (340, "Splatter#68E2E3"),
    (341, "Splatter#68E2E3"),
    (342, "Splatter#68E2E3"),
    (343, "Splatter#68E2E3"),
    (344, "Splatter#68E2E3"),
    (345, "Splatter#68E2E3"),
    (346, "Splatter#68E2E3"),
    (347, "Splatter#68E2E3"),
    (348, "Splatter#68E2E3"),
    (349, "Splatter#68E2E3"),
    (350, "Splatter#68E2E3"),
    (351, "Splatter#68E2E3"),
    (352, "Splatter#68E2E3"),
    (353, "Splatter#68E2E3"),
    (354, "Splatter#68E2E3"),
    (355, "Splatter#68E2E3"),
    (356, "Splatter#68E2E3"),
    (357, "Splatter#68E2E3"),
    (358, "Splatter#68E2E3"),
    (359, "Splatter#68E2E3"),
    (360, "Splatter#68E2E3"),
    (361, "Splatter#68E2E3"),
    (362, "Splatter#68E2E3"),
    (363, "Splatter#68E2E3"),
    (364, "Splatter#68E2E3"),
    (365, "Splatter#68E2E3"),
    (366, "Splatter#68E2E3"),
    (367, "Splatter#68E2E3"),
    (368, "Splatter#68E2E3"),
    (369, "Splatter#68E2E3"),
    (370, "Splatter#68E2E3"),
    (371, "Splatter#68E2E3"),
    (372, "Thalamic excitatory#D33088"),
    (373, "Splatter#68E2E3"),
    (374, "Splatter#68E2E3"),
    (375, "Splatter#68E2E3"),
    (376, "Splatter#68E2E3"),
    (377, "Splatter#68E2E3"),
    (378, "Splatter#68E2E3"),
    (379, "Splatter#68E2E3"),
    (380, "Splatter#68E2E3"),
    (381, "Splatter#68E2E3"),
    (382, "Splatter#68E2E3"),
    (383, "Splatter#68E2E3"),
    (384, "Splatter#68E2E3"),
    (385, "Splatter#68E2E3"),
    (386, "Splatter#68E2E3"),
    (387, "Splatter#68E2E3"),
    (388, "Splatter#68E2E3"),
    (389, "Splatter#68E2E3"),
    (390, "Splatter#68E2E3"),
    (391, "Splatter#68E2E3"),
    (392, "Splatter#68E2E3"),
    (393, "Splatter#68E2E3"),
    (394, "Splatter#68E2E3"),
    (395, "Splatter#68E2E3"),
    (396, "Splatter#68E2E3"),
    (397, "Splatter#68E2E3"),
    (398, "Splatter#68E2E3"),
    (399, "Splatter#68E2E3"),
    (400, "Splatter#68E2E3"),
    (401, "Miscellaneous#824820"),
    (402, "Splatter#68E2E3"),
    (403, "Splatter#68E2E3"),
    (404, "Miscellaneous#824820"),
    (405, "Amygdala excitatory#91E245"),
    (406, "Amygdala excitatory#91E245"),
    (407, "Amygdala excitatory#91E245"),
    (408, "Amygdala excitatory#91E245"),
    (409, "Splatter#68E2E3"),
    (410, "Splatter#68E2E3"),
    (411, "Splatter#68E2E3"),
    (412, "Splatter#68E2E3"),
    (413, "Splatter#68E2E3"),
    (414, "Splatter#68E2E3"),
    (415, "Splatter#68E2E3"),
    (416, "Splatter#68E2E3"),
    (417, "Splatter#68E2E3"),
    (418, "Splatter#68E2E3"),
    (419, "Amygdala excitatory#91E245"),
    (420, "Splatter#68E2E3"),
    (421, "Splatter#68E2E3"),
    (422, "Splatter#68E2E3"),
    (423, "Splatter#68E2E3"),
    (424, "Splatter#68E2E3"),
    (425, "Splatter#68E2E3"),
    (426, "Eccentric medium spiny neuron#68E2A6"),
    (427, "Medium spiny neuron#69E06E"),
    (428, "Splatter#68E2E3"),
    (429, "Splatter#68E2E3"),
    (430, "Medium spiny neuron#69E06E"),
    (431, "Splatter#68E2E3"),
    (432, "Splatter#68E2E3"),
    (433, "Midbrain-derived inhibitory#D32D4A"),
    (434, "Midbrain-derived inhibitory#D32D4A"),
    (435, "Midbrain-derived inhibitory#D32D4A"),
    (436, "Midbrain-derived inhibitory#D32D4A"),
    (437, "Midbrain-derived inhibitory#D32D4A"),
    (438, "Midbrain-derived inhibitory#D32D4A"),
    (439, "Midbrain-derived inhibitory#D32D4A"),
    (440, "Midbrain-derived inhibitory#D32D4A"),
    (441, "Midbrain-derived inhibitory#D32D4A"),
    (442, "Midbrain-derived inhibitory#D32D4A"),
    (443, "Midbrain-derived inhibitory#D32D4A"),
    (444, "Midbrain-derived inhibitory#D32D4A"),
    (445, "Thalamic excitatory#D33088"),
    (446, "Thalamic excitatory#D33088"),
    (447, "Thalamic excitatory#D33088"),
    (448, "Thalamic excitatory#D33088"),
    (449, "Thalamic excitatory#D33088"),
    (450, "Thalamic excitatory#D33088"),
    (451, "Thalamic excitatory#D33088"),
    (452, "Thalamic excitatory#D33088"),
    (453, "Thalamic excitatory#D33088"),
    (454, "Thalamic excitatory#D33088"),
    (455, "Thalamic excitatory#D33088"),
    (456, "Thalamic excitatory#D33088"),
    (457, "Thalamic excitatory#D33088"),
    (458, "Thalamic excitatory#D33088"),
    (459, "Thalamic excitatory#D33088"),
    (460, "Thalamic excitatory#D33088")
)


class Cell(models.Model):
    cluster = models.PositiveIntegerField(choices=CLUSTER)
    name = models.CharField(max_length=20, null=True, blank=True)
    gene = models.PositiveIntegerField(null=True, blank=True)
    chr = models.PositiveIntegerField(null=True, blank=True)
    start = models.PositiveIntegerField(null=True, blank=True)
    stop = models.PositiveIntegerField(null=True, blank=True)
    nsnps = models.PositiveIntegerField(null=True, blank=True)
    nparam = models.PositiveIntegerField(null=True, blank=True)
    n = models.IntegerField(null=True, blank=True)
    zstat = models.FloatField(null=True, blank=True)
    scz_2022_p = models.FloatField(null=True, blank=True)
    scz_2018_p = models.FloatField(null=True, blank=True)
    scz_2014_p = models.FloatField(null=True, blank=True)
    scz_2011_p = models.FloatField(null=True, blank=True)
    alcohol_2022_p = models.FloatField(null=True, blank=True)
    ms_2018_p = models.FloatField(null=True, blank=True)
    sleep_2019_p = models.FloatField(null=True, blank=True)
    alz_2022_p = models.FloatField(null=True, blank=True)
    ptsd_2023_p = models.FloatField(null=True, blank=True)
    bmi_2018_p = models.FloatField(null=True, blank=True)
    cig_2022_p = models.FloatField(null=True, blank=True)
    mdd_2023_p = models.FloatField(null=True, blank=True)
    mdd_2019_p = models.FloatField(null=True, blank=True)
    adhd_2019_p = models.FloatField(null=True, blank=True)
    an_2019_p = models.FloatField(null=True, blank=True)
    asd_2017_p = models.FloatField(null=True, blank=True)
    bip_2021_p = models.FloatField(null=True, blank=True)
    educ_2018_p = models.FloatField(null=True, blank=True)
    hgt_2018_p = models.FloatField(null=True, blank=True)
    intel_2018_p = models.FloatField(null=True, blank=True)
    neuro_2018_p = models.FloatField(null=True, blank=True)
    spe_rank = models.FloatField(null=True, blank=True)
    spe_val = models.FloatField(null=True, blank=True)
    gene_exp = models.FloatField(null=True, blank=True)
    scz_2022_p_log = models.FloatField(null=True, blank=True)
    enrichment_score = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.cluster} --- {self.name} --- {self.spe_rank}'


class Phenotype(models.Model):
    SHEET = (
        (1, 'Schizophrenia'),
        (2, 'Alcohol'),
        (3, 'Sleep'),
        (4, 'Multiple Sclerosis'),
        (5, 'Alzheimer Disease'),
    )
    sheet = models.PositiveSmallIntegerField(choices=SHEET)
    cluster = models.PositiveIntegerField(choices=CLUSTER)
    sig1_and_cond2_and_none0 = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    ngenes = models.IntegerField(null=True, blank=True)
    beta = models.FloatField(null=True, blank=True)
    beta_std = models.FloatField(null=True, blank=True)
    se = models.FloatField(null=True, blank=True)
    p = models.FloatField(null=True, blank=True)
    supercluster = models.CharField(max_length=255, null=True, blank=True)
    class_auto_annotation = models.CharField(max_length=255, null=True, blank=True)
    neurotransmitter_auto_annotation = models.CharField(max_length=255, null=True, blank=True)
    neuropeptide_auto_annotation = models.TextField(null=True, blank=True)
    subtype_auto_annotation = models.CharField(max_length=255, null=True, blank=True)
    transferred_mtg_label = models.CharField(max_length=255, null=True, blank=True)
    top_three_regions = models.TextField(null=True, blank=True)
    top_three_dissections = models.TextField(null=True, blank=True)
    top_enriched_genes = models.TextField(null=True, blank=True)
    number_of_cells = models.IntegerField(null=True, blank=True)
    doublet_finder_score = models.FloatField(null=True, blank=True)
    total_umi = models.FloatField(null=True, blank=True)
    fraction_unspliced = models.FloatField(null=True, blank=True)
    fraction_mitochondrial = models.FloatField(null=True, blank=True)
    h19_30_002 = models.IntegerField(null=True, blank=True)
    h19_30_001 = models.IntegerField(null=True, blank=True)
    h18_30_002 = models.IntegerField(null=True, blank=True)
    h18_30_001 = models.IntegerField(null=True, blank=True)
    fraction_cells_from_top_donor = models.FloatField(null=True, blank=True)
    number_of_dissections = models.IntegerField(null=True, blank=True)
    top_dissection_percentage = models.FloatField(null=True, blank=True)
    dissections = models.TextField(null=True, blank=True)
