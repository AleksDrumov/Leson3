Paint_weight_Mb = 400
analog_weight_Mb = 200
Paint_weight_Kb = Paint_weight_Mb * 1024
analog_weight_Kb = analog_weight_Mb * 1024
mb_or_kb = input('1 - мб, 2 - кб')
if mb_or_kb == '1':
    print(Paint_weight_Mb - analog_weight_Mb,'разница мб')
if mb_or_kb == '2':
    print(Paint_weight_Kb - analog_weight_Kb, 'разница кб')