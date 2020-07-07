__author__ = "Ellert van der Velden (@1313e)"

from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.86909722e-04, 2.08352776e-04, 2.82793739e-04],
           [1.02420841e-03, 7.09026614e-04, 1.01020819e-03],
           [2.18032747e-03, 1.44241992e-03, 2.14844683e-03],
           [3.75280218e-03, 2.37790132e-03, 3.68891334e-03],
           [5.74727296e-03, 3.49370967e-03, 5.62841034e-03],
           [8.17359410e-03, 4.77241971e-03, 7.96562586e-03],
           [1.10443181e-02, 6.19914475e-03, 1.06997616e-02],
           [1.43737793e-02, 7.76072600e-03, 1.38297028e-02],
           [1.81776428e-02, 9.44523807e-03, 1.73536418e-02],
           [2.24727681e-02, 1.12416151e-02, 2.12689739e-02],
           [2.72769369e-02, 1.31394915e-02, 2.55720740e-02],
           [3.26086925e-02, 1.51290769e-02, 3.02581889e-02],
           [3.84872063e-02, 1.72010722e-02, 3.53213666e-02],
           [4.47222261e-02, 1.93466133e-02, 4.07486197e-02],
           [5.09500806e-02, 2.15572331e-02, 4.62018871e-02],
           [5.71808510e-02, 2.38248357e-02, 5.15689235e-02],
           [6.34187681e-02, 2.61416786e-02, 5.68507484e-02],
           [6.96672743e-02, 2.85003609e-02, 6.20478243e-02],
           [7.59291578e-02, 3.08938137e-02, 6.71601906e-02],
           [8.22066577e-02, 3.33152931e-02, 7.21875696e-02],
           [8.85015506e-02, 3.57583739e-02, 7.71294513e-02],
           [9.48153158e-02, 3.82168680e-02, 8.19851951e-02],
           [1.01148955e-01, 4.06806343e-02, 8.67539928e-02],
           [1.07503187e-01, 4.30616118e-02, 9.14349804e-02],
           [1.13878547e-01, 4.53633225e-02, 9.60272871e-02],
           [1.20275369e-01, 4.75880815e-02, 1.00530045e-01],
           [1.26693882e-01, 4.97380057e-02, 1.04942421e-01],
           [1.33134099e-01, 5.18151457e-02, 1.09263606e-01],
           [1.39595872e-01, 5.38214735e-02, 1.13492844e-01],
           [1.46079025e-01, 5.57587947e-02, 1.17629459e-01],
           [1.52583333e-01, 5.76287866e-02, 1.21672843e-01],
           [1.59108504e-01, 5.94330341e-02, 1.25622464e-01],
           [1.65654125e-01, 6.11730992e-02, 1.29477863e-01],
           [1.72219811e-01, 6.28503975e-02, 1.33238662e-01],
           [1.78805178e-01, 6.44662366e-02, 1.36904555e-01],
           [1.85409797e-01, 6.60218673e-02, 1.40475307e-01],
           [1.92033210e-01, 6.75184779e-02, 1.43950753e-01],
           [1.98674987e-01, 6.89571516e-02, 1.47330792e-01],
           [2.05334722e-01, 7.03388730e-02, 1.50615372e-01],
           [2.12011971e-01, 7.16645951e-02, 1.53804504e-01],
           [2.18706315e-01, 7.29351829e-02, 1.56898243e-01],
           [2.25417358e-01, 7.41514208e-02, 1.59896686e-01],
           [2.32144723e-01, 7.53140142e-02, 1.62799960e-01],
           [2.38888015e-01, 7.64236378e-02, 1.65608235e-01],
           [2.45646873e-01, 7.74808832e-02, 1.68321706e-01],
           [2.52420969e-01, 7.84862568e-02, 1.70940576e-01],
           [2.59209961e-01, 7.94402342e-02, 1.73465080e-01],
           [2.66013519e-01, 8.03432396e-02, 1.75895468e-01],
           [2.72831343e-01, 8.11956204e-02, 1.78231992e-01],
           [2.79663171e-01, 8.19976376e-02, 1.80474895e-01],
           [2.86508681e-01, 8.27495854e-02, 1.82624460e-01],
           [2.93367596e-01, 8.34516690e-02, 1.84680955e-01],
           [3.00239714e-01, 8.41039642e-02, 1.86644601e-01],
           [3.07124737e-01, 8.47066282e-02, 1.88515678e-01],
           [3.14022396e-01, 8.52597479e-02, 1.90294446e-01],
           [3.20932507e-01, 8.57632664e-02, 1.91981099e-01],
           [3.27854822e-01, 8.62171742e-02, 1.93575865e-01],
           [3.34789052e-01, 8.66214829e-02, 1.95078994e-01],
           [3.41735032e-01, 8.69760059e-02, 1.96490623e-01],
           [3.48692538e-01, 8.72806004e-02, 1.97810918e-01],
           [3.55661249e-01, 8.75352244e-02, 1.99040109e-01],
           [3.62641042e-01, 8.77395301e-02, 2.00178230e-01],
           [3.69631646e-01, 8.78933428e-02, 2.01225420e-01],
           [3.76632720e-01, 8.79965615e-02, 2.02181863e-01],
           [3.83644237e-01, 8.80485905e-02, 2.03047399e-01],
           [3.90665741e-01, 8.80494409e-02, 2.03822267e-01],
           [3.97697030e-01, 8.79987188e-02, 2.04506413e-01],
           [4.04737921e-01, 8.78959614e-02, 2.05099713e-01],
           [4.11787904e-01, 8.77412073e-02, 2.05602373e-01],
           [4.18847045e-01, 8.75335268e-02, 2.06013879e-01],
           [4.25914634e-01, 8.72732532e-02, 2.06334594e-01],
           [4.32990688e-01, 8.69594767e-02, 2.06563938e-01],
           [4.40074552e-01, 8.65924242e-02, 2.06702117e-01],
           [4.47166158e-01, 8.61712769e-02, 2.06748514e-01],
           [4.54264791e-01, 8.56963715e-02, 2.06703307e-01],
           [4.61370423e-01, 8.51667738e-02, 2.06565656e-01],
           [4.68482190e-01, 8.45831301e-02, 2.06335819e-01],
           [4.75600038e-01, 8.39445393e-02, 2.06012803e-01],
           [4.82723160e-01, 8.32515905e-02, 2.05596622e-01],
           [4.89851045e-01, 8.25043389e-02, 2.05086765e-01],
           [4.96983399e-01, 8.17024154e-02, 2.04482254e-01],
           [5.04119272e-01, 8.08468955e-02, 2.03783036e-01],
           [5.11258027e-01, 7.99383002e-02, 2.02988445e-01],
           [5.18399290e-01, 7.89766450e-02, 2.02097209e-01],
           [5.25542018e-01, 7.79635816e-02, 2.01109036e-01],
           [5.32685382e-01, 7.69004851e-02, 2.00023125e-01],
           [5.39828516e-01, 7.57890204e-02, 1.98838551e-01],
           [5.46970487e-01, 7.46312873e-02, 1.97554312e-01],
           [5.54110277e-01, 7.34299038e-02, 1.96169338e-01],
           [5.61246784e-01, 7.21881035e-02, 1.94682482e-01],
           [5.68378803e-01, 7.09098503e-02, 1.93092527e-01],
           [5.75505021e-01, 6.95999704e-02, 1.91398184e-01],
           [5.82624002e-01, 6.82643057e-02, 1.89598093e-01],
           [5.89734175e-01, 6.69098901e-02, 1.87690827e-01],
           [5.96833821e-01, 6.55451489e-02, 1.85674897e-01],
           [6.03921055e-01, 6.41801224e-02, 1.83548753e-01],
           [6.10994030e-01, 6.28259792e-02, 1.81310235e-01],
           [6.18050608e-01, 6.14962511e-02, 1.78957300e-01],
           [6.25088030e-01, 6.02082174e-02, 1.76488904e-01],
           [6.32104256e-01, 5.89785060e-02, 1.73901364e-01],
           [6.39095785e-01, 5.78308182e-02, 1.71194184e-01],
           [6.46060072e-01, 5.67875250e-02, 1.68363271e-01],
           [6.52993262e-01, 5.58778509e-02, 1.65407315e-01],
           [6.59891596e-01, 5.51326945e-02, 1.62323652e-01],
           [6.66750963e-01, 5.45859754e-02, 1.59109421e-01],
           [6.73566797e-01, 5.42745434e-02, 1.55761785e-01],
           [6.80334032e-01, 5.42376114e-02, 1.52277993e-01],
           [6.87047060e-01, 5.45158871e-02, 1.48655458e-01],
           [6.93699685e-01, 5.51504015e-02, 1.44891848e-01],
           [7.00285091e-01, 5.61810769e-02, 1.40985191e-01],
           [7.06796237e-01, 5.76435451e-02, 1.36931763e-01],
           [7.13224652e-01, 5.95721299e-02, 1.32732028e-01],
           [7.19561873e-01, 6.19929392e-02, 1.28383465e-01],
           [7.25798320e-01, 6.49270119e-02, 1.23886727e-01],
           [7.31923874e-01, 6.83875861e-02, 1.19243091e-01],
           [7.37927853e-01, 7.23801500e-02, 1.14455226e-01],
           [7.43799113e-01, 7.69025815e-02, 1.09527932e-01],
           [7.49526309e-01, 8.19453014e-02, 1.04467796e-01],
           [7.55098066e-01, 8.74919188e-02, 9.92851325e-02],
           [7.60503440e-01, 9.35194867e-02, 9.39934527e-02],
           [7.65732337e-01, 9.99992342e-02, 8.86093142e-02],
           [7.70775945e-01, 1.06897139e-01, 8.31539000e-02],
           [7.75627240e-01, 1.14174686e-01, 7.76526208e-02],
           [7.80281368e-01, 1.21789936e-01, 7.21349339e-02],
           [7.84735944e-01, 1.29698609e-01, 6.66347777e-02],
           [7.88991197e-01, 1.37855344e-01, 6.11907481e-02],
           [7.93049873e-01, 1.46215258e-01, 5.58459026e-02],
           [7.96916985e-01, 1.54735273e-01, 5.06483497e-02],
           [8.00599494e-01, 1.63375121e-01, 4.56523351e-02],
           [8.04105780e-01, 1.72098421e-01, 4.09187682e-02],
           [8.07445021e-01, 1.80873537e-01, 3.65633012e-02],
           [8.10627207e-01, 1.89672606e-01, 3.28489690e-02],
           [8.13662020e-01, 1.98473285e-01, 2.97809531e-02],
           [8.16559107e-01, 2.07257026e-01, 2.73542528e-02],
           [8.19327731e-01, 2.16009007e-01, 2.55636781e-02],
           [8.21976558e-01, 2.24717827e-01, 2.44044475e-02],
           [8.24513543e-01, 2.33375040e-01, 2.38728224e-02],
           [8.26945882e-01, 2.41974699e-01, 2.39665842e-02],
           [8.29280004e-01, 2.50512913e-01, 2.46853696e-02],
           [8.31522343e-01, 2.58986251e-01, 2.60316070e-02],
           [8.33677554e-01, 2.67394452e-01, 2.80084987e-02],
           [8.35751192e-01, 2.75735872e-01, 3.06226998e-02],
           [8.37746932e-01, 2.84011762e-01, 3.38817602e-02],
           [8.39668705e-01, 2.92222811e-01, 3.77957713e-02],
           [8.41519999e-01, 3.00370199e-01, 4.23185532e-02],
           [8.43303900e-01, 3.08455467e-01, 4.71817113e-02],
           [8.45023136e-01, 3.16480417e-01, 5.23233390e-02],
           [8.46680124e-01, 3.24447031e-01, 5.76984968e-02],
           [8.48277003e-01, 3.32357393e-01, 6.32708020e-02],
           [8.49815977e-01, 3.40213287e-01, 6.90109556e-02],
           [8.51298995e-01, 3.48016602e-01, 7.48955428e-02],
           [8.52727152e-01, 3.55769991e-01, 8.09062865e-02],
           [8.54102854e-01, 3.63474415e-01, 8.70279872e-02],
           [8.55426529e-01, 3.71132852e-01, 9.32495243e-02],
           [8.56700462e-01, 3.78746074e-01, 9.95610441e-02],
           [8.57925114e-01, 3.86316638e-01, 1.05955702e-01],
           [8.59101674e-01, 3.93846154e-01, 1.12427692e-01],
           [8.60231836e-01, 4.01335605e-01, 1.18971996e-01],
           [8.61316031e-01, 4.08787096e-01, 1.25585441e-01],
           [8.62355266e-01, 4.16202023e-01, 1.32265189e-01],
           [8.63350492e-01, 4.23581725e-01, 1.39009038e-01],
           [8.64302612e-01, 4.30927482e-01, 1.45815298e-01],
           [8.65212486e-01, 4.38240513e-01, 1.52682696e-01],
           [8.66080942e-01, 4.45521979e-01, 1.59610296e-01],
           [8.66908780e-01, 4.52772978e-01, 1.66597437e-01],
           [8.67696781e-01, 4.59994548e-01, 1.73643681e-01],
           [8.68445712e-01, 4.67187666e-01, 1.80748774e-01],
           [8.69156332e-01, 4.74353252e-01, 1.87912610e-01],
           [8.69829395e-01, 4.81492166e-01, 1.95135204e-01],
           [8.70465660e-01, 4.88605210e-01, 2.02416672e-01],
           [8.71065890e-01, 4.95693133e-01, 2.09757209e-01],
           [8.71630860e-01, 5.02756626e-01, 2.17157076e-01],
           [8.72161623e-01, 5.09796140e-01, 2.24616343e-01],
           [8.72658811e-01, 5.16812398e-01, 2.32135528e-01],
           [8.73123168e-01, 5.23806001e-01, 2.39715100e-01],
           [8.73555546e-01, 5.30777442e-01, 2.47355481e-01],
           [8.73957119e-01, 5.37726968e-01, 2.55056838e-01],
           [8.74328606e-01, 5.44655118e-01, 2.62819814e-01],
           [8.74670845e-01, 5.51562321e-01, 2.70644984e-01],
           [8.74985029e-01, 5.58448759e-01, 2.78532635e-01],
           [8.75272170e-01, 5.65314715e-01, 2.86483264e-01],
           [8.75533135e-01, 5.72160553e-01, 2.94497564e-01],
           [8.75769304e-01, 5.78986303e-01, 3.02575772e-01],
           [8.75981711e-01, 5.85792206e-01, 3.10718511e-01],
           [8.76171468e-01, 5.92578442e-01, 3.18926382e-01],
           [8.76340195e-01, 5.99344894e-01, 3.27199529e-01],
           [8.76488878e-01, 6.06091811e-01, 3.35538782e-01],
           [8.76619141e-01, 6.12819077e-01, 3.43944390e-01],
           [8.76732398e-01, 6.19526697e-01, 3.52416865e-01],
           [8.76830159e-01, 6.26214628e-01, 3.60956686e-01],
           [8.76914211e-01, 6.32882684e-01, 3.69564104e-01],
           [8.76986066e-01, 6.39530835e-01, 3.78239722e-01],
           [8.77047786e-01, 6.46158771e-01, 3.86983628e-01],
           [8.77101044e-01, 6.52766396e-01, 3.95796390e-01],
           [8.77148015e-01, 6.59353376e-01, 4.04678112e-01],
           [8.77190693e-01, 6.65919479e-01, 4.13629161e-01],
           [8.77231368e-01, 6.72464347e-01, 4.22649653e-01],
           [8.77272331e-01, 6.78987642e-01, 4.31739780e-01],
           [8.77316047e-01, 6.85488962e-01, 4.40899612e-01],
           [8.77365088e-01, 6.91967879e-01, 4.50129174e-01],
           [8.77422136e-01, 6.98423938e-01, 4.59428441e-01],
           [8.77490045e-01, 7.04856633e-01, 4.68797267e-01],
           [8.77571747e-01, 7.11265449e-01, 4.78235489e-01],
           [8.77670376e-01, 7.17649812e-01, 4.87742774e-01],
           [8.77789136e-01, 7.24009148e-01, 4.97318780e-01],
           [8.77931451e-01, 7.30342820e-01, 5.06962964e-01],
           [8.78100806e-01, 7.36650200e-01, 5.16674769e-01],
           [8.78300918e-01, 7.42930599e-01, 5.26453408e-01],
           [8.78535556e-01, 7.49183340e-01, 5.36298078e-01],
           [8.78808732e-01, 7.55407687e-01, 5.46207706e-01],
           [8.79124486e-01, 7.61602932e-01, 5.56181216e-01],
           [8.79487121e-01, 7.67768301e-01, 5.66217203e-01],
           [8.79900924e-01, 7.73903066e-01, 5.76314291e-01],
           [8.80370474e-01, 7.80006432e-01, 5.86470700e-01],
           [8.80900271e-01, 7.86077671e-01, 5.96684729e-01],
           [8.81495136e-01, 7.92115981e-01, 6.06954181e-01],
           [8.82159739e-01, 7.98120653e-01, 6.17277003e-01],
           [8.82899090e-01, 8.04090903e-01, 6.27650556e-01],
           [8.83717980e-01, 8.10026062e-01, 6.38072403e-01],
           [8.84621526e-01, 8.15925395e-01, 6.48539462e-01],
           [8.85614592e-01, 8.21788285e-01, 6.59048859e-01],
           [8.86702289e-01, 8.27614084e-01, 6.69597115e-01],
           [8.87889516e-01, 8.33402244e-01, 6.80180833e-01],
           [8.89181222e-01, 8.39152246e-01, 6.90796251e-01],
           [8.90582336e-01, 8.44863616e-01, 7.01439304e-01],
           [8.92097443e-01, 8.50536012e-01, 7.12106155e-01],
           [8.93731530e-01, 8.56169030e-01, 7.22791834e-01],
           [8.95488748e-01, 8.61762521e-01, 7.33492452e-01],
           [8.97373732e-01, 8.67316252e-01, 7.44202724e-01],
           [8.99390578e-01, 8.72830163e-01, 7.54917869e-01],
           [9.01543131e-01, 8.78304287e-01, 7.65633089e-01],
           [9.03835612e-01, 8.83738618e-01, 7.76342169e-01],
           [9.06271323e-01, 8.89133381e-01, 7.87040280e-01],
           [9.08853678e-01, 8.94488809e-01, 7.97721785e-01],
           [9.11586246e-01, 8.99805146e-01, 8.08379998e-01],
           [9.14472044e-01, 9.05082766e-01, 8.19008982e-01],
           [9.17514032e-01, 9.10322073e-01, 8.29602437e-01],
           [9.20715268e-01, 9.15523473e-01, 8.40153327e-01],
           [9.24078938e-01, 9.20687375e-01, 8.50653788e-01],
           [9.27608322e-01, 9.25814188e-01, 8.61095312e-01],
           [9.31306737e-01, 9.30904299e-01, 8.71469161e-01],
           [9.35178037e-01, 9.35958041e-01, 8.81764746e-01],
           [9.39226540e-01, 9.40975720e-01, 8.91969652e-01],
           [9.43457073e-01, 9.45957665e-01, 9.02068971e-01],
           [9.47874825e-01, 9.50904385e-01, 9.12044403e-01],
           [9.52484829e-01, 9.55816879e-01, 9.21873185e-01],
           [9.57290652e-01, 9.60697263e-01, 9.31527028e-01],
           [9.62291713e-01, 9.65549867e-01, 9.40971718e-01],
           [9.67478538e-01, 9.70382926e-01, 9.50168874e-01],
           [9.72826027e-01, 9.75210567e-01, 9.59082435e-01],
           [9.78287385e-01, 9.80053801e-01, 9.67692361e-01],
           [9.83795465e-01, 9.84938154e-01, 9.76012541e-01],
           [9.89278574e-01, 9.89885972e-01, 9.84104942e-01],
           [9.94685265e-01, 9.94907946e-01, 9.92066682e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

cmap = ListedColormap(cm_data, name="sunburst")
