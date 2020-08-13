# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'diverging'

# RGB-values of this colormap
cm_data = [[5.93577071e-01, 9.89836236e-01, 1.02981048e-01],
           [5.85434900e-01, 9.85863765e-01, 1.07477611e-01],
           [5.77298967e-01, 9.81894688e-01, 1.11812644e-01],
           [5.69169206e-01, 9.77928747e-01, 1.16002639e-01],
           [5.61045612e-01, 9.73965670e-01, 1.20061660e-01],
           [5.52928250e-01, 9.70005173e-01, 1.24001804e-01],
           [5.44817258e-01, 9.66046965e-01, 1.27833554e-01],
           [5.36712578e-01, 9.62090781e-01, 1.31566721e-01],
           [5.28614934e-01, 9.58136240e-01, 1.35208295e-01],
           [5.20524748e-01, 9.54183012e-01, 1.38765315e-01],
           [5.12442519e-01, 9.50230756e-01, 1.42244063e-01],
           [5.04368740e-01, 9.46279140e-01, 1.45650368e-01],
           [4.96303889e-01, 9.42327835e-01, 1.48989707e-01],
           [4.88249040e-01, 9.38376434e-01, 1.52265993e-01],
           [4.80205187e-01, 9.34424550e-01, 1.55483148e-01],
           [4.72173469e-01, 9.30471784e-01, 1.58644673e-01],
           [4.64155185e-01, 9.26517727e-01, 1.61753696e-01],
           [4.56151066e-01, 9.22562051e-01, 1.64814465e-01],
           [4.48162940e-01, 9.18604298e-01, 1.67829052e-01],
           [4.40193104e-01, 9.14643969e-01, 1.70798722e-01],
           [4.32242652e-01, 9.10680724e-01, 1.73727259e-01],
           [4.24314168e-01, 9.06714063e-01, 1.76615703e-01],
           [4.16410169e-01, 9.02743511e-01, 1.79465473e-01],
           [4.08532779e-01, 8.98768659e-01, 1.82279021e-01],
           [4.00685438e-01, 8.94788974e-01, 1.85056584e-01],
           [3.92871072e-01, 8.90804004e-01, 1.87799747e-01],
           [3.85093011e-01, 8.86813279e-01, 1.90509729e-01],
           [3.77355641e-01, 8.82816255e-01, 1.93186165e-01],
           [3.69662556e-01, 8.78812494e-01, 1.95830702e-01],
           [3.62018381e-01, 8.74801494e-01, 1.98443534e-01],
           [3.54428313e-01, 8.70782739e-01, 2.01024313e-01],
           [3.46897579e-01, 8.66755747e-01, 2.03573226e-01],
           [3.39431846e-01, 8.62720044e-01, 2.06090255e-01],
           [3.32037219e-01, 8.58675160e-01, 2.08575180e-01],
           [3.24720254e-01, 8.54620635e-01, 2.11027598e-01],
           [3.17487950e-01, 8.50556024e-01, 2.13446928e-01],
           [3.10347747e-01, 8.46480902e-01, 2.15832427e-01],
           [3.03307514e-01, 8.42394864e-01, 2.18183203e-01],
           [2.96375530e-01, 8.38297534e-01, 2.20498225e-01],
           [2.89560458e-01, 8.34188566e-01, 2.22776338e-01],
           [2.82871313e-01, 8.30067649e-01, 2.25016283e-01],
           [2.76317421e-01, 8.25934509e-01, 2.27216707e-01],
           [2.69908333e-01, 8.21788919e-01, 2.29376280e-01],
           [2.63653739e-01, 8.17630690e-01, 2.31493891e-01],
           [2.57563718e-01, 8.13459683e-01, 2.33567484e-01],
           [2.51648223e-01, 8.09275814e-01, 2.35595493e-01],
           [2.45917079e-01, 8.05079043e-01, 2.37576833e-01],
           [2.40380162e-01, 8.00869394e-01, 2.39509420e-01],
           [2.35046959e-01, 7.96646944e-01, 2.41391775e-01],
           [2.29926582e-01, 7.92411817e-01, 2.43222560e-01],
           [2.25027662e-01, 7.88164210e-01, 2.44999950e-01],
           [2.20358165e-01, 7.83904353e-01, 2.46722855e-01],
           [2.15925276e-01, 7.79632550e-01, 2.48389643e-01],
           [2.11735295e-01, 7.75349138e-01, 2.49999236e-01],
           [2.07793474e-01, 7.71054512e-01, 2.51550394e-01],
           [2.04103949e-01, 7.66749106e-01, 2.53042143e-01],
           [2.00669617e-01, 7.62433395e-01, 2.54473567e-01],
           [1.97492074e-01, 7.58107891e-01, 2.55843909e-01],
           [1.94571561e-01, 7.53773135e-01, 2.57152547e-01],
           [1.91906934e-01, 7.49429695e-01, 2.58399003e-01],
           [1.89495651e-01, 7.45078164e-01, 2.59582919e-01],
           [1.87333849e-01, 7.40719145e-01, 2.60704134e-01],
           [1.85416271e-01, 7.36353265e-01, 2.61762501e-01],
           [1.83736597e-01, 7.31981141e-01, 2.62758225e-01],
           [1.82287087e-01, 7.27603425e-01, 2.63691277e-01],
           [1.81059391e-01, 7.23220727e-01, 2.64562206e-01],
           [1.80043866e-01, 7.18833698e-01, 2.65371220e-01],
           [1.79230452e-01, 7.14442948e-01, 2.66118955e-01],
           [1.78608454e-01, 7.10049084e-01, 2.66806070e-01],
           [1.78166382e-01, 7.05652741e-01, 2.67433011e-01],
           [1.77893062e-01, 7.01254474e-01, 2.68000805e-01],
           [1.77776817e-01, 6.96854860e-01, 2.68510243e-01],
           [1.77805669e-01, 6.92454487e-01, 2.68961986e-01],
           [1.77968373e-01, 6.88053861e-01, 2.69357210e-01],
           [1.78253536e-01, 6.83653501e-01, 2.69696881e-01],
           [1.78649914e-01, 6.79253921e-01, 2.69981913e-01],
           [1.79146656e-01, 6.74855610e-01, 2.70213284e-01],
           [1.79733621e-01, 6.70459006e-01, 2.70392186e-01],
           [1.80400902e-01, 6.66064548e-01, 2.70519678e-01],
           [1.81139077e-01, 6.61672657e-01, 2.70596833e-01],
           [1.81939229e-01, 6.57283731e-01, 2.70624728e-01],
           [1.82792915e-01, 6.52898154e-01, 2.70604417e-01],
           [1.83692207e-01, 6.48516293e-01, 2.70536951e-01],
           [1.84629882e-01, 6.44138472e-01, 2.70423481e-01],
           [1.85599093e-01, 6.39765013e-01, 2.70265071e-01],
           [1.86593490e-01, 6.35396219e-01, 2.70062779e-01],
           [1.87607197e-01, 6.31032377e-01, 2.69817646e-01],
           [1.88634797e-01, 6.26673753e-01, 2.69530704e-01],
           [1.89671308e-01, 6.22320600e-01, 2.69202964e-01],
           [1.90712158e-01, 6.17973156e-01, 2.68835423e-01],
           [1.91753165e-01, 6.13631639e-01, 2.68429058e-01],
           [1.92790393e-01, 6.09296273e-01, 2.67984768e-01],
           [1.93820400e-01, 6.04967244e-01, 2.67503510e-01],
           [1.94840078e-01, 6.00644727e-01, 2.66986230e-01],
           [1.95846561e-01, 5.96328888e-01, 2.66433822e-01],
           [1.96837255e-01, 5.92019882e-01, 2.65847162e-01],
           [1.97809818e-01, 5.87717852e-01, 2.65227102e-01],
           [1.98762075e-01, 5.83422940e-01, 2.64574441e-01],
           [1.99691930e-01, 5.79135295e-01, 2.63889890e-01],
           [2.00597940e-01, 5.74854995e-01, 2.63174362e-01],
           [2.01478589e-01, 5.70582144e-01, 2.62428622e-01],
           [2.02332483e-01, 5.66316841e-01, 2.61653394e-01],
           [2.03158116e-01, 5.62059215e-01, 2.60849255e-01],
           [2.03954774e-01, 5.57809297e-01, 2.60017073e-01],
           [2.04721521e-01, 5.53567156e-01, 2.59157530e-01],
           [2.05457212e-01, 5.49332902e-01, 2.58271132e-01],
           [2.06161373e-01, 5.45106559e-01, 2.57358636e-01],
           [2.06833477e-01, 5.40888161e-01, 2.56420708e-01],
           [2.07472618e-01, 5.36677810e-01, 2.55457772e-01],
           [2.08078676e-01, 5.32475494e-01, 2.54470573e-01],
           [2.08651216e-01, 5.28281255e-01, 2.53459651e-01],
           [2.09189715e-01, 5.24095150e-01, 2.52425458e-01],
           [2.09694245e-01, 5.19917154e-01, 2.51368682e-01],
           [2.10164261e-01, 5.15747336e-01, 2.50289675e-01],
           [2.10599888e-01, 5.11585667e-01, 2.49189071e-01],
           [2.11000876e-01, 5.07432177e-01, 2.48067288e-01],
           [2.11367191e-01, 5.03286867e-01, 2.46924811e-01],
           [2.11698853e-01, 4.99149727e-01, 2.45762122e-01],
           [2.11995754e-01, 4.95020773e-01, 2.44579610e-01],
           [2.12258076e-01, 4.90899971e-01, 2.43377777e-01],
           [2.12485710e-01, 4.86787340e-01, 2.42156958e-01],
           [2.12678912e-01, 4.82682835e-01, 2.40917641e-01],
           [2.12837621e-01, 4.78586466e-01, 2.39660138e-01],
           [2.12962108e-01, 4.74498188e-01, 2.38384899e-01],
           [2.13052395e-01, 4.70417997e-01, 2.37092235e-01],
           [2.13108717e-01, 4.66345850e-01, 2.35782542e-01],
           [2.13131207e-01, 4.62281726e-01, 2.34456149e-01],
           [2.13120030e-01, 4.58225594e-01, 2.33113386e-01],
           [2.13075440e-01, 4.54177407e-01, 2.31754606e-01],
           [2.12997519e-01, 4.50137148e-01, 2.30380071e-01],
           [2.12886628e-01, 4.46104749e-01, 2.28990160e-01],
           [2.12742791e-01, 4.42080202e-01, 2.27585079e-01],
           [2.12566390e-01, 4.38063432e-01, 2.26165194e-01],
           [2.12357551e-01, 4.34054408e-01, 2.24730739e-01],
           [2.12116523e-01, 4.30053079e-01, 2.23281994e-01],
           [2.11843569e-01, 4.26059384e-01, 2.21819237e-01],
           [2.11538821e-01, 4.22073289e-01, 2.20342675e-01],
           [2.11202614e-01, 4.18094720e-01, 2.18852604e-01],
           [2.10835105e-01, 4.14123632e-01, 2.17349225e-01],
           [2.10436550e-01, 4.10159962e-01, 2.15832780e-01],
           [2.10007201e-01, 4.06203644e-01, 2.14303503e-01],
           [2.09547218e-01, 4.02254629e-01, 2.12761574e-01],
           [2.09056896e-01, 3.98312839e-01, 2.11207236e-01],
           [2.08536425e-01, 3.94378214e-01, 2.09640673e-01],
           [2.07986026e-01, 3.90450687e-01, 2.08062077e-01],
           [2.07405941e-01, 3.86530183e-01, 2.06471648e-01],
           [2.06796355e-01, 3.82616637e-01, 2.04869552e-01],
           [2.06157503e-01, 3.78709972e-01, 2.03255976e-01],
           [2.05489592e-01, 3.74810114e-01, 2.01631085e-01],
           [2.04792819e-01, 3.70916988e-01, 1.99995040e-01],
           [2.04067396e-01, 3.67030514e-01, 1.98348002e-01],
           [2.03313517e-01, 3.63150613e-01, 1.96690121e-01],
           [2.02531378e-01, 3.59277203e-01, 1.95021544e-01],
           [2.01721162e-01, 3.55410202e-01, 1.93342410e-01],
           [2.00883066e-01, 3.51549522e-01, 1.91652860e-01],
           [2.00017261e-01, 3.47695080e-01, 1.89953019e-01],
           [1.99123917e-01, 3.43846788e-01, 1.88243009e-01],
           [1.98203229e-01, 3.40004549e-01, 1.86522965e-01],
           [1.97255330e-01, 3.36168281e-01, 1.84792984e-01],
           [1.96280400e-01, 3.32337884e-01, 1.83053188e-01],
           [1.95278595e-01, 3.28513262e-01, 1.81303683e-01],
           [1.94250034e-01, 3.24694326e-01, 1.79544553e-01],
           [1.93194915e-01, 3.20880962e-01, 1.77775926e-01],
           [1.92113324e-01, 3.17073082e-01, 1.75997864e-01],
           [1.91005408e-01, 3.13270579e-01, 1.74210463e-01],
           [1.89871316e-01, 3.09473342e-01, 1.72413819e-01],
           [1.88711112e-01, 3.05681279e-01, 1.70607978e-01],
           [1.87524987e-01, 3.01894259e-01, 1.68793059e-01],
           [1.86312976e-01, 2.98112190e-01, 1.66969089e-01],
           [1.85075212e-01, 2.94334949e-01, 1.65136153e-01],
           [1.83811796e-01, 2.90562419e-01, 1.63294315e-01],
           [1.82522767e-01, 2.86794494e-01, 1.61443603e-01],
           [1.81208292e-01, 2.83031029e-01, 1.59584120e-01],
           [1.79868336e-01, 2.79271932e-01, 1.57715849e-01],
           [1.78503074e-01, 2.75517045e-01, 1.55838899e-01],
           [1.77112466e-01, 2.71766268e-01, 1.53953249e-01],
           [1.75696635e-01, 2.68019450e-01, 1.52058978e-01],
           [1.74255574e-01, 2.64276469e-01, 1.50156083e-01],
           [1.72789350e-01, 2.60537181e-01, 1.48244611e-01],
           [1.71297971e-01, 2.56801450e-01, 1.46324569e-01],
           [1.69781466e-01, 2.53069130e-01, 1.44395981e-01],
           [1.68239838e-01, 2.49340076e-01, 1.42458853e-01],
           [1.66673096e-01, 2.45614136e-01, 1.40513197e-01],
           [1.65081215e-01, 2.41891161e-01, 1.38559003e-01],
           [1.63464212e-01, 2.38170984e-01, 1.36596291e-01],
           [1.61822000e-01, 2.34453462e-01, 1.34625013e-01],
           [1.60154635e-01, 2.30738400e-01, 1.32645217e-01],
           [1.58461945e-01, 2.27025668e-01, 1.30656801e-01],
           [1.56744024e-01, 2.23315044e-01, 1.28659843e-01],
           [1.55000672e-01, 2.19606391e-01, 1.26654224e-01],
           [1.53231868e-01, 2.15899505e-01, 1.24639950e-01],
           [1.51437540e-01, 2.12194193e-01, 1.22616993e-01],
           [1.49617506e-01, 2.08490286e-01, 1.20585249e-01],
           [1.47771757e-01, 2.04787547e-01, 1.18544742e-01],
           [1.45900099e-01, 2.01085793e-01, 1.16495367e-01],
           [1.44002358e-01, 1.97384820e-01, 1.14437033e-01],
           [1.42078466e-01, 1.93684382e-01, 1.12369732e-01],
           [1.40128206e-01, 1.89984265e-01, 1.10293351e-01],
           [1.38151360e-01, 1.86284248e-01, 1.08207775e-01],
           [1.36147727e-01, 1.82584087e-01, 1.06112909e-01],
           [1.34117184e-01, 1.78883500e-01, 1.04008727e-01],
           [1.32059400e-01, 1.75182260e-01, 1.01895039e-01],
           [1.29974120e-01, 1.71480098e-01, 9.97717223e-02],
           [1.27861071e-01, 1.67776735e-01, 9.76386458e-02],
           [1.25719958e-01, 1.64071881e-01, 9.54956666e-02],
           [1.23550491e-01, 1.60365226e-01, 9.33426537e-02],
           [1.21352316e-01, 1.56656461e-01, 9.11794297e-02],
           [1.19125043e-01, 1.52945271e-01, 8.90057926e-02],
           [1.16868279e-01, 1.49231316e-01, 8.68215460e-02],
           [1.14581600e-01, 1.45514245e-01, 8.46264775e-02],
           [1.12264555e-01, 1.41793688e-01, 8.24203573e-02],
           [1.09916658e-01, 1.38069263e-01, 8.02029367e-02],
           [1.07537389e-01, 1.34340566e-01, 7.79739464e-02],
           [1.05126193e-01, 1.30607176e-01, 7.57330946e-02],
           [1.02682472e-01, 1.26868651e-01, 7.34800649e-02],
           [1.00205611e-01, 1.23124517e-01, 7.12145380e-02],
           [9.76949429e-02, 1.19374280e-01, 6.89361610e-02],
           [9.51497069e-02, 1.15617435e-01, 6.66444981e-02],
           [9.25691182e-02, 1.11853440e-01, 6.43391082e-02],
           [8.99523362e-02, 1.08081719e-01, 6.20195101e-02],
           [8.72985443e-02, 1.04301626e-01, 5.96852809e-02],
           [8.46067201e-02, 1.00512538e-01, 5.73357842e-02],
           [8.18758061e-02, 9.67137737e-02, 5.49703670e-02],
           [7.91048135e-02, 9.29045425e-02, 5.25885051e-02],
           [7.62924351e-02, 8.90841048e-02, 5.01893025e-02],
           [7.34374822e-02, 8.52515715e-02, 4.77720654e-02],
           [7.05385097e-02, 8.14060597e-02, 4.53357980e-02],
           [6.75941175e-02, 7.75465443e-02, 4.28796310e-02],
           [6.46026202e-02, 7.36719955e-02, 4.04015700e-02],
           [6.15623519e-02, 6.97812216e-02, 3.79075483e-02],
           [5.84714214e-02, 6.58729633e-02, 3.54834537e-02],
           [5.53277713e-02, 6.19458450e-02, 3.31294679e-02],
           [5.21291979e-02, 5.79983378e-02, 3.08458359e-02],
           [4.88732946e-02, 5.40287551e-02, 2.86328144e-02],
           [4.55574343e-02, 5.00352225e-02, 2.64906900e-02],
           [4.21787151e-02, 4.60156603e-02, 2.44197435e-02],
           [3.87265867e-02, 4.19677314e-02, 2.24203048e-02],
           [3.53328926e-02, 3.78938314e-02, 2.04927853e-02],
           [3.20540618e-02, 3.39910022e-02, 1.86376369e-02],
           [2.88948643e-02, 3.03011133e-02, 1.68553982e-02],
           [2.58603328e-02, 2.68229445e-02, 1.51467259e-02],
           [2.29557838e-02, 2.35553694e-02, 1.35124230e-02],
           [2.01868579e-02, 2.04973625e-02, 1.19535320e-02],
           [1.75594949e-02, 1.76480623e-02, 1.04712226e-02],
           [1.50800242e-02, 1.50067619e-02, 9.06703599e-03],
           [1.27551680e-02, 1.25729757e-02, 7.74287416e-03],
           [1.05920860e-02, 1.03464998e-02, 6.50109923e-03],
           [8.59843551e-03, 8.32749067e-03, 5.34469737e-03],
           [6.78244118e-03, 6.51658762e-03, 4.27742942e-03],
           [5.15300998e-03, 4.91508335e-03, 3.30406568e-03],
           [3.71991476e-03, 3.52517839e-03, 2.43074812e-03],
           [2.49411356e-03, 2.35039569e-03, 1.66546910e-03],
           [1.48835803e-03, 1.39629209e-03, 1.01895103e-03],
           [7.18499856e-04, 6.71880741e-04, 5.06254539e-04],
           [2.06971679e-04, 1.93192112e-04, 1.50637801e-04],
           [0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.37999545e-04, 1.78676061e-04, 1.72860770e-04],
           [8.43741397e-04, 6.13721803e-04, 5.91827044e-04],
           [1.78351929e-03, 1.26017469e-03, 1.21163590e-03],
           [3.04723305e-03, 2.09697799e-03, 2.01086376e-03],
           [4.63081615e-03, 3.11039365e-03, 2.97549545e-03],
           [6.53327676e-03, 4.29023234e-03, 4.09511093e-03],
           [8.75485908e-03, 5.62859674e-03, 5.36166775e-03],
           [1.12970363e-02, 7.11894739e-03, 6.76850770e-03],
           [1.41618912e-02, 8.75578575e-03, 8.31005892e-03],
           [1.73517777e-02, 1.05344430e-02, 9.98162922e-03],
           [2.08699220e-02, 1.24506569e-02, 1.17789272e-02],
           [2.47190142e-02, 1.45009078e-02, 1.36984892e-02],
           [2.89029779e-02, 1.66817013e-02, 1.57368344e-02],
           [3.34248333e-02, 1.89902255e-02, 1.78912594e-02],
           [3.82887520e-02, 2.14235822e-02, 2.01589341e-02],
           [4.33836197e-02, 2.39793789e-02, 2.25376062e-02],
           [4.84395959e-02, 2.66551766e-02, 2.50249583e-02],
           [5.34625588e-02, 2.94488832e-02, 2.76190695e-02],
           [5.84560924e-02, 3.23583986e-02, 3.03180072e-02],
           [6.34230572e-02, 3.53818739e-02, 3.31201276e-02],
           [6.83662555e-02, 3.85174403e-02, 3.60237674e-02],
           [7.32878717e-02, 4.17293732e-02, 3.90275555e-02],
           [7.81902682e-02, 4.48941060e-02, 4.20821613e-02],
           [8.30750083e-02, 4.80192878e-02, 4.50891614e-02],
           [8.79442864e-02, 5.11066838e-02, 4.80596246e-02],
           [9.27990328e-02, 5.41584545e-02, 5.09958619e-02],
           [9.76415062e-02, 5.71758291e-02, 5.38991425e-02],
           [1.02472156e-01, 6.01607894e-02, 5.67716105e-02],
           [1.07292890e-01, 6.31143596e-02, 5.96143413e-02],
           [1.12104346e-01, 6.60380837e-02, 6.24290100e-02],
           [1.16907679e-01, 6.89330839e-02, 6.52168297e-02],
           [1.21704073e-01, 7.18003336e-02, 6.79788600e-02],
           [1.26493885e-01, 7.46411481e-02, 7.07165455e-02],
           [1.31278653e-01, 7.74560824e-02, 7.34305034e-02],
           [1.36058587e-01, 8.02463333e-02, 7.61220603e-02],
           [1.40834424e-01, 8.30127212e-02, 7.87921356e-02],
           [1.45607388e-01, 8.57557098e-02, 8.14412721e-02],
           [1.50377469e-01, 8.84763894e-02, 8.40706897e-02],
           [1.55145490e-01, 9.11753135e-02, 8.66810358e-02],
           [1.59912356e-01, 9.38529235e-02, 8.92728467e-02],
           [1.64678086e-01, 9.65101178e-02, 9.18471425e-02],
           [1.69443296e-01, 9.91474007e-02, 9.44045305e-02],
           [1.74208978e-01, 1.01765003e-01, 9.69453396e-02],
           [1.78975015e-01, 1.04363766e-01, 9.94705324e-02],
           [1.83741864e-01, 1.06944152e-01, 1.01980683e-01],
           [1.88510318e-01, 1.09506385e-01, 1.04476123e-01],
           [1.93280656e-01, 1.12050960e-01, 1.06957463e-01],
           [1.98053037e-01, 1.14578410e-01, 1.09425358e-01],
           [2.02827843e-01, 1.17089108e-01, 1.11880295e-01],
           [2.07605682e-01, 1.19583256e-01, 1.14322599e-01],
           [2.12386906e-01, 1.22061184e-01, 1.16752725e-01],
           [2.17171591e-01, 1.24523368e-01, 1.19171274e-01],
           [2.21960062e-01, 1.26970110e-01, 1.21578671e-01],
           [2.26752635e-01, 1.29401693e-01, 1.23975331e-01],
           [2.31549674e-01, 1.31818347e-01, 1.26361618e-01],
           [2.36351691e-01, 1.34220188e-01, 1.28737793e-01],
           [2.41158658e-01, 1.36607657e-01, 1.31104426e-01],
           [2.45970847e-01, 1.38980985e-01, 1.33461890e-01],
           [2.50788522e-01, 1.41340395e-01, 1.35810551e-01],
           [2.55611935e-01, 1.43686097e-01, 1.38150770e-01],
           [2.60441332e-01, 1.46018294e-01, 1.40482899e-01],
           [2.65276949e-01, 1.48337177e-01, 1.42807285e-01],
           [2.70119018e-01, 1.50642929e-01, 1.45124270e-01],
           [2.74967758e-01, 1.52935726e-01, 1.47434192e-01],
           [2.79823385e-01, 1.55215734e-01, 1.49737385e-01],
           [2.84686106e-01, 1.57483115e-01, 1.52034180e-01],
           [2.89556121e-01, 1.59738021e-01, 1.54324906e-01],
           [2.94433624e-01, 1.61980600e-01, 1.56609890e-01],
           [2.99318800e-01, 1.64210993e-01, 1.58889457e-01],
           [3.04211830e-01, 1.66429337e-01, 1.61163932e-01],
           [3.09112886e-01, 1.68635761e-01, 1.63433639e-01],
           [3.14022136e-01, 1.70830393e-01, 1.65698904e-01],
           [3.18939739e-01, 1.73013355e-01, 1.67960052e-01],
           [3.23865848e-01, 1.75184766e-01, 1.70217411e-01],
           [3.28800610e-01, 1.77344740e-01, 1.72471310e-01],
           [3.33744164e-01, 1.79493390e-01, 1.74722081e-01],
           [3.38696881e-01, 1.81630656e-01, 1.76969925e-01],
           [3.43658896e-01, 1.83756635e-01, 1.79215176e-01],
           [3.48630130e-01, 1.85871574e-01, 1.81458292e-01],
           [3.53610696e-01, 1.87975577e-01, 1.83699622e-01],
           [3.58600751e-01, 1.90068707e-01, 1.85939489e-01],
           [3.63600974e-01, 1.92150637e-01, 1.88177930e-01],
           [3.68610875e-01, 1.94221893e-01, 1.90415639e-01],
           [3.73630537e-01, 1.96282574e-01, 1.92652989e-01],
           [3.78660731e-01, 1.98332259e-01, 1.94889982e-01],
           [3.83701032e-01, 2.00371414e-01, 1.97127280e-01],
           [3.88751499e-01, 2.02400141e-01, 1.99365288e-01],
           [3.93812902e-01, 2.04417992e-01, 2.01604029e-01],
           [3.98884464e-01, 2.06425691e-01, 2.03844370e-01],
           [4.03967212e-01, 2.08422581e-01, 2.06086216e-01],
           [4.09060380e-01, 2.10409373e-01, 2.08330438e-01],
           [4.14164904e-01, 2.12385460e-01, 2.10577017e-01],
           [4.19279982e-01, 2.14351579e-01, 2.12826851e-01],
           [4.24406778e-01, 2.16306926e-01, 2.15079834e-01],
           [4.29544452e-01, 2.18252264e-01, 2.17336902e-01],
           [4.34693472e-01, 2.20187322e-01, 2.19598336e-01],
           [4.39854140e-01, 2.22111950e-01, 2.21864517e-01],
           [4.45026087e-01, 2.24026532e-01, 2.24136178e-01],
           [4.50209458e-01, 2.25931036e-01, 2.26413812e-01],
           [4.55404835e-01, 2.27825067e-01, 2.28697720e-01],
           [4.60611862e-01, 2.29708984e-01, 2.30988683e-01],
           [4.65830584e-01, 2.31582819e-01, 2.33287303e-01],
           [4.71061092e-01, 2.33446560e-01, 2.35594189e-01],
           [4.76303457e-01, 2.35300204e-01, 2.37909984e-01],
           [4.81557732e-01, 2.37143757e-01, 2.40235370e-01],
           [4.86823950e-01, 2.38977236e-01, 2.42571070e-01],
           [4.92102119e-01, 2.40800673e-01, 2.44917850e-01],
           [4.97392221e-01, 2.42614114e-01, 2.47276527e-01],
           [5.02694209e-01, 2.44417627e-01, 2.49647968e-01],
           [5.08008004e-01, 2.46211298e-01, 2.52033097e-01],
           [5.13334045e-01, 2.47994758e-01, 2.54432682e-01],
           [5.18671833e-01, 2.49768442e-01, 2.56847920e-01],
           [5.24021083e-01, 2.51532595e-01, 2.59279969e-01],
           [5.29382504e-01, 2.53286580e-01, 2.61729691e-01],
           [5.34755049e-01, 2.55031299e-01, 2.64198657e-01],
           [5.40139451e-01, 2.56766066e-01, 2.66687888e-01],
           [5.45534784e-01, 2.58491663e-01, 2.69199059e-01],
           [5.50941223e-01, 2.60207880e-01, 2.71733575e-01],
           [5.56358666e-01, 2.61914734e-01, 2.74293048e-01],
           [5.61786529e-01, 2.63612673e-01, 2.76879353e-01],
           [5.67224524e-01, 2.65301862e-01, 2.79494411e-01],
           [5.72672253e-01, 2.66982550e-01, 2.82140323e-01],
           [5.78129194e-01, 2.68655086e-01, 2.84819396e-01],
           [5.83594794e-01, 2.70319828e-01, 2.87534136e-01],
           [5.89068726e-01, 2.71976893e-01, 2.90287235e-01],
           [5.94549535e-01, 2.73627455e-01, 2.93081836e-01],
           [6.00036972e-01, 2.75271501e-01, 2.95921171e-01],
           [6.05529383e-01, 2.76910349e-01, 2.98808999e-01],
           [6.11025672e-01, 2.78544737e-01, 3.01749374e-01],
           [6.16524393e-01, 2.80175708e-01, 3.04746831e-01],
           [6.22023681e-01, 2.81804671e-01, 3.07806430e-01],
           [6.27521180e-01, 2.83433480e-01, 3.10933802e-01],
           [6.33014302e-01, 2.85064161e-01, 3.14135231e-01],
           [6.38499882e-01, 2.86699265e-01, 3.17417735e-01],
           [6.43974279e-01, 2.88341745e-01, 3.20789186e-01],
           [6.49432687e-01, 2.89995681e-01, 3.24258265e-01],
           [6.54869821e-01, 2.91665550e-01, 3.27834714e-01],
           [6.60278576e-01, 2.93357663e-01, 3.31528971e-01],
           [6.65651193e-01, 2.95078919e-01, 3.35352589e-01],
           [6.70978085e-01, 2.96838083e-01, 3.39317704e-01],
           [6.76247706e-01, 2.98646012e-01, 3.43436507e-01],
           [6.81447007e-01, 3.00515200e-01, 3.47720925e-01],
           [6.86561121e-01, 3.02460281e-01, 3.52181241e-01],
           [6.91574077e-01, 3.04497393e-01, 3.56824920e-01],
           [6.96469718e-01, 3.06643361e-01, 3.61655163e-01],
           [7.01232814e-01, 3.08914699e-01, 3.66669009e-01],
           [7.05850938e-01, 3.11325604e-01, 3.71857046e-01],
           [7.10315812e-01, 3.13886477e-01, 3.77203428e-01],
           [7.14624219e-01, 3.16602743e-01, 3.82687321e-01],
           [7.18778053e-01, 3.19474524e-01, 3.88285163e-01],
           [7.22783534e-01, 3.22497196e-01, 3.93973108e-01],
           [7.26649962e-01, 3.25662561e-01, 3.99728869e-01],
           [7.30388342e-01, 3.28960174e-01, 4.05533169e-01],
           [7.34010270e-01, 3.32378584e-01, 4.11369939e-01],
           [7.37527061e-01, 3.35906259e-01, 4.17226538e-01],
           [7.40949295e-01, 3.39532191e-01, 4.23093146e-01],
           [7.44286624e-01, 3.43246190e-01, 4.28962164e-01],
           [7.47547518e-01, 3.47039129e-01, 4.34828307e-01],
           [7.50739597e-01, 3.50902796e-01, 4.40687245e-01],
           [7.53869340e-01, 3.54830065e-01, 4.46536330e-01],
           [7.56942466e-01, 3.58814646e-01, 4.52373507e-01],
           [7.59964099e-01, 3.62850947e-01, 4.58197051e-01],
           [7.62938370e-01, 3.66934305e-01, 4.64006509e-01],
           [7.65869298e-01, 3.71060378e-01, 4.69800828e-01],
           [7.68760065e-01, 3.75225594e-01, 4.75579993e-01],
           [7.71613661e-01, 3.79426698e-01, 4.81343746e-01],
           [7.74432711e-01, 3.83660846e-01, 4.87092030e-01],
           [7.77219521e-01, 3.87925550e-01, 4.92824941e-01],
           [7.79976122e-01, 3.92218632e-01, 4.98542679e-01],
           [7.82704372e-01, 3.96538143e-01, 5.04245424e-01],
           [7.85406084e-01, 4.00882261e-01, 5.09933180e-01],
           [7.88082514e-01, 4.05249620e-01, 5.15606583e-01],
           [7.90735337e-01, 4.09638653e-01, 5.21265437e-01],
           [7.93365587e-01, 4.14048288e-01, 5.26910332e-01],
           [7.95974443e-01, 4.18477413e-01, 5.32541479e-01],
           [7.98563090e-01, 4.22924967e-01, 5.38158965e-01],
           [8.01132465e-01, 4.27390099e-01, 5.43763104e-01],
           [8.03683448e-01, 4.31872040e-01, 5.49354179e-01],
           [8.06216903e-01, 4.36370067e-01, 5.54932407e-01],
           [8.08733632e-01, 4.40883535e-01, 5.60498004e-01],
           [8.11234380e-01, 4.45411861e-01, 5.66051184e-01],
           [8.13719871e-01, 4.49954510e-01, 5.71592130e-01],
           [8.16190854e-01, 4.54510951e-01, 5.77120941e-01],
           [8.18647860e-01, 4.59080818e-01, 5.82637919e-01],
           [8.21091477e-01, 4.63663731e-01, 5.88143257e-01],
           [8.23522322e-01, 4.68259306e-01, 5.93637068e-01],
           [8.25941042e-01, 4.72867160e-01, 5.99119408e-01],
           [8.28347989e-01, 4.77487112e-01, 6.04590612e-01],
           [8.30743837e-01, 4.82118792e-01, 6.10050646e-01],
           [8.33128976e-01, 4.86762021e-01, 6.15499748e-01],
           [8.35503932e-01, 4.91416548e-01, 6.20937990e-01],
           [8.37869141e-01, 4.96082188e-01, 6.26365511e-01],
           [8.40225092e-01, 5.00758736e-01, 6.31782384e-01],
           [8.42572132e-01, 5.05446082e-01, 6.37188794e-01],
           [8.44910847e-01, 5.10143977e-01, 6.42584689e-01],
           [8.47241478e-01, 5.14852394e-01, 6.47970322e-01],
           [8.49564536e-01, 5.19571148e-01, 6.53345684e-01],
           [8.51880425e-01, 5.24300126e-01, 6.58710851e-01],
           [8.54189457e-01, 5.29039277e-01, 6.64065968e-01],
           [8.56492061e-01, 5.33788486e-01, 6.69411068e-01],
           [8.58788681e-01, 5.38547636e-01, 6.74746163e-01],
           [8.61079598e-01, 5.43316710e-01, 6.80071393e-01],
           [8.63365189e-01, 5.48095643e-01, 6.85386808e-01],
           [8.65645824e-01, 5.52884376e-01, 6.90692458e-01],
           [8.67921943e-01, 5.57682816e-01, 6.95988333e-01],
           [8.70193820e-01, 5.62490968e-01, 7.01274543e-01],
           [8.72461813e-01, 5.67308797e-01, 7.06551129e-01],
           [8.74726275e-01, 5.72136272e-01, 7.11818130e-01],
           [8.76987556e-01, 5.76973366e-01, 7.17075581e-01],
           [8.79246004e-01, 5.81820062e-01, 7.22323516e-01],
           [8.81501987e-01, 5.86676330e-01, 7.27561950e-01],
           [8.83755830e-01, 5.91542172e-01, 7.32790924e-01],
           [8.86007861e-01, 5.96417587e-01, 7.38010471e-01],
           [8.88258422e-01, 6.01302575e-01, 7.43220615e-01],
           [8.90507851e-01, 6.06197136e-01, 7.48421374e-01],
           [8.92756486e-01, 6.11101277e-01, 7.53612768e-01],
           [8.95004663e-01, 6.16015007e-01, 7.58794812e-01],
           [8.97252718e-01, 6.20938337e-01, 7.63967517e-01],
           [8.99500988e-01, 6.25871283e-01, 7.69130895e-01],
           [9.01749808e-01, 6.30813862e-01, 7.74284952e-01],
           [9.03999514e-01, 6.35766096e-01, 7.79429694e-01],
           [9.06250441e-01, 6.40728007e-01, 7.84565122e-01],
           [9.08502927e-01, 6.45699621e-01, 7.89691237e-01],
           [9.10757306e-01, 6.50680967e-01, 7.94808035e-01],
           [9.13013918e-01, 6.55672074e-01, 7.99915508e-01],
           [9.15273100e-01, 6.60672973e-01, 8.05013649e-01],
           [9.17535190e-01, 6.65683701e-01, 8.10102444e-01],
           [9.19800529e-01, 6.70704293e-01, 8.15181880e-01],
           [9.22069457e-01, 6.75734787e-01, 8.20251936e-01],
           [9.24342317e-01, 6.80775223e-01, 8.25312592e-01],
           [9.26619454e-01, 6.85825642e-01, 8.30363821e-01],
           [9.28901213e-01, 6.90886086e-01, 8.35405595e-01],
           [9.31187941e-01, 6.95956601e-01, 8.40437880e-01],
           [9.33479990e-01, 7.01037232e-01, 8.45460640e-01],
           [9.35777709e-01, 7.06128027e-01, 8.50473834e-01],
           [9.38081453e-01, 7.11229033e-01, 8.55477417e-01],
           [9.40391578e-01, 7.16340301e-01, 8.60471340e-01],
           [9.42708444e-01, 7.21461881e-01, 8.65455547e-01],
           [9.45032411e-01, 7.26593827e-01, 8.70429980e-01],
           [9.47363845e-01, 7.31736190e-01, 8.75394575e-01],
           [9.49703113e-01, 7.36889025e-01, 8.80349262e-01],
           [9.52050586e-01, 7.42052388e-01, 8.85293966e-01],
           [9.54406641e-01, 7.47226332e-01, 8.90228605e-01],
           [9.56771640e-01, 7.52410923e-01, 8.95153097e-01],
           [9.59145966e-01, 7.57606219e-01, 9.00067348e-01],
           [9.61530016e-01, 7.62812270e-01, 9.04971253e-01],
           [9.63924184e-01, 7.68029136e-01, 9.09864706e-01],
           [9.66328868e-01, 7.73256875e-01, 9.14747590e-01],
           [9.68744470e-01, 7.78495545e-01, 9.19619782e-01],
           [9.71171399e-01, 7.83745204e-01, 9.24481152e-01],
           [9.73610056e-01, 7.89005920e-01, 9.29331562e-01],
           [9.76060827e-01, 7.94277767e-01, 9.34170872e-01],
           [9.78524185e-01, 7.99560782e-01, 9.38998912e-01],
           [9.81000569e-01, 8.04855022e-01, 9.43815515e-01],
           [9.83490426e-01, 8.10160543e-01, 9.48620503e-01]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.watermelon', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)