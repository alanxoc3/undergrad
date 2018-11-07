# Graph - Alan Morgan - Indian - increment hidden
import numpy as np
from matplotlib import pyplot as plt
from math import pi as pi

per1 = [0.41527001862197394, 0.6666666666666666]
t1 = [0, 1]

per2 = [0.3687150837988827, 0.6461824953445066, 0.6871508379888268, 0.6964618249534451, 0.7467411545623837, 0.750465549348231, 0.7392923649906891, 0.7374301675977654, 0.7430167597765364, 0.7411545623836127, 0.7392923649906891, 0.7411545623836127, 0.7392923649906891, 0.7411545623836127, 0.7392923649906891, 0.7411545623836127, 0.7430167597765364, 0.7467411545623837, 0.7486033519553073, 0.7467411545623837, 0.74487895716946, 0.7467411545623837, 0.74487895716946, 0.7430167597765364, 0.74487895716946, 0.7467411545623837, 0.74487895716946, 0.7430167597765364, 0.7411545623836127, 0.7430167597765364, 0.74487895716946, 0.7486033519553073, 0.750465549348231, 0.7523277467411545, 0.7541899441340782, 0.7560521415270018, 0.7541899441340782, 0.7523277467411545, 0.750465549348231, 0.7523277467411545, 0.750465549348231, 0.7523277467411545, 0.7541899441340782, 0.7560521415270018, 0.7579143389199255, 0.7616387337057728, 0.7597765363128491]
t2 = [0, 1, 19, 20, 21, 22, 23, 26, 27, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 50, 53, 55, 56, 57, 58, 59, 62, 65, 68, 69, 70, 74, 77, 79, 81, 84, 86, 87, 92, 94, 95, 97]

per3 = [0.6256983240223464, 0.6666666666666666, 0.6610800744878957, 0.6629422718808193, 0.6685288640595903, 0.6703910614525139, 0.6722532588454376, 0.6703910614525139, 0.6741154562383612, 0.6759776536312849, 0.6815642458100558, 0.6908752327746741, 0.7057728119180633, 0.7281191806331471, 0.74487895716946, 0.7616387337057728, 0.7579143389199255, 0.7597765363128491, 0.7579143389199255, 0.750465549348231, 0.7523277467411545, 0.7541899441340782, 0.7560521415270018, 0.7523277467411545, 0.7541899441340782, 0.7579143389199255, 0.7616387337057728, 0.7597765363128491, 0.7616387337057728, 0.7635009310986964, 0.7597765363128491, 0.7635009310986964, 0.7653631284916201, 0.7635009310986964, 0.7616387337057728, 0.7597765363128491, 0.7579143389199255, 0.7597765363128491, 0.7616387337057728, 0.7635009310986964, 0.7653631284916201, 0.7672253258845437, 0.7690875232774674, 0.7653631284916201, 0.7690875232774674, 0.7672253258845437, 0.7653631284916201, 0.7635009310986964, 0.7597765363128491, 0.7579143389199255, 0.7523277467411545, 0.7541899441340782, 0.7523277467411545]
t3 = [0, 1, 2, 28, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 55, 58, 59, 61, 62, 65, 66, 68, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 88, 90, 91, 96, 97, 98]

per4 = [0.6424581005586593, 0.6461824953445066, 0.6443202979515829, 0.6480446927374302, 0.6536312849162011, 0.664804469273743, 0.6722532588454376, 0.6852886405959032, 0.6890130353817505, 0.6927374301675978, 0.6964618249534451, 0.702048417132216, 0.7057728119180633, 0.7132216014897579, 0.7169459962756052, 0.7188081936685289, 0.7206703910614525, 0.7225325884543762, 0.7206703910614525, 0.7169459962756052, 0.7206703910614525, 0.7225325884543762, 0.7188081936685289, 0.7206703910614525, 0.7243947858472998, 0.7225325884543762, 0.7188081936685289, 0.7206703910614525, 0.7188081936685289, 0.7206703910614525, 0.7188081936685289, 0.7206703910614525, 0.7225325884543762, 0.7243947858472998, 0.7281191806331471, 0.7299813780260708, 0.7318435754189944, 0.7355679702048417, 0.7392923649906891, 0.7411545623836127, 0.74487895716946, 0.7467411545623837, 0.74487895716946, 0.7430167597765364, 0.7411545623836127, 0.7430167597765364, 0.7411545623836127, 0.7430167597765364, 0.74487895716946, 0.7467411545623837]
t4 = [0, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 82, 83, 85, 86, 89, 90, 91, 94, 99]

per5 = [0.4227188081936685, 0.6368715083798883, 0.6461824953445066, 0.6424581005586593, 0.6443202979515829, 0.6461824953445066, 0.6480446927374302, 0.6517690875232774, 0.6554934823091247, 0.659217877094972, 0.6685288640595903, 0.6722532588454376, 0.6741154562383612, 0.6871508379888268, 0.6927374301675978, 0.702048417132216, 0.7150837988826816, 0.7169459962756052, 0.7132216014897579, 0.707635009310987, 0.7113594040968343, 0.7094972067039106, 0.7132216014897579, 0.7150837988826816, 0.7113594040968343, 0.7206703910614525, 0.7150837988826816, 0.7188081936685289, 0.7169459962756052, 0.7206703910614525, 0.7188081936685289, 0.7225325884543762, 0.7206703910614525, 0.7225325884543762, 0.7262569832402235, 0.7299813780260708, 0.7337057728119181, 0.7355679702048417, 0.7374301675977654, 0.7392923649906891, 0.7374301675977654, 0.7355679702048417, 0.7374301675977654, 0.7355679702048417, 0.7337057728119181, 0.7355679702048417, 0.7374301675977654, 0.7392923649906891, 0.7411545623836127, 0.74487895716946, 0.7467411545623837, 0.7486033519553073, 0.7523277467411545]
t5 = [0, 1, 2, 3, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 52, 54, 55, 58, 59, 60, 62, 64, 66, 68, 69, 72, 73, 78, 84, 85, 87, 89, 93, 96, 97]

per6 = [0.41899441340782123, 0.6108007448789572, 0.664804469273743, 0.6703910614525139, 0.6722532588454376, 0.6815642458100558, 0.6890130353817505, 0.6852886405959032, 0.6927374301675978, 0.7039106145251397, 0.7150837988826816, 0.7188081936685289, 0.7225325884543762, 0.7169459962756052, 0.7206703910614525, 0.7262569832402235, 0.7243947858472998, 0.7225325884543762, 0.7188081936685289, 0.7206703910614525, 0.7169459962756052, 0.7150837988826816, 0.7094972067039106, 0.7169459962756052, 0.7150837988826816, 0.7169459962756052, 0.7188081936685289, 0.7169459962756052, 0.7225325884543762, 0.7206703910614525, 0.7188081936685289, 0.7206703910614525, 0.7188081936685289, 0.7206703910614525, 0.7281191806331471, 0.7318435754189944, 0.7299813780260708, 0.7337057728119181, 0.7318435754189944, 0.7337057728119181, 0.7355679702048417, 0.7411545623836127, 0.7467411545623837, 0.7523277467411545, 0.7541899441340782, 0.750465549348231, 0.7523277467411545, 0.7560521415270018, 0.7541899441340782, 0.7560521415270018, 0.7541899441340782, 0.7560521415270018, 0.7579143389199255, 0.7597765363128491, 0.7616387337057728, 0.7635009310986964, 0.7616387337057728, 0.7635009310986964]
t6 = [0, 1, 2, 3, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 55, 56, 62, 67, 70, 72, 75, 76, 77, 78, 79, 80, 82, 83, 85, 88, 91, 92, 93, 95, 96, 97, 99]

per7 = [0.478584729981378, 0.6238361266294227, 0.6424581005586593, 0.6480446927374302, 0.6499068901303539, 0.6517690875232774, 0.659217877094972, 0.6629422718808193, 0.6685288640595903, 0.6703910614525139, 0.6797020484171322, 0.6815642458100558, 0.6834264432029795, 0.6908752327746741, 0.6983240223463687, 0.7001862197392924, 0.707635009310987, 0.7132216014897579, 0.7113594040968343, 0.7132216014897579, 0.7150837988826816, 0.7206703910614525, 0.7225325884543762, 0.7262569832402235, 0.7299813780260708, 0.7318435754189944, 0.7281191806331471, 0.7318435754189944, 0.7337057728119181, 0.7355679702048417, 0.7374301675977654, 0.7392923649906891, 0.7411545623836127, 0.7486033519553073, 0.7467411545623837, 0.7486033519553073, 0.74487895716946, 0.7486033519553073, 0.7523277467411545, 0.750465549348231, 0.7523277467411545, 0.7560521415270018, 0.7579143389199255, 0.7597765363128491, 0.7616387337057728, 0.7653631284916201, 0.7690875232774674, 0.7616387337057728, 0.7635009310986964, 0.7672253258845437, 0.7690875232774674, 0.770949720670391, 0.7728119180633147, 0.7746741154562383, 0.7728119180633147, 0.7746741154562383, 0.776536312849162, 0.7746741154562383]
t7 = [0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50, 52, 55, 56, 59, 62, 65, 66, 69, 70, 71, 72, 73, 77, 84, 89, 94]

per8 = [0.5810055865921788, 0.6219739292364991, 0.6424581005586593, 0.6480446927374302, 0.6536312849162011, 0.6610800744878957, 0.659217877094972, 0.6554934823091247, 0.659217877094972, 0.6610800744878957, 0.6685288640595903, 0.6797020484171322, 0.7001862197392924, 0.7113594040968343, 0.7188081936685289, 0.7206703910614525, 0.7243947858472998, 0.7337057728119181, 0.7392923649906891, 0.7411545623836127, 0.7392923649906891, 0.7411545623836127, 0.7430167597765364, 0.7467411545623837, 0.7486033519553073, 0.7523277467411545, 0.7560521415270018, 0.7541899441340782, 0.7560521415270018, 0.7486033519553073, 0.7541899441340782, 0.7523277467411545, 0.750465549348231, 0.7541899441340782, 0.7579143389199255, 0.7597765363128491, 0.7579143389199255, 0.7560521415270018, 0.7541899441340782, 0.7579143389199255, 0.7597765363128491, 0.7579143389199255, 0.7616387337057728, 0.7635009310986964, 0.7616387337057728, 0.7635009310986964, 0.7653631284916201, 0.7672253258845437, 0.7690875232774674, 0.7672253258845437, 0.7653631284916201, 0.7635009310986964, 0.7653631284916201, 0.7635009310986964, 0.7616387337057728, 0.7635009310986964, 0.7653631284916201, 0.7690875232774674, 0.770949720670391, 0.7728119180633147]
t8 = [0, 1, 2, 3, 4, 5, 7, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 66, 71, 73, 74, 75, 77, 82, 84, 85, 86, 92, 94, 98, 99]

plt.plot(t1, per1, t2, per2, t3, per3, t4, per4, t5, per5, t6, per6, t7, per7, t8, per8)
plt.legend(['1 HN - 61.47', '2 HN - 71.00', '3 HN - 69.70', '4 HN - 77.92', '5 HN - 76.62', '6 HN - 75.76', '7 HN - 77.92', '8 HN - 75.32'])

plt.xlabel('loop iteration')
plt.show()