import streamlit as st

st.title("Profil d'investisseur")

st.write("Cette application vous permettra de connaître quel type d'investisseur vous êtes.")

q1_options = ['Une personne qui aime parier', 'Une personne qui est prête à prendre des risques après avoir effectué une certaine recherche', 'Une personne prudente', 'Une personne qui évite systématiquement le risque']
q1 = st.selectbox('En général, comment votre meilleur ami vous décrirait-il en tant que personne qui prend des risques?', q1_options)
q2_options = ['1 000 $ en argent', 'Une chance sur deux de remporter 5 000 $', 'Une chance sur quatre de remporter 10 000 $', 'Une chance sur 20 de remporter 100 000 $']
q2 = st.selectbox('Vous participez à un jeu-questionnaire télévisé et vous pouvez choisir une option parmi les suivantes. Laquelle prendriez-vous?',q2_options)
q3_options  = ['Annuler vos vacances', 'Prendre des vacances beaucoup moins coûteuses', 'Partir comme prévu, en vous disant que vous avez besoin de temps pour vous préparer à la recherche d\'un nouvel emploi','Prolonger vos vacances, puisqu il s\'agit peut-être de votre dernière chance de partir en première classe']
q3 = st.selectbox('Vous avez enfin épargné l\'argent qu\'il vous fallait pour prendre les « vacances de votre vie ». Trois semaines avant votre départ, vous perdez votre boulot. Vous prenez une des décisions suivantes :', q3_options)
q4_options = ['Vous les déposeriez dans un compte bancaire ou un compte du marché monétaire?', 'Vous les investiriez dans des obligations de premier rang ou dans des fonds communs obligataires', 'Vous les placeriez dans des actions ou dans des fonds communs']
q4 = st.selectbox('Si vous receviez soudainement 20 000 $ pour investir, que feriez-vous?', q4_options)
q5_options = ['Pas du tout à l\'aise', 'Plutôt à l\'aise', 'Très à l\'aise']
q5 = st.selectbox('Relativement à votre expérience, jusqu\'à quel point êtes-vous à l\'aise d investir dans des titres boursiers ou des fonds communs?',q5_options)
q6_options = ['Perte', 'Incertitude', 'Avantage', 'Frissons']
q6 = st.selectbox('Quand vous pensez au mot « risque », lequel des mots suivants vous vient immédiatement en tête?', q6_options)
q7_options = ['Vous conservez les obligations', 'Vous vendez vos obligations, placez la moitié des profits dans des comptes du marché monétaire, et l\'autre moitié dans des biens durables', 'Vous vendez vos obligations et placez la totalité des profits dans des biens durables','Vous vendez vos obligations, placez l\'argent obtenu dans des biens durables et empruntez davantage pour en acheter plus']
q7 = st.selectbox('Certains spécialistes prévoient que le cours de certains actifs comme l\'or, les bijoux, les articles de collection et l\'immobilier (biens durables) augmenteront de valeur. Le cours des obligations risque de baisser; toutefois, les spécialistes s\'accordent sur le fait que les obligations du gouvernement sont relativement sécuritaires. La plupart de vos placements sont actuellement dans des obligations gouvernementales à fort intérêt. Que faites-vous?', q7_options)
q8_options = ['Dans le meilleur cas, vous gagnez 200 $; dans le pire cas, vous perdez 0 $', 'Vous gagnez 800 $ dans le meilleur cas; dans le pire cas, vous perdez 200 $', 'Vous gagnez 2 600 $ dans le meilleur cas; dans le pire cas, vous perdez 800 $', 'Dans le meilleur cas, vous gagnez 4 800 $; dans le pire cas, vous perdez 2 400 $']
q8 = st.selectbox('Lequel des quatre scénarios de placement ci-dessous choisiriez-vous?', q8_options)
q9_options = ['Un gain assuré de 500$', '50 % des chances de gagner 1 000 $ et 50 % des chances de ne rien gagner.']
q9 = st.selectbox('En plus de ce que vous possédez déjà, on vous a donné 1 000 $. On vous demande maintenant de choisir entre :', q9_options)
q10_options = ['Une perte assurée de 500 $', '50 % des chances de perdre 1 000 $ et 50 % des chances de ne rien perdre']
q10 = st.selectbox('En plus de ce que vous possédez déjà, on vous a donné 2 000 $. On vous demande maintenant de choisir entre :', q10_options)
q11_options = ['Un compte d\'épargne ou un fonds du marché monétaire', 'Un fonds commun qui possède à la fois des actions et des obligations', 'Un portefeuille de 15 actions ordinaires', 'Des biens comme l\'or, l\'argent et le gaz']
q11 = st.selectbox('Supposons qu\'un de vos parents vous laisse un héritage de 100 000 $, stipulant dans son testament que devez investir TOUTE cette somme dans UN des outils suivants. Lequel choisissez-vous?',q11_options)
q12_options = ['60 % dans des placements à faible risque, 30 % dans des placements à risque moyen, 10 % dans des placements à risque élevé', '30 % dans des placements à faible risque, 40 % dans des placements à risque moyen, 30 % dans des placements à risque élevé', '10 % dans des placements à faible risque, 40 % dans des placements à risque moyen, 50 % dans des placements à risque élevé']
q12 = st.selectbox('Si vous aviez à investir 20 000 $, laquelle des options de placement suivantes trouveriez-vous la plus attirante?', q12_options)
q13_options = ['Rien', 'Un mois de salaire', 'Trois mois de salaire', 'Six mois de salaire']
q13 = st.selectbox('Votre grand ami et voisin, un géologue d expérience, rassemble un groupe d\'investisseurs pour financer une entreprise d\'exploitation aurifère. L\'entreprise pourrait rapporter de 50 à 100 fois l\'investissement si elle réussit. Si l\'entreprise échoue, l\'investissement au complet sera englouti. Votre ami estime que les chances de succès ne sont que de 20 %. Si vous aviez de l\'argent, combien investiriez-vous?',q13_options)

total = 0
if(q1 == q1_options[0]):
    total += 4
elif(q1 == q1_options[1]):
    total += 3
elif(q1 == q1_options[2]):
    total += 2
elif(q1 == q1_options[3]):
    total += 1
if(q2 == q2_options[0]):
    total += 1
elif(q2 == q2_options[1]):
    total += 2
elif(q2 == q2_options[2]):
    total += 3
elif(q2 == q2_options[3]):
    total += 4
if(q3 == q3_options[0]):
    total += 1
elif(q3 == q3_options[1]):
    total += 2
elif(q3 == q3_options[2]):
    total += 3
elif(q3 == q3_options[3]):
    total += 4
if(q4 == q4_options[0]):
    total += 1
elif(q4 == q4_options[1]):
    total += 2
elif(q4 == q4_options[2]):
    total += 3
if(q5 == q5_options[0]):
    total += 1
elif(q5 == q5_options[1]):
    total += 2
elif(q5 == q5_options[2]):
    total += 3
if(q6 == q6_options[0]):
    total += 1
elif(q6 == q6_options[1]):
    total += 2
elif(q6 == q6_options[2]):
    total += 3
elif(q6 == q6_options[3]):
    total += 4
if(q7 == q7_options[0]):
    total += 1
elif(q7 == q7_options[1]):
    total += 2
elif(q7 == q7_options[2]):
    total += 3
elif(q7 == q7_options[3]):
    total += 4
if(q8 == q8_options[0]):
    total += 1
elif(q8 == q8_options[1]):
    total += 2
elif(q8 == q8_options[2]):
    total += 3
elif(q8 == q8_options[3]):
    total += 4
if(q9 == q9_options[0]):
    total += 1
elif(q9 == q9_options[1]):
    total += 3
if(q10 == q10_options[0]):
    total += 1
elif(q10 == q10_options[1]):
    total += 3
if(q11 == q11_options[0]):
    total += 1
elif(q11 == q11_options[1]):
    total += 2
elif(q11 == q11_options[2]):
    total += 3
elif(q11 == q11_options[3]):
    total += 4
if(q12 == q12_options[0]):
    total += 1
elif(q12 == q12_options[1]):
    total += 2
elif(q12 == q12_options[2]):
    total += 3
if(q13 == q13_options[0]):
    total += 1
elif(q13 == q13_options[1]):
    total += 2
elif(q13 == q13_options[2]):
    total += 3
elif(q13 == q13_options[3]):
    total += 4


st.write(str(total))

if total >= 33 :
    st.write('Votre profil d\'investisseur est élevé et vous devriez investir à 30% en revenu fixe et 70% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/performance/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA9fBn7jWPmVUEhn8s82LF2Do38bF-J828jptXJaoUCmzCqlC4_xaZhoCBlMQAvD_BwE&gclsrc=aw.ds')
elif total >= 29 and total <= 32 :
    st.write ('Votre profil d\'investisseur est au-dessus de la moyenne et vous devriez investir à 40% en revenu fixe et 60% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/performance/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA9fBn7jWPmVUEhn8s82LF2Do38bF-J828jptXJaoUCmzCqlC4_xaZhoCBlMQAvD_BwE&gclsrc=aw.ds')
elif total >= 23 and total <= 28 :
    st.write ('Votre profil d\'investisseur est moyen ou modéré et vous devriez investir à 50% en revenu fixe et 50% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/information/ir/produits-investissement-responsable/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA5egh5C9ZVLD25hsix21YpXkfZDK6cEgm6y35LKPp7vi4Bb03VrSlhoCoYoQAvD_BwE&gclsrc=aw.ds')
elif total >= 19 and total <= 22 :
    st.write ('Votre profil d\'investisseur est en dessous de la moyenne et vous devriez investir à 60% en revenu fixe et 40% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/information/ir/produits-investissement-responsable/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA5egh5C9ZVLD25hsix21YpXkfZDK6cEgm6y35LKPp7vi4Bb03VrSlhoCoYoQAvD_BwE&gclsrc=aw.ds')
elif total >= 16 and total <= 18 :
    st.write ('Votre profil d\'investisseur est faible et vous devriez investir à 70% en revenu fixe et 30% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/information/ir/produits-investissement-responsable/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA5egh5C9ZVLD25hsix21YpXkfZDK6cEgm6y35LKPp7vi4Bb03VrSlhoCoYoQAvD_BwE&gclsrc=aw.ds')
elif total >= 11 and total <= 15 :
    st.write ('Votre profil d\'investisseur est faible et vous devriez investir à 80% en revenu fixe et 20% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/faible-risque/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA4eGAFtuyT4P5U78LUcZQ7V1cCcDgHboDoCMhRumhMc9GoogAxIfWxoC_b0QAvD_BwE&gclsrc=aw.ds')
elif total >= 10 :
    st.write ('Votre profil d\'investisseur est faible et vous devriez investir à 100% en revenu fixe et 0% en titre de croissance. Voici dans quelques fonds que vous pourriez investir chez Desjardins : https://www.desjardins.com/particuliers/epargne-placements/fonds-communs-placement/fonds-desjardins/faible-risque/?utm_id=e-gp-0-132972177091&campagne=e-gp-0-132972177091&gclid=CjwKCAjwitShBhA6EiwAq3RqA4eGAFtuyT4P5U78LUcZQ7V1cCcDgHboDoCMhRumhMc9GoogAxIfWxoC_b0QAvD_BwE&gclsrc=aw.ds')
