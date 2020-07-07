__author__ = "Ellert van der Velden (@1313e)"

from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [3.45220173e-04, 1.91908630e-04, 2.22295331e-04],
           [1.25316625e-03, 6.45171190e-04, 7.66558877e-04],
           [2.70346228e-03, 1.29798548e-03, 1.57931597e-03],
           [4.70211932e-03, 2.11827475e-03, 2.63526221e-03],
           [7.26113418e-03, 3.08337294e-03, 3.91731079e-03],
           [1.03948080e-02, 4.17548448e-03, 5.41234402e-03],
           [1.41186375e-02, 5.37976199e-03, 7.10951628e-03],
           [1.84490034e-02, 6.68326431e-03, 8.99939181e-03],
           [2.34031351e-02, 8.07431456e-03, 1.10734391e-02],
           [2.89979513e-02, 9.54252884e-03, 1.33238416e-02],
           [3.52511267e-02, 1.10781500e-02, 1.57431801e-02],
           [4.21312486e-02, 1.26718537e-02, 1.83242756e-02],
           [4.90938316e-02, 1.43152744e-02, 2.10602979e-02],
           [5.60282878e-02, 1.59999861e-02, 2.39443894e-02],
           [6.29406897e-02, 1.77181359e-02, 2.69698350e-02],
           [6.98359822e-02, 1.94622548e-02, 3.01299790e-02],
           [7.67192790e-02, 2.12246078e-02, 3.34179550e-02],
           [8.35935183e-02, 2.29985289e-02, 3.68271769e-02],
           [9.04631146e-02, 2.47763514e-02, 4.03505140e-02],
           [9.73298549e-02, 2.65519512e-02, 4.38374257e-02],
           [1.04197383e-01, 2.83178651e-02, 4.72480493e-02],
           [1.11067077e-01, 3.00681392e-02, 5.05859036e-02],
           [1.17941523e-01, 3.17958490e-02, 5.38521737e-02],
           [1.24822404e-01, 3.34946829e-02, 5.70479550e-02],
           [1.31710891e-01, 3.51587411e-02, 6.01742000e-02],
           [1.38609455e-01, 3.67808533e-02, 6.32311132e-02],
           [1.45518569e-01, 3.83556498e-02, 6.62193312e-02],
           [1.52439403e-01, 3.98771028e-02, 6.91390116e-02],
           [1.59373547e-01, 4.13181789e-02, 7.19899088e-02],
           [1.66321851e-01, 4.26601825e-02, 7.47718398e-02],
           [1.73284899e-01, 4.39102455e-02, 7.74845363e-02],
           [1.80263529e-01, 4.50676929e-02, 8.01274321e-02],
           [1.87258489e-01, 4.61316596e-02, 8.26998039e-02],
           [1.94270446e-01, 4.71010954e-02, 8.52007753e-02],
           [2.01299982e-01, 4.79747678e-02, 8.76293197e-02],
           [2.08347600e-01, 4.87512643e-02, 8.99842621e-02],
           [2.15413719e-01, 4.94289941e-02, 9.22642807e-02],
           [2.22498675e-01, 5.00061889e-02, 9.44679063e-02],
           [2.29602716e-01, 5.04809043e-02, 9.65935231e-02],
           [2.36726002e-01, 5.08510200e-02, 9.86393669e-02],
           [2.43868594e-01, 5.11142411e-02, 1.00603525e-01],
           [2.51030453e-01, 5.12681001e-02, 1.02483933e-01],
           [2.58211742e-01, 5.13094748e-02, 1.04278163e-01],
           [2.65412833e-01, 5.12344917e-02, 1.05983370e-01],
           [2.72632586e-01, 5.10412781e-02, 1.07597497e-01],
           [2.79871561e-01, 5.07248086e-02, 1.09117006e-01],
           [2.87128804e-01, 5.02820709e-02, 1.10539147e-01],
           [2.94404364e-01, 4.97078351e-02, 1.11860068e-01],
           [3.01696835e-01, 4.89989192e-02, 1.13076716e-01],
           [3.09006507e-01, 4.81484060e-02, 1.14184221e-01],
           [3.16331883e-01, 4.71520413e-02, 1.15178759e-01],
           [3.23671812e-01, 4.60042594e-02, 1.16055741e-01],
           [3.31025108e-01, 4.46987786e-02, 1.16810051e-01],
           [3.38390277e-01, 4.32291011e-02, 1.17436233e-01],
           [3.45765460e-01, 4.15886159e-02, 1.17928492e-01],
           [3.53148383e-01, 3.97626237e-02, 1.18280696e-01],
           [3.60537183e-01, 3.77745449e-02, 1.18485311e-01],
           [3.67928321e-01, 3.56644446e-02, 1.18535690e-01],
           [3.75318576e-01, 3.34436698e-02, 1.18423679e-01],
           [3.82703524e-01, 3.11282035e-02, 1.18141322e-01],
           [3.90078966e-01, 2.87350595e-02, 1.17678808e-01],
           [3.97438918e-01, 2.62881015e-02, 1.17027044e-01],
           [4.04776790e-01, 2.38151748e-02, 1.16175890e-01],
           [4.12084714e-01, 2.13504041e-02, 1.15114951e-01],
           [4.19352723e-01, 1.89371127e-02, 1.13834997e-01],
           [4.26570742e-01, 1.66224567e-02, 1.12324220e-01],
           [4.33725129e-01, 1.44682396e-02, 1.10574776e-01],
           [4.40800995e-01, 1.25445969e-02, 1.08578823e-01],
           [4.47780992e-01, 1.09341219e-02, 1.06331686e-01],
           [4.54646057e-01, 9.72993081e-03, 1.03831334e-01],
           [4.61374407e-01, 9.03875437e-03, 1.01083575e-01],
           [4.67943867e-01, 8.97333957e-03, 9.80989370e-02],
           [4.74332037e-01, 9.65079659e-03, 9.48965003e-02],
           [4.80518085e-01, 1.11852657e-02, 9.15036915e-02],
           [4.86484602e-01, 1.36798254e-02, 8.79551508e-02],
           [4.92219263e-01, 1.72188440e-02, 8.42902141e-02],
           [4.97715857e-01, 2.18626551e-02, 8.05497029e-02],
           [5.02974461e-01, 2.76455908e-02, 7.67726562e-02],
           [5.08000816e-01, 3.45775480e-02, 7.29932913e-02],
           [5.12805043e-01, 4.25782994e-02, 6.92386981e-02],
           [5.17400121e-01, 5.08402514e-02, 6.55288787e-02],
           [5.21800517e-01, 5.91181556e-02, 6.18772701e-02],
           [5.26020851e-01, 6.73602677e-02, 5.82898648e-02],
           [5.30075508e-01, 7.55322822e-02, 5.47703989e-02],
           [5.33977613e-01, 8.36143272e-02, 5.13167800e-02],
           [5.37739248e-01, 9.15949094e-02, 4.79258557e-02],
           [5.41371164e-01, 9.94689338e-02, 4.45925733e-02],
           [5.44882773e-01, 1.07235673e-01, 4.13105904e-02],
           [5.48282664e-01, 1.14896196e-01, 3.80760523e-02],
           [5.51577719e-01, 1.22454969e-01, 3.50111958e-02],
           [5.54774696e-01, 1.29915472e-01, 3.21246475e-02],
           [5.57878762e-01, 1.37283559e-01, 2.94033275e-02],
           [5.60894775e-01, 1.44564373e-01, 2.68372138e-02],
           [5.63826925e-01, 1.51763219e-01, 2.44174876e-02],
           [5.66678815e-01, 1.58885403e-01, 2.21365016e-02],
           [5.69453537e-01, 1.65936126e-01, 1.99877302e-02],
           [5.72153881e-01, 1.72920179e-01, 1.79660285e-02],
           [5.74782485e-01, 1.79841794e-01, 1.60676895e-02],
           [5.77340918e-01, 1.86706159e-01, 1.42882549e-02],
           [5.79831603e-01, 1.93516432e-01, 1.26265556e-02],
           [5.82255494e-01, 2.00277390e-01, 1.10796622e-02],
           [5.84614617e-01, 2.06991685e-01, 9.64788529e-03],
           [5.86909745e-01, 2.13663274e-01, 8.33016539e-03],
           [5.89141917e-01, 2.20295265e-01, 7.12690849e-03],
           [5.91312092e-01, 2.26890484e-01, 6.03920403e-03],
           [5.93421279e-01, 2.33451351e-01, 5.06895055e-03],
           [5.95469903e-01, 2.39980699e-01, 4.21783174e-03],
           [5.97458510e-01, 2.46480898e-01, 3.48840788e-03],
           [5.99387567e-01, 2.52954153e-01, 2.88373936e-03],
           [6.01257445e-01, 2.59402531e-01, 2.40734229e-03],
           [6.03068435e-01, 2.65827975e-01, 2.06318103e-03],
           [6.04820763e-01, 2.72232296e-01, 1.85567512e-03],
           [6.06514791e-01, 2.78616985e-01, 1.78990843e-03],
           [6.08150425e-01, 2.84983843e-01, 1.87093242e-03],
           [6.09727696e-01, 2.91334375e-01, 2.10445239e-03],
           [6.11246587e-01, 2.97669992e-01, 2.49661019e-03],
           [6.12707101e-01, 3.03991957e-01, 3.05404059e-03],
           [6.14109434e-01, 3.10301242e-01, 3.78401163e-03],
           [6.15453120e-01, 3.16599319e-01, 4.69364819e-03],
           [6.16738001e-01, 3.22887263e-01, 5.79084960e-03],
           [6.17964315e-01, 3.29165720e-01, 7.08428371e-03],
           [6.19131467e-01, 3.35435967e-01, 8.58241672e-03],
           [6.20239297e-01, 3.41698823e-01, 1.02945444e-02],
           [6.21287824e-01, 3.47954893e-01, 1.22305338e-02],
           [6.22276407e-01, 3.54205243e-01, 1.44002979e-02],
           [6.23205158e-01, 3.60450277e-01, 1.68146978e-02],
           [6.24073484e-01, 3.66690887e-01, 1.94846631e-02],
           [6.24881270e-01, 3.72927543e-01, 2.24218770e-02],
           [6.25628126e-01, 3.79160872e-01, 2.56383701e-02],
           [6.26313762e-01, 3.85391375e-01, 2.91467215e-02],
           [6.26937869e-01, 3.91619525e-01, 3.29599994e-02],
           [6.27500098e-01, 3.97845780e-01, 3.70917674e-02],
           [6.28000142e-01, 4.04070528e-01, 4.15289618e-02],
           [6.28437662e-01, 4.10294147e-01, 4.60375144e-02],
           [6.28812316e-01, 4.16516978e-01, 5.05905514e-02],
           [6.29123802e-01, 4.22739308e-01, 5.51886166e-02],
           [6.29371737e-01, 4.28961444e-01, 5.98323278e-02],
           [6.29555852e-01, 4.35183596e-01, 6.45223594e-02],
           [6.29675746e-01, 4.41406029e-01, 6.92594205e-02],
           [6.29731148e-01, 4.47628905e-01, 7.40442372e-02],
           [6.29721684e-01, 4.53852424e-01, 7.88775538e-02],
           [6.29647027e-01, 4.60076741e-01, 8.37601182e-02],
           [6.29506864e-01, 4.66301977e-01, 8.86926779e-02],
           [6.29300805e-01, 4.72528283e-01, 9.36759956e-02],
           [6.29028571e-01, 4.78755727e-01, 9.87108150e-02],
           [6.28689750e-01, 4.84984433e-01, 1.03797911e-01],
           [6.28284038e-01, 4.91214451e-01, 1.08938039e-01],
           [6.27811039e-01, 4.97445864e-01, 1.14131989e-01],
           [6.27270386e-01, 5.03678721e-01, 1.19380554e-01],
           [6.26661711e-01, 5.09913058e-01, 1.24684549e-01],
           [6.25984571e-01, 5.16148932e-01, 1.30044835e-01],
           [6.25238609e-01, 5.22386344e-01, 1.35462278e-01],
           [6.24423343e-01, 5.28625337e-01, 1.40937822e-01],
           [6.23538345e-01, 5.34865914e-01, 1.46472441e-01],
           [6.22583200e-01, 5.41108055e-01, 1.52067156e-01],
           [6.21557261e-01, 5.47351828e-01, 1.57723138e-01],
           [6.20460372e-01, 5.53597068e-01, 1.63441444e-01],
           [6.19291432e-01, 5.59844004e-01, 1.69223586e-01],
           [6.18050561e-01, 5.66092319e-01, 1.75070681e-01],
           [6.16736705e-01, 5.72342179e-01, 1.80984431e-01],
           [6.15349492e-01, 5.78593441e-01, 1.86966380e-01],
           [6.13888651e-01, 5.84845908e-01, 1.93018154e-01],
           [6.12352950e-01, 5.91099746e-01, 1.99141957e-01],
           [6.10742292e-01, 5.97354644e-01, 2.05339660e-01],
           [6.09056286e-01, 6.03610396e-01, 2.11613442e-01],
           [6.07294249e-01, 6.09866882e-01, 2.17965827e-01],
           [6.05455313e-01, 6.16124027e-01, 2.24399669e-01],
           [6.03539624e-01, 6.22381357e-01, 2.30917590e-01],
           [6.01546862e-01, 6.28638555e-01, 2.37522719e-01],
           [5.99476826e-01, 6.34895241e-01, 2.44218445e-01],
           [5.97329474e-01, 6.41150957e-01, 2.51008434e-01],
           [5.95104966e-01, 6.47405160e-01, 2.57896647e-01],
           [5.92803723e-01, 6.53657204e-01, 2.64887354e-01],
           [5.90426489e-01, 6.59906322e-01, 2.71985154e-01],
           [5.87974412e-01, 6.66151610e-01, 2.79194984e-01],
           [5.85449139e-01, 6.72392000e-01, 2.86522139e-01],
           [5.82852924e-01, 6.78626242e-01, 2.93972279e-01],
           [5.80188761e-01, 6.84852872e-01, 3.01551441e-01],
           [5.77459821e-01, 6.91070384e-01, 3.09266472e-01],
           [5.74670663e-01, 6.97276889e-01, 3.17124445e-01],
           [5.71828249e-01, 7.03469864e-01, 3.25132119e-01],
           [5.68938230e-01, 7.09647193e-01, 3.33298412e-01],
           [5.66011380e-01, 7.15805440e-01, 3.41630497e-01],
           [5.63056745e-01, 7.21941711e-01, 3.50138400e-01],
           [5.60089414e-01, 7.28051649e-01, 3.58830061e-01],
           [5.57125265e-01, 7.34130846e-01, 3.67715029e-01],
           [5.54183268e-01, 7.40174278e-01, 3.76803179e-01],
           [5.51287126e-01, 7.46175974e-01, 3.86103679e-01],
           [5.48465036e-01, 7.52129140e-01, 3.95625264e-01],
           [5.45749570e-01, 7.58026251e-01, 4.05376475e-01],
           [5.43179217e-01, 7.63858768e-01, 4.15364376e-01],
           [5.40799047e-01, 7.69617094e-01, 4.25593632e-01],
           [5.38659811e-01, 7.75290840e-01, 4.36066731e-01],
           [5.36817536e-01, 7.80868963e-01, 4.46783548e-01],
           [5.35335343e-01, 7.86339530e-01, 4.57737534e-01],
           [5.34278761e-01, 7.91690666e-01, 4.68918338e-01],
           [5.33715511e-01, 7.96910672e-01, 4.80308636e-01],
           [5.33711709e-01, 8.01988767e-01, 4.91884238e-01],
           [5.34327642e-01, 8.06915841e-01, 5.03614745e-01],
           [5.35613950e-01, 8.11685098e-01, 5.15463722e-01],
           [5.37607635e-01, 8.16292665e-01, 5.27390329e-01],
           [5.40329070e-01, 8.20737946e-01, 5.39351951e-01],
           [5.43780949e-01, 8.25023653e-01, 5.51305870e-01],
           [5.47948638e-01, 8.29155600e-01, 5.63211325e-01],
           [5.52802240e-01, 8.33142057e-01, 5.75033368e-01],
           [5.58299957e-01, 8.36993211e-01, 5.86741619e-01],
           [5.64391283e-01, 8.40720608e-01, 5.98310539e-01],
           [5.71021443e-01, 8.44336052e-01, 6.09723142e-01],
           [5.78133893e-01, 8.47851494e-01, 6.20966664e-01],
           [5.85671889e-01, 8.51278922e-01, 6.32031031e-01],
           [5.93583217e-01, 8.54628895e-01, 6.42914613e-01],
           [6.01817475e-01, 8.57911955e-01, 6.53614830e-01],
           [6.10330112e-01, 8.61137195e-01, 6.64134379e-01],
           [6.19078740e-01, 8.64313720e-01, 6.74474137e-01],
           [6.28027429e-01, 8.67449073e-01, 6.84639388e-01],
           [6.37144203e-01, 8.70550136e-01, 6.94635674e-01],
           [6.46399461e-01, 8.73623646e-01, 7.04467255e-01],
           [6.55768813e-01, 8.76675113e-01, 7.14140715e-01],
           [6.65231937e-01, 8.79709170e-01, 7.23663503e-01],
           [6.74767553e-01, 8.82731305e-01, 7.33039168e-01],
           [6.84361951e-01, 8.85744742e-01, 7.42276253e-01],
           [6.93997517e-01, 8.88754503e-01, 7.51377326e-01],
           [7.03664959e-01, 8.91762958e-01, 7.60350712e-01],
           [7.13353054e-01, 8.94773463e-01, 7.69201151e-01],
           [7.23052220e-01, 8.97789043e-01, 7.77933380e-01],
           [7.32754323e-01, 9.00812417e-01, 7.86552081e-01],
           [7.42452495e-01, 9.03846034e-01, 7.95061843e-01],
           [7.52140978e-01, 9.06892098e-01, 8.03467129e-01],
           [7.61814971e-01, 9.09952597e-01, 8.11772250e-01],
           [7.71470496e-01, 9.13029330e-01, 8.19981342e-01],
           [7.81104285e-01, 9.16123931e-01, 8.28098348e-01],
           [7.90711630e-01, 9.19238677e-01, 8.36125645e-01],
           [8.00289792e-01, 9.22375176e-01, 8.44066470e-01],
           [8.09839077e-01, 9.25533917e-01, 8.51925535e-01],
           [8.19352928e-01, 9.28718119e-01, 8.59702687e-01],
           [8.28834401e-01, 9.31927295e-01, 8.67403505e-01],
           [8.38277414e-01, 9.35164594e-01, 8.75027488e-01],
           [8.47685083e-01, 9.38429566e-01, 8.82579409e-01],
           [8.57051716e-01, 9.41725303e-01, 8.90058452e-01],
           [8.66379155e-01, 9.45051921e-01, 8.97467925e-01],
           [8.75666602e-01, 9.48410614e-01, 9.04809230e-01],
           [8.84910046e-01, 9.51803928e-01, 9.12081730e-01],
           [8.94110256e-01, 9.55232496e-01, 9.19287094e-01],
           [9.03266377e-01, 9.58697643e-01, 9.26425730e-01],
           [9.12376723e-01, 9.62201081e-01, 9.33497240e-01],
           [9.21439357e-01, 9.65744671e-01, 9.40500717e-01],
           [9.30451314e-01, 9.69330763e-01, 9.47434349e-01],
           [9.39409980e-01, 9.72961625e-01, 9.54296060e-01],
           [9.48312072e-01, 9.76639873e-01, 9.61083012e-01],
           [9.57152227e-01, 9.80369068e-01, 9.67791105e-01],
           [9.65922871e-01, 9.84153757e-01, 9.74415316e-01],
           [9.74613024e-01, 9.87999918e-01, 9.80950110e-01],
           [9.83206531e-01, 9.91915541e-01, 9.87390771e-01],
           [9.91679773e-01, 9.95911208e-01, 9.93736879e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

cmap = ListedColormap(cm_data, name="apple")
