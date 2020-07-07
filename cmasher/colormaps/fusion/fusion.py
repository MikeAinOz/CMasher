__author__ = "Ellert van der Velden (@1313e)"

from matplotlib.colors import ListedColormap

cm_type = "diverging"

cm_data = [[0.15269566, 0.01594210, 0.06988881],
           [0.15825218, 0.01698613, 0.07448610],
           [0.16381559, 0.01801391, 0.07904903],
           [0.16938824, 0.01902024, 0.08357670],
           [0.17497227, 0.02000000, 0.08806795],
           [0.18056933, 0.02094854, 0.09252115],
           [0.18618125, 0.02186079, 0.09693475],
           [0.19180964, 0.02273184, 0.10130694],
           [0.19745571, 0.02355734, 0.10563546],
           [0.20312086, 0.02433247, 0.10991812],
           [0.20880647, 0.02505241, 0.11415254],
           [0.21451331, 0.02571326, 0.11833582],
           [0.22024232, 0.02631087, 0.12246503],
           [0.22599426, 0.02684139, 0.12653697],
           [0.23176973, 0.02730126, 0.13054822],
           [0.23756918, 0.02768731, 0.13449511],
           [0.24339322, 0.02799614, 0.13837386],
           [0.24924171, 0.02822590, 0.14218023],
           [0.25511451, 0.02837495, 0.14590987],
           [0.26101189, 0.02844103, 0.14955835],
           [0.26693291, 0.02842451, 0.15312083],
           [0.27287751, 0.02832433, 0.15659247],
           [0.27884443, 0.02814220, 0.15996819],
           [0.28483274, 0.02787955, 0.16324286],
           [0.29084134, 0.02753849, 0.16641124],
           [0.29686854, 0.02712298, 0.16946810],
           [0.30291252, 0.02663769, 0.17240825],
           [0.30897122, 0.02608836, 0.17522660],
           [0.31504239, 0.02548174, 0.17791823],
           [0.32112348, 0.02482582, 0.18047848],
           [0.32721154, 0.02413013, 0.18290307],
           [0.33330350, 0.02340514, 0.18518817],
           [0.33939638, 0.02266162, 0.18733027],
           [0.34548643, 0.02191286, 0.18932678],
           [0.35157038, 0.02117156, 0.19117542],
           [0.35764438, 0.02045243, 0.19287499],
           [0.36370491, 0.01976980, 0.19442473],
           [0.36974824, 0.01913910, 0.19582493],
           [0.37577077, 0.01857585, 0.19707658],
           [0.38176904, 0.01809548, 0.19818146],
           [0.38773974, 0.01771347, 0.19914209],
           [0.39367973, 0.01744507, 0.19996177],
           [0.39958615, 0.01730503, 0.20064439],
           [0.40545640, 0.01730756, 0.20119435],
           [0.41128814, 0.01746625, 0.20161659],
           [0.41707934, 0.01779395, 0.20191636],
           [0.42282828, 0.01830274, 0.20209920],
           [0.42853351, 0.01900391, 0.20217081],
           [0.43419385, 0.01990800, 0.20213703],
           [0.43980839, 0.02102481, 0.20200373],
           [0.44537650, 0.02236329, 0.20177660],
           [0.45089772, 0.02393184, 0.20146133],
           [0.45637175, 0.02573832, 0.20106358],
           [0.46179860, 0.02778978, 0.20058845],
           [0.46717826, 0.03009310, 0.20004129],
           [0.47251097, 0.03265447, 0.19942678],
           [0.47779699, 0.03547995, 0.19874971],
           [0.48303675, 0.03857509, 0.19801427],
           [0.48823063, 0.04190477, 0.19722484],
           [0.49337920, 0.04533361, 0.19638501],
           [0.49848295, 0.04885560, 0.19549855],
           [0.50354245, 0.05246016, 0.19456891],
           [0.50855829, 0.05613794, 0.19359908],
           [0.51353106, 0.05988082, 0.19259203],
           [0.51846134, 0.06368175, 0.19155052],
           [0.52334968, 0.06753461, 0.19047725],
           [0.52819668, 0.07143406, 0.18937444],
           [0.53300287, 0.07537552, 0.18824429],
           [0.53776881, 0.07935505, 0.18708888],
           [0.54249498, 0.08336925, 0.18591011],
           [0.54718187, 0.08741520, 0.18470977],
           [0.55182995, 0.09149040, 0.18348952],
           [0.55643964, 0.09559271, 0.18225093],
           [0.56101135, 0.09972030, 0.18099554],
           [0.56554545, 0.10387162, 0.17972470],
           [0.57004228, 0.10804535, 0.17843965],
           [0.57450218, 0.11224039, 0.17714162],
           [0.57892543, 0.11645581, 0.17583175],
           [0.58331227, 0.12069081, 0.17451137],
           [0.58766296, 0.12494477, 0.17318140],
           [0.59197769, 0.12921716, 0.17184282],
           [0.59625664, 0.13350755, 0.17049678],
           [0.60049995, 0.13781560, 0.16914425],
           [0.60470775, 0.14214109, 0.16778605],
           [0.60888014, 0.14648377, 0.16642339],
           [0.61301718, 0.15084356, 0.16505701],
           [0.61711892, 0.15522035, 0.16368797],
           [0.62118537, 0.15961411, 0.16231725],
           [0.62521654, 0.16402486, 0.16094574],
           [0.62921239, 0.16845259, 0.15957459],
           [0.63317286, 0.17289743, 0.15820467],
           [0.63709789, 0.17735940, 0.15683719],
           [0.64098737, 0.18183867, 0.15547315],
           [0.64484118, 0.18633534, 0.15411376],
           [0.64865919, 0.19084955, 0.15276021],
           [0.65244121, 0.19538149, 0.15141373],
           [0.65618709, 0.19993128, 0.15007576],
           [0.65989658, 0.20449916, 0.14874755],
           [0.66356950, 0.20908526, 0.14743075],
           [0.66720557, 0.21368981, 0.14612684],
           [0.67080453, 0.21831301, 0.14483750],
           [0.67436611, 0.22295502, 0.14356461],
           [0.67788999, 0.22761609, 0.14230996],
           [0.68137585, 0.23229639, 0.14107563],
           [0.68482337, 0.23699614, 0.13986380],
           [0.68823217, 0.24171554, 0.13867669],
           [0.69160188, 0.24645478, 0.13751682],
           [0.69493213, 0.25121406, 0.13638677],
           [0.69822249, 0.25599358, 0.13528928],
           [0.70147255, 0.26079351, 0.13422734],
           [0.70468187, 0.26561404, 0.13320407],
           [0.70785001, 0.27045535, 0.13222275],
           [0.71097649, 0.27531759, 0.13128691],
           [0.71406086, 0.28020092, 0.13040026],
           [0.71710262, 0.28510549, 0.12956671],
           [0.72010127, 0.29003143, 0.12879035],
           [0.72305631, 0.29497887, 0.12807554],
           [0.72596723, 0.29994790, 0.12742676],
           [0.72883351, 0.30493864, 0.12684874],
           [0.73165462, 0.30995115, 0.12634639],
           [0.73443003, 0.31498551, 0.12592479],
           [0.73715922, 0.32004174, 0.12558920],
           [0.73984165, 0.32511988, 0.12534501],
           [0.74247679, 0.33021994, 0.12519777],
           [0.74506413, 0.33534188, 0.12515309],
           [0.74760315, 0.34048567, 0.12521671],
           [0.75009333, 0.34565125, 0.12539436],
           [0.75253419, 0.35083851, 0.12569182],
           [0.75492525, 0.35604733, 0.12611484],
           [0.75726603, 0.36127756, 0.12666908],
           [0.75955612, 0.36652901, 0.12736013],
           [0.76179510, 0.37180145, 0.12819340],
           [0.76398258, 0.37709464, 0.12917414],
           [0.76611821, 0.38240828, 0.13030734],
           [0.76820170, 0.38774203, 0.13159774],
           [0.77023277, 0.39309552, 0.13304977],
           [0.77221122, 0.39846833, 0.13466751],
           [0.77413687, 0.40386001, 0.13645469],
           [0.77600962, 0.40927004, 0.13841463],
           [0.77782945, 0.41469787, 0.14055024],
           [0.77959637, 0.42014290, 0.14286400],
           [0.78131049, 0.42560450, 0.14535795],
           [0.78297201, 0.43108193, 0.14803371],
           [0.78458119, 0.43657447, 0.15089242],
           [0.78613838, 0.44208132, 0.15393484],
           [0.78764406, 0.44760163, 0.15716125],
           [0.78909879, 0.45313449, 0.16057155],
           [0.79050321, 0.45867899, 0.16416524],
           [0.79185809, 0.46423414, 0.16794145],
           [0.79316437, 0.46979884, 0.17189894],
           [0.79442299, 0.47537209, 0.17603613],
           [0.79563505, 0.48095278, 0.18035117],
           [0.79680179, 0.48653975, 0.18484187],
           [0.79792464, 0.49213177, 0.18950575],
           [0.79900496, 0.49772771, 0.19434016],
           [0.80004432, 0.50332634, 0.19934218],
           [0.80104441, 0.50892642, 0.20450869],
           [0.80200701, 0.51452672, 0.20983640],
           [0.80293413, 0.52012589, 0.21532172],
           [0.80382766, 0.52572276, 0.22096109],
           [0.80468967, 0.53131609, 0.22675077],
           [0.80552232, 0.53690464, 0.23268687],
           [0.80632783, 0.54248721, 0.23876543],
           [0.80710851, 0.54806261, 0.24498237],
           [0.80786670, 0.55362968, 0.25133358],
           [0.80860481, 0.55918732, 0.25781488],
           [0.80932526, 0.56473444, 0.26442207],
           [0.81003050, 0.57027003, 0.27115092],
           [0.81072299, 0.57579311, 0.27799721],
           [0.81140518, 0.58130277, 0.28495673],
           [0.81207972, 0.58679806, 0.29202509],
           [0.81274908, 0.59227815, 0.29919806],
           [0.81341552, 0.59774241, 0.30647173],
           [0.81408137, 0.60319018, 0.31384208],
           [0.81474926, 0.60862071, 0.32130478],
           [0.81542167, 0.61403338, 0.32885569],
           [0.81610036, 0.61942795, 0.33649157],
           [0.81678817, 0.62480368, 0.34420784],
           [0.81748695, 0.63016037, 0.35200121],
           [0.81819885, 0.63549767, 0.35986798],
           [0.81892611, 0.64081526, 0.36780440],
           [0.81967060, 0.64611297, 0.37580716],
           [0.82043411, 0.65139072, 0.38387313],
           [0.82121909, 0.65664815, 0.39199823],
           [0.82202656, 0.66188554, 0.40018042],
           [0.82285870, 0.66710267, 0.40841599],
           [0.82371744, 0.67229949, 0.41670163],
           [0.82460384, 0.67747627, 0.42503525],
           [0.82551949, 0.68263309, 0.43341401],
           [0.82646594, 0.68777007, 0.44183516],
           [0.82744484, 0.69288728, 0.45029574],
           [0.82845747, 0.69798494, 0.45879337],
           [0.82950490, 0.70306338, 0.46732598],
           [0.83058837, 0.70812283, 0.47589127],
           [0.83170905, 0.71316357, 0.48448704],
           [0.83286801, 0.71818592, 0.49311119],
           [0.83406629, 0.72319019, 0.50176173],
           [0.83530503, 0.72817668, 0.51043647],
           [0.83658533, 0.73314569, 0.51913321],
           [0.83790779, 0.73809768, 0.52785070],
           [0.83927317, 0.74303306, 0.53658732],
           [0.84068221, 0.74795225, 0.54534156],
           [0.84213588, 0.75285557, 0.55411142],
           [0.84363540, 0.75774329, 0.56289444],
           [0.84518059, 0.76261608, 0.57169073],
           [0.84677218, 0.76747433, 0.58049871],
           [0.84841181, 0.77231818, 0.58931505],
           [0.85009872, 0.77714844, 0.59814098],
           [0.85183442, 0.78196527, 0.60697334],
           [0.85361898, 0.78676924, 0.61581180],
           [0.85545300, 0.79156074, 0.62465496],
           [0.85733708, 0.79634019, 0.63350137],
           [0.85927157, 0.80110804, 0.64235012],
           [0.86125682, 0.80586474, 0.65120031],
           [0.86329372, 0.81061062, 0.66004984],
           [0.86538175, 0.81534633, 0.66889970],
           [0.86752270, 0.82007195, 0.67774580],
           [0.86971583, 0.82478816, 0.68658960],
           [0.87196152, 0.82949538, 0.69543018],
           [0.87426133, 0.83419375, 0.70426386],
           [0.87661459, 0.83888389, 0.71309208],
           [0.87902177, 0.84356618, 0.72191377],
           [0.88148352, 0.84824093, 0.73072734],
           [0.88400075, 0.85290842, 0.73953068],
           [0.88657330, 0.85756911, 0.74832427],
           [0.88920173, 0.86222332, 0.75710696],
           [0.89188662, 0.86687134, 0.76587761],
           [0.89462859, 0.87151346, 0.77463504],
           [0.89742844, 0.87614990, 0.78337778],
           [0.90028705, 0.88078089, 0.79210422],
           [0.90320498, 0.88540665, 0.80081379],
           [0.90618322, 0.89002734, 0.80950508],
           [0.90922288, 0.89464305, 0.81817656],
           [0.91232527, 0.89925383, 0.82682655],
           [0.91549189, 0.90385964, 0.83545317],
           [0.91872454, 0.90846037, 0.84405428],
           [0.92202532, 0.91305582, 0.85262744],
           [0.92539674, 0.91764567, 0.86116973],
           [0.92884183, 0.92222945, 0.86967767],
           [0.93236418, 0.92680655, 0.87814698],
           [0.93596810, 0.93137619, 0.88657233],
           [0.93965884, 0.93593743, 0.89494635],
           [0.94344228, 0.94048919, 0.90326058],
           [0.94732508, 0.94503036, 0.91150406],
           [0.95131441, 0.94955998, 0.91966230],
           [0.95541703, 0.95407768, 0.92771676],
           [0.95963758, 0.95858437, 0.93564471],
           [0.96397569, 0.96308327, 0.94342013],
           [0.96842214, 0.96758121, 0.95101597],
           [0.97295466, 0.97208912, 0.95841520],
           [0.97753779, 0.97662151, 0.96561627],
           [0.98212842, 0.98119340, 0.97264191],
           [0.98668707, 0.98581600, 0.97953727],
           [0.99118833, 0.99049355, 0.98636053],
           [0.99562415, 0.99522369, 0.99316724],
           [1.00000000, 1.00000000, 1.00000000],
           [0.99286734, 0.99599371, 0.99614812],
           [0.98570140, 0.99201791, 0.99234019],
           [0.97850515, 0.98807093, 0.98857653],
           [0.97128081, 0.98415141, 0.98485747],
           [0.96403006, 0.98025821, 0.98118332],
           [0.95675420, 0.97639033, 0.97755440],
           [0.94945423, 0.97254691, 0.97397106],
           [0.94213095, 0.96872714, 0.97043361],
           [0.93478417, 0.96493058, 0.96694278],
           [0.92741484, 0.96115639, 0.96349871],
           [0.92002357, 0.95740386, 0.96010167],
           [0.91261066, 0.95367238, 0.95675205],
           [0.90517530, 0.94996172, 0.95345071],
           [0.89771808, 0.94627115, 0.95019787],
           [0.89023961, 0.94259997, 0.94699371],
           [0.88273889, 0.93894800, 0.94383920],
           [0.87521615, 0.93531462, 0.94073469],
           [0.86767223, 0.93169907, 0.93768025],
           [0.86010488, 0.92810149, 0.93467745],
           [0.85251625, 0.92452070, 0.93172572],
           [0.84490442, 0.92095675, 0.92882652],
           [0.83727062, 0.91740873, 0.92597970],
           [0.82961330, 0.91387653, 0.92318658],
           [0.82193388, 0.91035919, 0.92044693],
           [0.81423010, 0.90685681, 0.91776249],
           [0.80650377, 0.90336829, 0.91513282],
           [0.79875363, 0.89989342, 0.91255918],
           [0.79097948, 0.89643167, 0.91004225],
           [0.78318199, 0.89298227, 0.90758225],
           [0.77536055, 0.88954478, 0.90518014],
           [0.76751441, 0.88611881, 0.90283699],
           [0.75964444, 0.88270351, 0.90055296],
           [0.75175053, 0.87929829, 0.89832878],
           [0.74383262, 0.87590255, 0.89616521],
           [0.73589072, 0.87251564, 0.89406298],
           [0.72792492, 0.86913691, 0.89202278],
           [0.71993521, 0.86576571, 0.89004544],
           [0.71192219, 0.86240124, 0.88813142],
           [0.70388623, 0.85904276, 0.88628135],
           [0.69582754, 0.85568955, 0.88449599],
           [0.68774673, 0.85234079, 0.88277592],
           [0.67964457, 0.84899564, 0.88112162],
           [0.67152191, 0.84565322, 0.87953357],
           [0.66337974, 0.84231265, 0.87801219],
           [0.65521921, 0.83897298, 0.87655784],
           [0.64704068, 0.83563346, 0.87517148],
           [0.63884614, 0.83229298, 0.87385299],
           [0.63063758, 0.82895047, 0.87260229],
           [0.62241561, 0.82560511, 0.87142035],
           [0.61418307, 0.82225567, 0.87030656],
           [0.60594176, 0.81890115, 0.86926118],
           [0.59769403, 0.81554044, 0.86828407],
           [0.58944247, 0.81217242, 0.86737501],
           [0.58119025, 0.80879588, 0.86653338],
           [0.57293967, 0.80540980, 0.86575933],
           [0.56469499, 0.80201285, 0.86505150],
           [0.55645949, 0.79860391, 0.86440940],
           [0.54823663, 0.79518185, 0.86383250],
           [0.54003116, 0.79174538, 0.86331922],
           [0.53184747, 0.78829334, 0.86286840],
           [0.52369022, 0.78482455, 0.86247868],
           [0.51556437, 0.78133787, 0.86214854],
           [0.50747510, 0.77783215, 0.86187634],
           [0.49942800, 0.77430627, 0.86166013],
           [0.49142890, 0.77075916, 0.86149781],
           [0.48348378, 0.76718977, 0.86138716],
           [0.47559884, 0.76359711, 0.86132585],
           [0.46778040, 0.75998024, 0.86131146],
           [0.46003500, 0.75633830, 0.86134138],
           [0.45236936, 0.75267044, 0.86141286],
           [0.44479028, 0.74897593, 0.86152307],
           [0.43730459, 0.74525408, 0.86166912],
           [0.42991920, 0.74150429, 0.86184809],
           [0.42264101, 0.73772603, 0.86205698],
           [0.41547682, 0.73391885, 0.86229290],
           [0.40843352, 0.73008237, 0.86255277],
           [0.40151789, 0.72621630, 0.86283355],
           [0.39473655, 0.72232041, 0.86313228],
           [0.38809598, 0.71839456, 0.86344609],
           [0.38160250, 0.71443865, 0.86377213],
           [0.37526225, 0.71045270, 0.86410756],
           [0.36908114, 0.70643673, 0.86444972],
           [0.36306481, 0.70239086, 0.86479601],
           [0.35721866, 0.69831525, 0.86514393],
           [0.35154777, 0.69421011, 0.86549111],
           [0.34605694, 0.69007569, 0.86583531],
           [0.34075062, 0.68591227, 0.86617437],
           [0.33563291, 0.68172019, 0.86650626],
           [0.33070754, 0.67749978, 0.86682914],
           [0.32597787, 0.67325141, 0.86714125],
           [0.32144684, 0.66897547, 0.86744092],
           [0.31711700, 0.66467238, 0.86772661],
           [0.31299046, 0.66034252, 0.86799697],
           [0.30906887, 0.65598631, 0.86825072],
           [0.30535347, 0.65160416, 0.86848667],
           [0.30184500, 0.64719650, 0.86870371],
           [0.29854375, 0.64276372, 0.86890085],
           [0.29544956, 0.63830622, 0.86907725],
           [0.29256178, 0.63382438, 0.86923211],
           [0.28987929, 0.62931858, 0.86936472],
           [0.28740051, 0.62478917, 0.86947441],
           [0.28512341, 0.62023651, 0.86956060],
           [0.28304548, 0.61566092, 0.86962274],
           [0.28116383, 0.61106270, 0.86966040],
           [0.27947513, 0.60644214, 0.86967318],
           [0.27797569, 0.60179951, 0.86966073],
           [0.27666143, 0.59713504, 0.86962272],
           [0.27552793, 0.59244896, 0.86955888],
           [0.27457047, 0.58774146, 0.86946893],
           [0.27378405, 0.58301273, 0.86935267],
           [0.27316343, 0.57826292, 0.86920990],
           [0.27270315, 0.57349216, 0.86904042],
           [0.27239757, 0.56870055, 0.86884409],
           [0.27224091, 0.56388818, 0.86862073],
           [0.27222727, 0.55905510, 0.86837022],
           [0.27235069, 0.55420136, 0.86809242],
           [0.27260513, 0.54932696, 0.86778718],
           [0.27298455, 0.54443190, 0.86745438],
           [0.27348292, 0.53951613, 0.86709387],
           [0.27409422, 0.53457961, 0.86670552],
           [0.27481251, 0.52962225, 0.86628917],
           [0.27563190, 0.52464394, 0.86584466],
           [0.27654662, 0.51964457, 0.86537182],
           [0.27755099, 0.51462399, 0.86487045],
           [0.27863945, 0.50958201, 0.86434035],
           [0.27980659, 0.50451846, 0.86378130],
           [0.28104713, 0.49943311, 0.86319304],
           [0.28235594, 0.49432573, 0.86257530],
           [0.28372807, 0.48919605, 0.86192779],
           [0.28515870, 0.48404380, 0.86125019],
           [0.28664319, 0.47886866, 0.86054215],
           [0.28817706, 0.47367032, 0.85980329],
           [0.28975598, 0.46844842, 0.85903319],
           [0.29137580, 0.46320260, 0.85823140],
           [0.29303250, 0.45793246, 0.85739743],
           [0.29472223, 0.45263759, 0.85653076],
           [0.29644130, 0.44731755, 0.85563081],
           [0.29818615, 0.44197190, 0.85469698],
           [0.29995337, 0.43660014, 0.85372861],
           [0.30173966, 0.43120178, 0.85272499],
           [0.30354187, 0.42577630, 0.85168538],
           [0.30535698, 0.42032315, 0.85060895],
           [0.30718208, 0.41484175, 0.84949487],
           [0.30901435, 0.40933154, 0.84834220],
           [0.31085108, 0.40379189, 0.84714995],
           [0.31268965, 0.39822218, 0.84591709],
           [0.31452753, 0.39262176, 0.84464249],
           [0.31636229, 0.38698995, 0.84332498],
           [0.31819155, 0.38132607, 0.84196330],
           [0.32001300, 0.37562939, 0.84055611],
           [0.32182440, 0.36989919, 0.83910199],
           [0.32362357, 0.36413471, 0.83759945],
           [0.32540842, 0.35833516, 0.83604691],
           [0.32717680, 0.35249976, 0.83444267],
           [0.32892666, 0.34662771, 0.83278494],
           [0.33065594, 0.34071820, 0.83107184],
           [0.33236262, 0.33477038, 0.82930136],
           [0.33404470, 0.32878343, 0.82747138],
           [0.33570018, 0.32275648, 0.82557967],
           [0.33732703, 0.31668868, 0.82362385],
           [0.33892344, 0.31057909, 0.82160147],
           [0.34048732, 0.30442687, 0.81950987],
           [0.34201654, 0.29823123, 0.81734622],
           [0.34350900, 0.29199133, 0.81510757],
           [0.34496286, 0.28570623, 0.81279086],
           [0.34637591, 0.27937515, 0.81039277],
           [0.34774576, 0.27299746, 0.80790978],
           [0.34907049, 0.26657226, 0.80533828],
           [0.35034765, 0.26009898, 0.80267437],
           [0.35157477, 0.25357710, 0.79991393],
           [0.35274974, 0.24700593, 0.79705268],
           [0.35386957, 0.24038540, 0.79408603],
           [0.35493209, 0.23371498, 0.79100920],
           [0.35593417, 0.22699489, 0.78781709],
           [0.35687304, 0.22022524, 0.78450439],
           [0.35774590, 0.21340635, 0.78106545],
           [0.35854927, 0.20653923, 0.77749437],
           [0.35927989, 0.19962502, 0.77378495],
           [0.35993451, 0.19266520, 0.76993060],
           [0.36050928, 0.18566214, 0.76592451],
           [0.36100028, 0.17861881, 0.76175953],
           [0.36140342, 0.17153899, 0.75742820],
           [0.36171435, 0.16442749, 0.75292275],
           [0.36192848, 0.15729037, 0.74823513],
           [0.36204093, 0.15013519, 0.74335708],
           [0.36204673, 0.14297118, 0.73827997],
           [0.36194040, 0.13580989, 0.73299516],
           [0.36171608, 0.12866551, 0.72749406],
           [0.36136795, 0.12155514, 0.72176784],
           [0.36088975, 0.11449965, 0.71580795],
           [0.36027488, 0.10752429, 0.70960628],
           [0.35951665, 0.10065933, 0.70315520],
           [0.35860825, 0.09394083, 0.69644767],
           [0.35754257, 0.08741135, 0.68947827],
           [0.35631270, 0.08112040, 0.68224270],
           [0.35491188, 0.07512464, 0.67473859],
           [0.35333367, 0.06948733, 0.66696587],
           [0.35157216, 0.06427682, 0.65892725],
           [0.34962224, 0.05956371, 0.65062860],
           [0.34747984, 0.05541636, 0.64207929],
           [0.34514220, 0.05189493, 0.63329238],
           [0.34260814, 0.04904439, 0.62428467],
           [0.33987821, 0.04688785, 0.61507656],
           [0.33695485, 0.04542168, 0.60569166],
           [0.33384244, 0.04461402, 0.59615620],
           [0.33054719, 0.04440736, 0.58649826],
           [0.32707699, 0.04472460, 0.57674681],
           [0.32344118, 0.04547712, 0.56693081],
           [0.31965016, 0.04657302, 0.55707817],
           [0.31571506, 0.04792403, 0.54721501],
           [0.31164748, 0.04944885, 0.53736593],
           [0.30745900, 0.05107806, 0.52755208],
           [0.30316106, 0.05275303, 0.51779232],
           [0.29876453, 0.05442732, 0.50810188],
           [0.29427986, 0.05606322, 0.49849429],
           [0.28971686, 0.05763199, 0.48898038],
           [0.28508450, 0.05911251, 0.47956842],
           [0.28039092, 0.06048993, 0.47026435],
           [0.27564340, 0.06175448, 0.46107205],
           [0.27084884, 0.06289865, 0.45199509],
           [0.26601325, 0.06391846, 0.44303518],
           [0.26114211, 0.06481189, 0.43419322],
           [0.25623998, 0.06557967, 0.42546825],
           [0.25131127, 0.06622224, 0.41685990],
           [0.24635989, 0.06674117, 0.40836707],
           [0.24138922, 0.06713884, 0.39998800],
           [0.23640219, 0.06741821, 0.39172046],
           [0.23140135, 0.06758265, 0.38356178],
           [0.22638882, 0.06763578, 0.37550902],
           [0.22136723, 0.06757936, 0.36756094],
           [0.21633793, 0.06741776, 0.35971365],
           [0.21130262, 0.06715380, 0.35196469],
           [0.20626253, 0.06679084, 0.34431091],
           [0.20121936, 0.06633069, 0.33675064],
           [0.19617350, 0.06577759, 0.32927959],
           [0.19112598, 0.06513382, 0.32189534],
           [0.18607797, 0.06440103, 0.31459602],
           [0.18102995, 0.06358187, 0.30737861],
           [0.17598229, 0.06267883, 0.30024012],
           [0.17093544, 0.06169384, 0.29317803],
           [0.16588972, 0.06062873, 0.28618983],
           [0.16084537, 0.05948518, 0.27927302],
           [0.15580287, 0.05826412, 0.27242584],
           [0.15076217, 0.05696715, 0.26564568],
           [0.14572304, 0.05559583, 0.25892982],
           [0.14068532, 0.05415133, 0.25227586],
           [0.13564929, 0.05263380, 0.24568244],
           [0.13061484, 0.05104378, 0.23914760],
           [0.12558094, 0.04938293, 0.23266799],
           [0.12054835, 0.04764989, 0.22624353],
           [0.11551573, 0.04584618, 0.21987072],
           [0.11048325, 0.04397075, 0.21354882],
           [0.10544988, 0.04202398, 0.20727521],
           [0.10041564, 0.03999828, 0.20104928],
           [0.09537889, 0.03791701, 0.19486783]]

cmap = ListedColormap(cm_data, name="fusion")
