# # ### text sentiment analysis

# # # https://www.edenai.co/post/top-10-sentiment-analysis-apis
# # # https://app.edenai.run/bricks/text/sentiment-analysis#live-testing

# import json
# import requests

# headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjI3ODQwYjUtY2IxOC00MGFmLWE5NmEtYWMzNzNjMzAxMDBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.sJnkDP04P0fnK0Bd_ayFkEpFMM0gM9GdM8MR9LwsLG0"}

# url ="https://api.edenai.run/v2/text/sentiment_analysis"
# text = "I'm happy to tell you that I have a baby"
# payload={"providers": "google", 'language': "en", 'text': text}

# response = requests.post(url, json=payload, headers=headers)

# result = json.loads(response.text)
# x= result['google']['items']
# print(x.sentiment)

# # ###package snscrape.modules.twitter as sntwitter

# # #Pour requeter les n tweets sur twitter avec une query définie

# # from ast import NotIn
# # from stop_words import get_stop_words

# # ##pour ajouter des appax
# # stop_words=get_stop_words("fr")
# # ma_list = ["c'est", "est","j'ai","ça", "ca", "après", "qu'"]
# # for mot in ma_list:
# #     if mot not in stop_words:
# #         stop_words.append(mot)

# # # print(stop_words)

# import requests

# url = "https://sentiment-analysis4.p.rapidapi.com/reviews"

# payload = {"text": "bought as a gift for my son's family, nice laptop especially for the price!"}
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "fcc0d0a037msh068becd35422b9ep1d39a3jsnc9d49376520b",
# 	"X-RapidAPI-Host": "sentiment-analysis4.p.rapidapi.com"
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# # print(response.text)

# import requests

# url = "https://api.apilayer.com/sentiment/analysis"

# payload = "Mes chers compatriotes de métropole, d’outre-mer et de l’étranger,".encode("utf-8")
# headers= {
#   "apikey": "qGHUb2OdRSWW9sY5cYx4CpwF4THQJnBB"
# }

# response = requests.request("POST", url, headers=headers, data = payload)

# status_code = response.status_code
# result = response.text

# print(result)

# text = "À nouveau, cette dernière soirée de l’année est marquée par l’épidémie et les contraintes renforcées qui pèsent sur notre quotidien. Alors en ce moment, j’ai avant tout une pensée pour nos 123 000 compatriotes à qui le virus a enlevé la vie. Une pensée pour tous ceux qui traversent ce moment dans le deuil, la peine ou la solitude."
# text_filtre = text[:10]


# def text_limit(text):
#     return text[:10]

# print(text_limit(text))


# import requests
# import json
# import lorem
# import lorem_text
# from lorem_text import lorem

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjI3ODQwYjUtY2IxOC00MGFmLWE5NmEtYWMzNzNjMzAxMDBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.sJnkDP04P0fnK0Bd_ayFkEpFMM0gM9GdM8MR9LwsLG0"}
text_only_limited = "  Françaises, Français,  Mes chers compatriotes de métropole, d’outre-mer et de l’étranger,  À nouveau, cette dernière soirée de l’année est marquée par l’épidémie et les contraintes renforcées qui pèsent sur notre quotidien. Alors en ce moment, j’ai avant tout une pensée pour nos 123 000 compatriotes à qui le virus a enlevé la vie. Une pensée pour tous ceux qui traversent ce moment dans le deuil, la peine ou la solitude.  Je n’oublie pas non plus ceux d’entre vous qui sont touchés par le COVID long comme ceux qui subissent les conséquences psychologiques de la crise sanitaire.  Je veux ce soir, une fois encore, en votre nom à tous, témoigner notre reconnaissance pour nos personnels soignants, nos armées, nos forces de l’ordre, nos sapeurs-pompiers, nos auxiliaires de vie nos aides à domicile et tant d’autres professions, tous engagés ce 31 décembre comme chaque jour pour nous protéger, pour prendre soin de nous.  Les semaines à venir seront difficiles nous le savons tous : le virus circule et circulera de plus en plus, des mesures ont été prises par le gouvernement pour y faire face et je vous demande à tous et toute d’y veiller, des secteurs comme la culture, le sport, la restauration, l’hôtellerie, le tourisme, ou l’événementiel vont à nouveau subir les conséquences économiques de cette situation. Nous les aiderons comme il se doit et comme nous le faisons depuis le début de cette pandémie.  Il y aura aussi nombre de nos activités désorganisées en raison de ce nouveau variant si contagieux. Nous veillerons dans ce contexte à assurer la continuité des services publics et de la vie de la Nation. Mais par rapport au même moment l’année dernière où les contraintes étaient beaucoup plus fortes, nous avons pour nous l’arme du vaccin, et les acquis de notre expérience collective. Et donc de vraies raisons d’espérer.  Nous sommes ce soir au moment où je vous parle plus de 53 millions à être totalement vaccinés, ce qui place notre pays dans le peloton de tête mondial. Nous sommes 24 millions à avoir reçu une dose de rappel et notre objectif est de permettre à chacun d’être vacciné et de faire son rappel.  Nous pourrons ainsi surmonter cette vague en limitant au maximum les restrictions. En continuant comme nous l’avons fait depuis le début, de tout faire pour préserver l’activité et ce que nous avons de plus précieux, c’est à dire l’école, l’éducation de nos enfants.  Alors ce soir, je veux le redire avec beaucoup de forces et de convictions : la vaccination est notre plus sûr atout. Elle réduit fortement la transmission, elle divise par 10 le nombre des formes graves. C’est pour cela qu’une nouvelle fois, j’en appelle aux 5 millions de non-vaccinés. Faites ce geste simple. Pour vous. Pour vos compatriotes. Pour notre pays. Tout la France compte sur vous.  La vaccination est-elle seule suffisante ? Non. C’est pour cela que le respect des gestes barrière contre le virus demeure essentiel, en particulier le port du masque.  Tous ensemble, nous allons donc traverser cette nouvelle épreuve en suivant les mêmes principes que depuis le premier jour.  D’abord nous protéger. Protéger les plus vulnérables, protéger nos hôpitaux et nos soignants, qui sont sous forte pression alors même qu’il faut soigner les autres maladies. Protéger aussi notre économie, et nos emplois, comme nous l’avons fait avec le « quoi qu’il en coûte ».  Ensuite nous attacher, sur la base des faits et de la science, à prendre des mesures proportionnées. C’est exactement ce que le Premier ministre et les ministres ont fait ces derniers jours. Tout faire pour éviter de prendre des restrictions qui pèsent sur nos libertés et veiller à respecter tous nos principes démocratiques.  Enfin, nous appuyer sur la responsabilité de chacun, principalement en se faisant vacciner, pour soi et pour les autres. Être un citoyen libre et toujours être un citoyen responsable pour soi et pour autrui ; les devoirs valent avant les droits.  Un autre motif d’espoir est que, malgré l’épreuve sanitaire, malgré la fatigue, la lassitude, notre pays continue à avancer. Nous n’avons cessé d’œuvrer pour attirer des entreprises et des investissements, ouvrir des usines, créer des emplois. Jamais depuis quinze ans, le chômage n’avait été aussi bas. La réindustrialisation de notre pays est bien une réalité.  Nous avons protégé les travailleurs, aidé les plus modestes d’entre nous, nous avons investi pour défendre la dignité de nos compatriotes en situation de handicaps, pris des mesures et des décisions claires pour mieux protéger nos enfants, accompagner nos aînés.  Nous avons formé notre jeunesse. En effet, qui aurait pensé que nous serions capables en cinq ans de doubler le nombre de nos apprentis : près de 700 000 apprentis ces douze derniers mois. Que nous saurions inventer un programme, « 1 jeune 1 solution », qui a accompagné en un an et demi plus de 3 millions de Français vers l’emploi ou la formation.   Là où nous aurions pu tout reporter, nous n’avons jamais renoncé à notre ambition collective.  Le travail avec la réforme de l’assurance chômage, le contrat d’engagement jeunes qui sera mis en œuvre au début du mois de mars prochain ; le pouvoir d’achat avec l’indemnité inflation, le chèque énergie, l’augmentation des salaires des fonctionnaires les plus modestes ;  l’urgence écologique et climatique avec le renouvellement de notre parc automobile, le développement des énergies renouvelables, les rénovations thermiques de logements et au 1er janvier la fin des emballages plastique comme de nouvelles mesures inédites pour le bien-être de nos animaux. Notre agriculture avec l’assurance récolte, la retraite minimale à 1000 euros ; le déploiement de 2000 maisons France services, le versement automatique des pensions alimentaires qui bénéficiera notamment aux mères seules ; la gratuité de la contraception pour les femmes jusqu’à 25 ans  ; et la réforme de l’Etat, de notre Haute Fonction publique avec entre autres la création de l’Institut National du Service Public, rien que ces dernières semaines et dans les prochains mois, des décisions dont on parlait parfois depuis des décennies, que je viens à la cavalcade ici d’essayer de rassembler ont été prises et seront prises qui changeront la vie.   La France, malgré les épreuves est donc plus forte aujourd’hui qu’il y a deux ans.  Tout cela, c’est grâce à vous, grâce à nous tous, grâce à notre esprit de résistance, notre solidarité notre civisme, notre engagement et notre esprit d’entreprendre.  Alors au moment où je m’exprime devant vous ce soir, je veux vous dire que je suis résolument optimiste pour l’année qui vient. Optimiste pour notre Nation pas simplement pour 2022, mais pour les années qui viennent. Car l’ambition et la solidarité dont nous n’avons cessé de faire preuve nous autorisent tous les espoirs. 2022 peut être sera l’année de sortie de l’épidémie, je veux le croire avec vous ; l’année où nous pouvons voir l’issue de ce jour sans fin.  Dans notre pays, en déployant ces campagnes de rappel et en nous organisant comme il se doit pour domestiquer le virus et écraser sa diffusion. Et au niveau mondial en agissant pour vacciner l’humanité. La France qui, dès avril 2020, a été à l’initiative des dons de doses aux pays pauvres, et nous seront au rendez-vous pour amplifier l’effort et ainsi permettre d’entrevoir la fin de ce virus sous sa forme aigue. 2022 doit être l’année d’un tournant européen.  Notre continent a été tant décrié ces dernières années. On l’a dit divisé, incapable de projets collectifs, en train de sortir de l’Histoire.  Alors même que nous célébrons les 20 ans de la mise en circulation de l’euro notre monnaie commune qui nous aura donné une stabilité monétaire, une place internationale inédites, la crise a démontré qu’unie, notre Europe pouvait être non seulement utile, mais porteuse d’espérance pour tous.  Sans l’Europe nous n’aurions pas aujourd’hui de vaccin disponible en nombre, y compris pour organiser des campagnes de rappel.  Sans l’Europe, nous n’aurions pas pu bâtir partout à travers notre continent des plans de relance parmi les plus ambitieux au monde et connaître les résultats économiques – croissance, créations d’emplois que nous connaissons.  Alors à partir de minuit, la France prendra la Présidence de l’Union Européenne et vous pouvez compter sur mon engagement total pour faire de ce moment, qui ne survient qu’une fois tous les 13 ans, un temps de progrès pour vous. Un temps de progrès pour la maîtrise de nos frontières, notre défense, la transition climatique, l’égalité entre les femmes et les hommes, la construction d’une alliance nouvelle avec le continent africain, le meilleur encadrement des grandes plateformes de l’internet, et la culture en Europe.  Oui les valeurs que porte notre Union - la démocratie, l’équilibre entre liberté et solidarité, une certaine idée de l’Homme – sont, j’en suis convaincu, celles qui permettront de relever nos défis contemporains. Et notre Europe est bien le seul chemin par lequel la France sera plus forte face aux fracas du monde et des grandes puissances. 2022 sera pour la France une année décisive.  Une année d’action, encore et toujours. Fort de votre confiance, j’agirai jusqu’au dernier jour du mandat pour lequel vous m’avez élu. Bien sûr pour tenir le cap et prendre toutes les décisions nécessaires face à l’épidémie. Et nous aurons aussi à préparer l’avenir, en déployant le plan d’investissement France 2030 qui vise à la fois à faire de nous une Nation forte sur les technologies du futur et à nous rendre plus indépendants. Nous aurons à investir plus fortement encore que nous ne l’avons fait dans l’éducation, la recherche publique, la santé, la culture et l’inclusion de tous les Français.  Nous aurons à prendre de nouvelles décisions pour lutter contre l’islamisme radical, renforcer l’ordre, la sécurité et la tranquillité de tous, pour mieux vous protéger.  Nous aurons à prendre de nouveaux choix industriels en particulier en matière d’énergie, inédit, afin de tenir nos engagements climatiques. 2022 sera une année d’élection, enfin.  Nous aurons à élire au printemps prochain le Président de la République, puis à désigner nos représentants à l’Assemblée nationale. Malgré la pandémie, ces scrutins essentiels devront se dérouler dans les meilleures conditions possibles et toutes les sensibilités politiques du pays doivent y œuvrer. J’y veillerai tout particulièrement.  Nous aurons donc cette année des choix majeurs à faire pour notre Nation. Ces choix, nous les ferons avec la conviction que la France a un chemin singulier, unique, à poursuivre. Nous les ferons, je le sais, en étant fidèles à l’esprit de résistance, l’esprit de tolérance et le choix de notre avenir commun qui nous ont toujours inspiré. Pour ma part, quelle que soit ma place et les circonstances, je continuerai à vous servir. Et de la France, notre patrie, nul ne saura déraciner mon cœur.    Mes chers compatriotes,  J’ai travaillé et nous avons travaillé sans relâche depuis bientôt cinq ans afin que la France soit écoutée et respectée en Europe et dans le concert des Nations. Elle l’est.  À faire progresser notre pays dans l’unité aussi. Chemin bien difficile car il est si aisé d’opposer les générations, les catégories sociales, les origines, les territoires. Mais chemin nécessaire car lorsqu’il est rassemblé, rien ne peut résister au peuple français.  En vous souhaitant ce soir une année pleine de bonheur et d’accomplissements personnels, je forme donc pour nous tous ce vœu : continuons à respecter nos différences, à avoir confiance en ce que nous sommes, à regarder avec courage, audace et lucidité notre avenir pour agir. Décidons pour nous-même d’être tout à la fois enracinés dans notre langue, notre culture, notre laïcité. Et épris de liberté, d’universel, de créativité.  Restons unis, bienveillants, solidaires. Restons du côté de la vie. C’est là, ce que nous nous devons à nous-mêmes.  Alors, 2022 sera l’année de tous les possibles.  Vive notre Europe. Vive la République.  Vive la France. "
# def get_api(text_only_limited, lang):
#     headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjI3ODQwYjUtY2IxOC00MGFmLWE5NmEtYWMzNzNjMzAxMDBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.sJnkDP04P0fnK0Bd_ayFkEpFMM0gM9GdM8MR9LwsLG0"}
#     lang = "fr"
#     url ="https://api.edenai.run/v2/text/sentiment_analysis"
#     payload={"providers": "amazon", 'language': lang, 'text': text_only_limited}

#     response = requests.post(url, json=payload, headers=headers)
#     result = json.loads(response.text)
#     n = len(text_only_limited)
#     if n >= 4000:
#         text_only_limited = text_only_limited[:4000]

#     if result['amazon']['status'] == 'fail':
#         for i in range(20):
#             n -= 1000
#             text_only_limited = text_only_limited[:n]
#             payload={"providers": "amazon", 'language': lang, 'text': text_only_limited}
#             response = requests.post(url, json=payload, headers=headers)
#             result = json.loads(response.text)
#             # print(n)
#             if result['amazon']['status'] != 'fail':
#                 return(result['amazon']['items'])
#                 break

# print(get_api(text_only_limited, "fr"))









###__________________Appel de l'API analyse de sentiments__________________###
#     headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjI3ODQwYjUtY2IxOC00MGFmLWE5NmEtYWMzNzNjMzAxMDBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.sJnkDP04P0fnK0Bd_ayFkEpFMM0gM9GdM8MR9LwsLG0"}
#     lang = "fr"
#     url ="https://api.edenai.run/v2/text/sentiment_analysis"
#     payload={"providers": "amazon", 'language': lang, 'text': text_only}

    
#     response = requests.post(url, json=payload, headers=headers)
#     result = json.loads(response.text)
#     n = len(text_only)
#     if n >= 4000:
#         text_only = text_only[:4000]

#     if result['amazon']['status'] == 'fail':
#         for i in range(20):
#             n -= 1000
#             text_only = text_only[:n]
#             payload={"providers": "amazon", 'language': lang, 'text': text_only}
#             response = requests.post(url, json=payload, headers=headers)
#             result = json.loads(response.text)
#             if result['amazon']['status'] != 'fail':
#                 break
#     x = result['amazon']['items']

# #Création dataframe du résultat de l'API
#     api_dico = {}
#     for i in range(len(x)):
#         api_dico[x[i]['sentiment']] = round(x[i]['sentiment_rate'],4)*100

#     api_df = pd.DataFrame(list(api_dico.items()), columns=['sentiment', 'sentiment_rate'])

# ###__________________Mise en forme du graphique de l'analyse sentimentale__________________###
#     labels = api_df['sentiment'].tolist()
#     data = api_df['sentiment_rate'].tolist()


#     #Supression sentiment Mixed
#     labels.remove('Mixed')
#     del data[-1]




#########################################################################
#                          language detector                            #
#########################################################################

# import langid  #for language detect
# def language_detector(text):
#     return langid.classify(text)[0]


# x = "Hello"
# print(language_detector(text_only_limited))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = [60, 30, 10]
labels = ["Positive", "Negative", "Neutral"]
Period = ["from_date to_date", "from_date to_date", "from_date to_date"]
my_api_df = pd.DataFrame({
    "Probability":data,
    "labels":labels,
    "Period":Period
})

data_365_days_ago = [86.99999999999999, 0.208, 0.9705]
labels_365_days_ago = ["Positive", "Negative", "Neutral"]
Period = ["from_compared_date to_compared_date", "from_compared_date to_compared_date", "from_compared_date to_compared_date"]
my_api_df_365 = pd.DataFrame({
    "Probability":data_365_days_ago,
    "labels":labels_365_days_ago,
    "Period":Period
})



result_df_api_test2 = pd.DataFrame({
  "Period" : ["from_date to_date", "from_compared_date to_compared_date"]  ,
  "Positive" : [data[0], data_365_days_ago[0]],
  "Negative" :[data[1], data_365_days_ago[1]],
  "Neutral" : [data[2], data_365_days_ago[2]]
})
result_df_api_test2.plot(x="Period", y=["Positive", "Negative", "Neutral"], kind="bar")
plt.show()
# frames = [my_api_df, my_api_df_365]
# result_df_api = pd.concat(frames)


# sns.barplot(x = 'Period', y = 'Probability', hue = 'labels', data = result_df_api,
#             palette = 'hls',
#             # order = ['male', 'female'],  
#             capsize = 0.05,             
#             saturation = 8,             
#             errcolor = 'gray', errwidth = 2,  
#             )



# result_df_api.plot(x="Period", y="Probability", kind="bar")
# plt.show()