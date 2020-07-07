__author__ = "Ellert van der Velden (@1313e)"

from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.60742330e-04, 2.34190287e-04, 1.36018080e-04],
           [9.13691188e-04, 8.13696470e-04, 4.33185752e-04],
           [1.91036886e-03, 1.68887728e-03, 8.27564924e-04],
           [3.23082593e-03, 2.83869278e-03, 1.28589144e-03],
           [4.86279104e-03, 4.25056329e-03, 1.78566510e-03],
           [6.79747597e-03, 5.91613005e-03, 2.30999716e-03],
           [9.02785634e-03, 7.82958556e-03, 2.84576603e-03],
           [1.15479054e-02, 9.98685396e-03, 3.38233832e-03],
           [1.43521332e-02, 1.23851310e-02, 3.91090537e-03],
           [1.74352869e-02, 1.50226042e-02, 4.42408417e-03],
           [2.07922196e-02, 1.78982794e-02, 4.91534487e-03],
           [2.44176980e-02, 2.10118645e-02, 5.37892795e-03],
           [2.83060007e-02, 2.43636565e-02, 5.81084496e-03],
           [3.24513511e-02, 2.79545470e-02, 6.20656830e-03],
           [3.68473994e-02, 3.17859448e-02, 6.56264358e-03],
           [4.14622213e-02, 3.58597506e-02, 6.87646212e-03],
           [4.60335746e-02, 4.01784026e-02, 7.14508147e-03],
           [5.05273397e-02, 4.45487621e-02, 7.36660486e-03],
           [5.49447642e-02, 4.88818692e-02, 7.53987233e-03],
           [5.92865839e-02, 5.31864747e-02, 7.66251491e-03],
           [6.35526994e-02, 5.74668748e-02, 7.73426967e-03],
           [6.77424896e-02, 6.17271365e-02, 7.75469563e-03],
           [7.18547567e-02, 6.59711393e-02, 7.72352466e-03],
           [7.58877098e-02, 7.02026047e-02, 7.64093987e-03],
           [7.98389653e-02, 7.44251342e-02, 7.50761609e-03],
           [8.37055401e-02, 7.86422416e-02, 7.32476844e-03],
           [8.74838157e-02, 8.28574034e-02, 7.09402254e-03],
           [9.11693385e-02, 8.70742249e-02, 6.81653349e-03],
           [9.47572872e-02, 9.12959721e-02, 6.49662720e-03],
           [9.82415670e-02, 9.55263832e-02, 6.13626736e-03],
           [1.01615755e-01, 9.97688292e-02, 5.74096070e-03],
           [1.04872164e-01, 1.04027014e-01, 5.31544657e-03],
           [1.08002034e-01, 1.08304739e-01, 4.86560857e-03],
           [1.10995867e-01, 1.12605675e-01, 4.39962863e-03],
           [1.13842731e-01, 1.16933732e-01, 3.92642128e-03],
           [1.16531015e-01, 1.21292594e-01, 3.45774573e-03],
           [1.19047775e-01, 1.25686029e-01, 3.00701123e-03],
           [1.21378965e-01, 1.30117707e-01, 2.59016588e-03],
           [1.23509772e-01, 1.34591006e-01, 2.22635822e-03],
           [1.25425435e-01, 1.39108651e-01, 1.93878381e-03],
           [1.27111111e-01, 1.43672788e-01, 1.75422380e-03],
           [1.28552421e-01, 1.48284779e-01, 1.70340949e-03],
           [1.29738294e-01, 1.52944210e-01, 1.82237187e-03],
           [1.30658982e-01, 1.57649791e-01, 2.15016002e-03],
           [1.31310228e-01, 1.62398041e-01, 2.73012384e-03],
           [1.31691930e-01, 1.67184053e-01, 3.60774342e-03],
           [1.31809357e-01, 1.72001366e-01, 4.82983393e-03],
           [1.31672879e-01, 1.76842352e-01, 6.44313586e-03],
           [1.31297168e-01, 1.81698726e-01, 8.49308541e-03],
           [1.30700038e-01, 1.86562084e-01, 1.10229240e-02],
           [1.29901139e-01, 1.91424385e-01, 1.40732150e-02],
           [1.28920731e-01, 1.96278312e-01, 1.76817423e-02],
           [1.27778680e-01, 2.01117499e-01, 2.18837002e-02],
           [1.26493766e-01, 2.05936618e-01, 2.67120573e-02],
           [1.25084104e-01, 2.10731188e-01, 3.21975437e-02],
           [1.23565086e-01, 2.15497921e-01, 3.83699258e-02],
           [1.21951581e-01, 2.20234126e-01, 4.50222502e-02],
           [1.20256835e-01, 2.24937855e-01, 5.17303468e-02],
           [1.18493618e-01, 2.29607604e-01, 5.84894785e-02],
           [1.16672771e-01, 2.34242507e-01, 6.52937807e-02],
           [1.14805211e-01, 2.38841917e-01, 7.21380555e-02],
           [1.12901286e-01, 2.43405488e-01, 7.90180121e-02],
           [1.10970931e-01, 2.47933112e-01, 8.59300566e-02],
           [1.09023803e-01, 2.52424871e-01, 9.28711302e-02],
           [1.07069412e-01, 2.56880995e-01, 9.98385835e-02],
           [1.05117742e-01, 2.61301765e-01, 1.06829736e-01],
           [1.03178720e-01, 2.65687578e-01, 1.13842223e-01],
           [1.01261259e-01, 2.70039033e-01, 1.20874610e-01],
           [9.93768805e-02, 2.74356513e-01, 1.27924001e-01],
           [9.75342237e-02, 2.78640787e-01, 1.34989652e-01],
           [9.57453034e-02, 2.82892330e-01, 1.42068827e-01],
           [9.40196077e-02, 2.87111926e-01, 1.49160679e-01],
           [9.23679979e-02, 2.91300258e-01, 1.56263645e-01],
           [9.08021662e-02, 2.95457978e-01, 1.63375771e-01],
           [8.93324471e-02, 2.99585878e-01, 1.70496105e-01],
           [8.79696546e-02, 3.03684714e-01, 1.77623434e-01],
           [8.67245614e-02, 3.07755248e-01, 1.84756553e-01],
           [8.56076396e-02, 3.11798255e-01, 1.91894362e-01],
           [8.46289314e-02, 3.15814518e-01, 1.99035861e-01],
           [8.37979099e-02, 3.19804828e-01, 2.06180148e-01],
           [8.31233352e-02, 3.23769978e-01, 2.13326421e-01],
           [8.26131113e-02, 3.27710760e-01, 2.20473974e-01],
           [8.22741505e-02, 3.31627968e-01, 2.27622196e-01],
           [8.21122524e-02, 3.35522388e-01, 2.34770571e-01],
           [8.21320048e-02, 3.39394801e-01, 2.41918676e-01],
           [8.23367114e-02, 3.43245981e-01, 2.49066179e-01],
           [8.27283573e-02, 3.47076689e-01, 2.56212836e-01],
           [8.33079336e-02, 3.50887666e-01, 2.63358220e-01],
           [8.40744260e-02, 3.54679660e-01, 2.70502544e-01],
           [8.50259444e-02, 3.58453390e-01, 2.77645830e-01],
           [8.61594593e-02, 3.62209557e-01, 2.84788185e-01],
           [8.74711885e-02, 3.65948839e-01, 2.91929545e-01],
           [8.89559712e-02, 3.69671902e-01, 2.99070360e-01],
           [9.06080550e-02, 3.73379383e-01, 3.06211039e-01],
           [9.24213273e-02, 3.77071897e-01, 3.13351849e-01],
           [9.43891165e-02, 3.80750032e-01, 3.20493240e-01],
           [9.65042876e-02, 3.84414349e-01, 3.27635931e-01],
           [9.87598755e-02, 3.88065382e-01, 3.34780360e-01],
           [1.01148718e-01, 3.91703636e-01, 3.41927210e-01],
           [1.03663661e-01, 3.95329582e-01, 3.49077317e-01],
           [1.06298008e-01, 3.98943669e-01, 3.56231210e-01],
           [1.09044995e-01, 4.02546304e-01, 3.63389871e-01],
           [1.11898352e-01, 4.06137867e-01, 3.70554078e-01],
           [1.14852167e-01, 4.09718708e-01, 3.77724626e-01],
           [1.17900790e-01, 4.13289136e-01, 3.84902536e-01],
           [1.21039164e-01, 4.16849437e-01, 3.92088548e-01],
           [1.24262467e-01, 4.20399855e-01, 3.99283734e-01],
           [1.27566431e-01, 4.23940605e-01, 4.06488948e-01],
           [1.30947149e-01, 4.27471869e-01, 4.13705159e-01],
           [1.34401141e-01, 4.30993793e-01, 4.20933318e-01],
           [1.37925341e-01, 4.34506494e-01, 4.28174332e-01],
           [1.41517042e-01, 4.38010052e-01, 4.35429173e-01],
           [1.45173936e-01, 4.41504520e-01, 4.42698718e-01],
           [1.48894041e-01, 4.44989916e-01, 4.49983896e-01],
           [1.52675717e-01, 4.48466228e-01, 4.57285578e-01],
           [1.56517636e-01, 4.51933414e-01, 4.64604611e-01],
           [1.60418755e-01, 4.55391401e-01, 4.71941824e-01],
           [1.64378307e-01, 4.58840088e-01, 4.79298007e-01],
           [1.68395779e-01, 4.62279347e-01, 4.86673883e-01],
           [1.72470876e-01, 4.65709017e-01, 4.94070218e-01],
           [1.76603546e-01, 4.69128922e-01, 5.01487575e-01],
           [1.80793897e-01, 4.72538840e-01, 5.08926703e-01],
           [1.85042258e-01, 4.75938547e-01, 5.16388023e-01],
           [1.89349093e-01, 4.79327779e-01, 5.23872117e-01],
           [1.93715033e-01, 4.82706252e-01, 5.31379408e-01],
           [1.98140841e-01, 4.86073671e-01, 5.38910188e-01],
           [2.02627402e-01, 4.89429687e-01, 5.46464958e-01],
           [2.07175714e-01, 4.92773979e-01, 5.54043730e-01],
           [2.11786876e-01, 4.96106162e-01, 5.61646793e-01],
           [2.16462078e-01, 4.99425852e-01, 5.69274224e-01],
           [2.21202572e-01, 5.02732663e-01, 5.76925872e-01],
           [2.26009716e-01, 5.06026142e-01, 5.84601875e-01],
           [2.30884891e-01, 5.09305873e-01, 5.92301891e-01],
           [2.35829531e-01, 5.12571417e-01, 6.00025557e-01],
           [2.40845168e-01, 5.15822272e-01, 6.07772725e-01],
           [2.45933311e-01, 5.19057981e-01, 6.15542759e-01],
           [2.51095503e-01, 5.22278066e-01, 6.23334968e-01],
           [2.56333345e-01, 5.25482017e-01, 6.31148704e-01],
           [2.61648493e-01, 5.28669292e-01, 6.38983291e-01],
           [2.67042507e-01, 5.31839414e-01, 6.46837518e-01],
           [2.72517014e-01, 5.34991858e-01, 6.54710274e-01],
           [2.78073646e-01, 5.38126095e-01, 6.62600306e-01],
           [2.83714101e-01, 5.41241558e-01, 6.70506371e-01],
           [2.89439983e-01, 5.44337728e-01, 6.78426809e-01],
           [2.95252882e-01, 5.47414087e-01, 6.86359795e-01],
           [3.01154407e-01, 5.50470103e-01, 6.94303407e-01],
           [3.07146151e-01, 5.53505248e-01, 7.02255529e-01],
           [3.13229685e-01, 5.56519004e-01, 7.10213840e-01],
           [3.19406555e-01, 5.59510860e-01, 7.18175801e-01],
           [3.25678280e-01, 5.62480322e-01, 7.26138638e-01],
           [3.32046337e-01, 5.65426912e-01, 7.34099327e-01],
           [3.38512167e-01, 5.68350176e-01, 7.42054578e-01],
           [3.45077158e-01, 5.71249686e-01, 7.50000814e-01],
           [3.51742643e-01, 5.74125047e-01, 7.57934152e-01],
           [3.58509890e-01, 5.76975904e-01, 7.65850381e-01],
           [3.65380093e-01, 5.79801947e-01, 7.73744941e-01],
           [3.72354659e-01, 5.82602800e-01, 7.81613266e-01],
           [3.79434434e-01, 5.85378338e-01, 7.89449777e-01],
           [3.86620281e-01, 5.88128455e-01, 7.97248649e-01],
           [3.93913195e-01, 5.90853027e-01, 8.05003890e-01],
           [4.01314094e-01, 5.93551999e-01, 8.12709040e-01],
           [4.08823064e-01, 5.96225688e-01, 8.20356432e-01],
           [4.16441270e-01, 5.98874043e-01, 8.27939073e-01],
           [4.24168107e-01, 6.01497756e-01, 8.35447886e-01],
           [4.32004534e-01, 6.04096985e-01, 8.42874771e-01],
           [4.39949530e-01, 6.06672721e-01, 8.50209475e-01],
           [4.48002849e-01, 6.09225744e-01, 8.57441952e-01],
           [4.56163985e-01, 6.11757026e-01, 8.64561415e-01],
           [4.64431288e-01, 6.14268076e-01, 8.71555784e-01],
           [4.72803145e-01, 6.16760499e-01, 8.78412530e-01],
           [4.81277403e-01, 6.19236226e-01, 8.85118287e-01],
           [4.89851286e-01, 6.21697555e-01, 8.91658841e-01],
           [4.98521295e-01, 6.24147188e-01, 8.98019151e-01],
           [5.07283108e-01, 6.26588280e-01, 9.04183384e-01],
           [5.16131472e-01, 6.29024480e-01, 9.10134997e-01],
           [5.25060255e-01, 6.31459906e-01, 9.15856889e-01],
           [5.34062440e-01, 6.33899154e-01, 9.21331536e-01],
           [5.43128788e-01, 6.36347747e-01, 9.26540981e-01],
           [5.52249873e-01, 6.38811408e-01, 9.31467539e-01],
           [5.61413790e-01, 6.41296819e-01, 9.36093797e-01],
           [5.70608046e-01, 6.43810938e-01, 9.40403253e-01],
           [5.79817663e-01, 6.46361577e-01, 9.44380777e-01],
           [5.89026896e-01, 6.48956761e-01, 9.48013194e-01],
           [5.98218482e-01, 6.51604894e-01, 9.51289912e-01],
           [6.07373831e-01, 6.54314595e-01, 9.54203648e-01],
           [6.16473839e-01, 6.57094341e-01, 9.56750904e-01],
           [6.25499088e-01, 6.59952297e-01, 9.58932494e-01],
           [6.34430339e-01, 6.62896072e-01, 9.60753875e-01],
           [6.43249104e-01, 6.65932460e-01, 9.62225264e-01],
           [6.51938368e-01, 6.69067177e-01, 9.63361373e-01],
           [6.60483010e-01, 6.72304715e-01, 9.64181026e-01],
           [6.68869969e-01, 6.75648300e-01, 9.64706770e-01],
           [6.77088850e-01, 6.79099768e-01, 9.64963831e-01],
           [6.85132321e-01, 6.82659569e-01, 9.64978830e-01],
           [6.92994802e-01, 6.86327129e-01, 9.64780495e-01],
           [7.00674273e-01, 6.90100609e-01, 9.64396398e-01],
           [7.08170509e-01, 6.93977389e-01, 9.63854135e-01],
           [7.15485118e-01, 6.97954176e-01, 9.63180459e-01],
           [7.22621408e-01, 7.02027150e-01, 9.62400585e-01],
           [7.29584117e-01, 7.06192129e-01, 9.61537745e-01],
           [7.36379028e-01, 7.10444735e-01, 9.60613103e-01],
           [7.43012754e-01, 7.14780518e-01, 9.59645485e-01],
           [7.49492326e-01, 7.19195072e-01, 9.58651759e-01],
           [7.55824306e-01, 7.23684072e-01, 9.57649178e-01],
           [7.62016722e-01, 7.28243362e-01, 9.56649190e-01],
           [7.68076614e-01, 7.32868962e-01, 9.55664507e-01],
           [7.74010956e-01, 7.37557067e-01, 9.54706536e-01],
           [7.79827077e-01, 7.42304167e-01, 9.53783222e-01],
           [7.85531732e-01, 7.47106944e-01, 9.52902601e-01],
           [7.91131462e-01, 7.51962312e-01, 9.52071464e-01],
           [7.96632558e-01, 7.56867418e-01, 9.51295478e-01],
           [8.02040784e-01, 7.61819494e-01, 9.50581160e-01],
           [8.07362056e-01, 7.66816172e-01, 9.49931436e-01],
           [8.12601870e-01, 7.71855270e-01, 9.49349018e-01],
           [8.17765048e-01, 7.76934419e-01, 9.48840071e-01],
           [8.22856812e-01, 7.82052034e-01, 9.48403409e-01],
           [8.27881480e-01, 7.87205927e-01, 9.48045306e-01],
           [8.32843657e-01, 7.92394772e-01, 9.47764392e-01],
           [8.37747446e-01, 7.97617001e-01, 9.47562711e-01],
           [8.42596764e-01, 8.02870984e-01, 9.47443379e-01],
           [8.47395426e-01, 8.08155563e-01, 9.47406095e-01],
           [8.52147021e-01, 8.13469535e-01, 9.47451606e-01],
           [8.56854975e-01, 8.18811752e-01, 9.47580714e-01],
           [8.61522576e-01, 8.24181153e-01, 9.47793999e-01],
           [8.66152976e-01, 8.29576749e-01, 9.48091858e-01],
           [8.70749203e-01, 8.34997622e-01, 9.48474528e-01],
           [8.75314176e-01, 8.40442915e-01, 9.48942119e-01],
           [8.79850788e-01, 8.45911684e-01, 9.49495510e-01],
           [8.84361825e-01, 8.51403115e-01, 9.50134925e-01],
           [8.88849884e-01, 8.56916612e-01, 9.50859371e-01],
           [8.93317558e-01, 8.62451485e-01, 9.51668654e-01],
           [8.97767735e-01, 8.68006627e-01, 9.52565145e-01],
           [9.02202735e-01, 8.73581689e-01, 9.53546748e-01],
           [9.06625179e-01, 8.79175891e-01, 9.54613988e-01],
           [9.11037835e-01, 8.84788307e-01, 9.55768205e-01],
           [9.15443025e-01, 8.90418533e-01, 9.57007785e-01],
           [9.19843764e-01, 8.96065423e-01, 9.58335191e-01],
           [9.24242463e-01, 9.01728513e-01, 9.59749092e-01],
           [9.28642094e-01, 9.07406788e-01, 9.61251052e-01],
           [9.33045632e-01, 9.13099284e-01, 9.62842254e-01],
           [9.37455812e-01, 9.18805297e-01, 9.64522470e-01],
           [9.41876167e-01, 9.24523403e-01, 9.66295132e-01],
           [9.46309775e-01, 9.30252613e-01, 9.68161513e-01],
           [9.50759801e-01, 9.35991805e-01, 9.70123859e-01],
           [9.55229507e-01, 9.41739640e-01, 9.72186128e-01],
           [9.59722155e-01, 9.47494514e-01, 9.74354876e-01],
           [9.64239506e-01, 9.53255563e-01, 9.76635485e-01],
           [9.68781936e-01, 9.59022106e-01, 9.79036854e-01],
           [9.73346603e-01, 9.64794480e-01, 9.81570447e-01],
           [9.77924958e-01, 9.70575046e-01, 9.84249994e-01],
           [9.82499323e-01, 9.76369711e-01, 9.87089810e-01],
           [9.87039391e-01, 9.82189775e-01, 9.90100089e-01],
           [9.91501542e-01, 9.88053082e-01, 9.93277974e-01],
           [9.95835534e-01, 9.93982453e-01, 9.96596527e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

cmap = ListedColormap(cm_data, name="horizon")
