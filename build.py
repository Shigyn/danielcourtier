# Génère les 5 pages de l'aperçu Daniel B. : python build.py
import os
ICI = os.path.dirname(os.path.abspath(__file__))
V = '1'
URL = 'https://shigyn.github.io/danielcourtier/'

NAV = [('index.html', 'Accueil'), ('prets.html', 'Prêts'), ('accompagnement.html', 'Accompagnement'),
       ('qui-suis-je.html', 'Qui suis-je'), ('contact.html', 'Contact')]

AVERT = 'Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.'


def page(fichier, titre, desc, corps):
    nav = ''.join('<a href="%s"%s>%s</a>' % (f, ' aria-current="page"' if f == fichier else '', n) for f, n in NAV)
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600&family=Young+Serif&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js')</script>
<link rel="stylesheet" href="style.css?v={V}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%231c2733'/%3E%3Ctext x='16' y='22' font-family='Georgia' font-size='17' fill='%23c9c2f2' text-anchor='middle'%3EDB%3C/text%3E%3C/svg%3E">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FinancialService","name":"Daniel B. — Courtier en prêt immobilier","description":"Courtier en prêt immobilier à Valence : recherche du meilleur taux, assurance emprunteur, renégociation.","url":"{URL}","areaServed":["Valence","Drôme","Ardèche"],"address":{{"@type":"PostalAddress","addressLocality":"Valence","postalCode":"26000","addressCountry":"FR"}}}}</script>
</head>
<body>
<div class="apercu"><b>Aperçu préparé par LocWeb</b> pour Daniel B. : photos et vidéos d'illustration, à remplacer par les vôtres.</div>
<header class="entete">
  <div class="conteneur">
    <a class="marque" href="index.html"><b>Daniel B.</b><small>Courtier en prêt immobilier · Valence</small></a>
    <nav class="nav" aria-label="Menu principal">{nav}</nav>
    <a class="bouton" href="contact.html">Être rappelé</a>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<main>
{corps}
</main>
<footer class="pied">
  <div class="conteneur">
    <div class="pied-haut">
      <div>
        <a class="marque" href="index.html"><b>Daniel B.</b><small>Courtier en prêt immobilier · Valence</small></a>
        <p style="margin-top:16px">Rendez-vous à Valence, chez vous ou en visio, partout dans la Drôme et l'Ardèche.</p>
      </div>
      <div><h4>Le site</h4><ul>{''.join('<li><a href="%s">%s</a></li>' % (f, n) for f, n in NAV)}</ul></div>
      <div><h4>Me joindre</h4><ul><li><a href="contact.html">Demander un rappel</a></li><li>Téléphone : <span class="a-completer">à ajouter</span></li><li>E-mail : <span class="a-completer">à ajouter</span></li></ul></div>
    </div>
    <div class="mentions">
      <p><strong>{AVERT}</strong></p>
      <p>Daniel B., courtier en opérations de banque et en services de paiement (COBSP), immatriculé à l'ORIAS sous le n° <span class="a-completer">à compléter</span> (www.orias.fr). Activité soumise au contrôle de l'ACPR, 4 place de Budapest, 75436 Paris Cedex 09.</p>
      <p>Aucun versement, de quelque nature que ce soit, ne peut être exigé d'un particulier avant l'obtention d'un ou plusieurs prêts d'argent.</p>
    </div>
  </div>
</footer>
<script src="app.js?v={V}" defer></script>
</body>
</html>
'''


def curseur(nom, libelle, mini, maxi, pas, val):
    return f'''<div class="curseur"><label for="c-{nom}">{libelle} <output data-o="{nom}"></output></label>
      <input id="c-{nom}" type="range" name="{nom}" min="{mini}" max="{maxi}" step="{pas}" value="{val}"></div>'''


ACCUEIL = f'''
<section class="heros">
  <div class="heros-fond">
    <video data-ambiance autoplay muted loop playsinline preload="auto" poster="videos/cles.webp" aria-hidden="true"><source src="videos/cles.mp4" type="video/mp4"></video>
  </div>
  <div class="conteneur">
    <div class="heros-texte entree">
      <p class="surtitre">Courtier en prêt immobilier à Valence</p>
      <h1>Je mets les banques en concurrence. <em>Vous gardez la différence.</em></h1>
      <p class="chapo">Je monte votre dossier, je le présente aux banques et je négocie le taux, l'assurance et les frais, jusqu'à la signature chez le notaire.</p>
      <div class="heros-actions"><a class="bouton bouton-lavande" href="contact.html">Étudier mon projet</a><a class="bouton bouton-clair" href="accompagnement.html">Comment je travaille</a></div>
    </div>
    <form class="calcul entree-carte" data-calcul="mensualite" onsubmit="return false" aria-label="Calcul de mensualité">
      <h2>Votre mensualité, en direct</h2>
      {curseur('montant', 'Montant emprunté', 30000, 600000, 5000, 220000)}
      {curseur('duree', 'Durée', 7, 25, 1, 25)}
      {curseur('taux', 'Taux nominal', 1.5, 5, 0.05, 3.4)}
      <div class="resultat" aria-live="polite">
        <span class="resultat-libelle">Mensualité hors assurance</span>
        <span class="resultat-chiffre"><span data-o="mens"></span> <small>€ / mois</small></span>
        <span class="resultat-cout">Coût des intérêts<b><span data-o="cout"></span> €</b></span>
      </div>
      <p class="gain">Avec 0,30 point de taux en moins, vous paieriez <b><span data-o="gain"></span> €</b> d'intérêts en moins sur la durée du prêt. C'est ce que je vais chercher.</p>
      <p class="avertissement">Simulation indicative, hors assurance et frais. {AVERT}</p>
    </form>
  </div>
</section>

<section class="section section-blanche">
  <div class="conteneur">
    <div class="tete-section revele">
      <div><p class="surtitre">Ce que je négocie</p><h2>Le taux n'est qu'une des quatre lignes du prix.</h2></div>
      <p>Une banque qui baisse son taux peut se rattraper ailleurs. Je regarde le coût total de votre crédit, ligne par ligne, avant de vous recommander une offre.</p>
    </div>
    <div class="leviers revele">
      <div class="levier"><div class="levier-mot">Taux</div><h3>Le taux nominal</h3><p>Votre dossier présenté à plusieurs banques, avec les arguments qui comptent pour chacune.</p></div>
      <div class="levier"><div class="levier-mot">Assurance</div><h3>L'assurance emprunteur</h3><p>Souvent le deuxième poste de coût. La délégation d'assurance peut le réduire nettement.</p></div>
      <div class="levier"><div class="levier-mot">Frais</div><h3>Les frais de dossier</h3><p>Négociables, et parfois supprimés quand le dossier est solide.</p></div>
      <div class="levier"><div class="levier-mot">Garantie</div><h3>Caution ou hypothèque</h3><p>Le choix de la garantie change le coût à la signature et à la revente.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="conteneur media-perso">
    <div class="cadre-video rideau">
      <img src="photos/rendez-vous.webp" alt="" loading="lazy">
      <div><span class="lecture" aria-hidden="true"></span><strong>Votre vidéo de présentation</strong><small>Une minute face caméra : qui vous êtes, comment vous travaillez.</small></div>
    </div>
    <div class="revele">
      <p class="surtitre">Un interlocuteur, du premier appel aux clés</p>
      <h2>Vous parlez à la même personne du début à la fin.</h2>
      <p class="chapo">Pas de plateforme ni de conseiller qui change à chaque appel. Je connais votre dossier, je relance les banques et je vous explique chaque offre avant que vous la signiez.</p>
      <p class="signature-nom">Daniel B.</p>
    </div>
  </div>
</section>

<section class="section section-blanche">
  <div class="conteneur">
    <div class="tete-section revele">
      <div><p class="surtitre">Votre projet</p><h2>Trois situations, trois façons de monter le dossier.</h2></div>
      <p>Un premier achat, un investissement locatif ou un prêt déjà en cours ne se défendent pas avec les mêmes arguments devant une banque.</p>
    </div>
    <div class="profils">
      <a class="profil revele" href="prets.html#residence"><img src="photos/couple-vide.webp" alt="Un couple assis dans le salon vide de leur nouveau logement" loading="lazy"><div><h3>Premier achat</h3><p>Apport, prêt à taux zéro, prêts aidés : je construis le plan de financement qui passe.</p><span class="lien">Acheter sa résidence →</span></div></a>
      <a class="profil revele" href="prets.html#investissement"><img src="photos/mas.webp" alt="Un mas en pierre au pied des montagnes" loading="lazy"><div><h3>Investissement locatif</h3><p>Les loyers attendus, la durée et l'effort mensuel présentés comme une banque veut les lire.</p><span class="lien">Investir →</span></div></a>
      <a class="profil revele" href="prets.html#renegociation"><img src="photos/maquette.webp" alt="Une maquette de maison posée près d'une calculatrice" loading="lazy"><div><h3>Prêt en cours</h3><p>Renégociation, rachat par une autre banque ou changement d'assurance : on calcule si ça vaut le coup.</p><span class="lien">Faire baisser mon prêt →</span></div></a>
    </div>
  </div>
</section>

<section class="bandeau-local">
  <video data-ambiance autoplay muted loop playsinline preload="metadata" poster="videos/vercors.webp" aria-hidden="true"><source src="videos/vercors.mp4" type="video/mp4"></video>
  <div class="conteneur revele">
    <p class="surtitre" style="color:#c9c2f2">Ici, entre Rhône et Vercors</p>
    <h2>Je connais les banques de Valence, et les prix de la Drôme.</h2>
    <div class="communes"><span>Valence</span><span>Bourg-lès-Valence</span><span>Guilherand-Granges</span><span>Portes-lès-Valence</span><span>Romans-sur-Isère</span><span>Crest</span><span>Tournon-sur-Rhône</span><span>Montélimar</span></div>
  </div>
</section>

<section class="section">
  <div class="conteneur appel revele">
    <p class="surtitre">Premier échange offert</p>
    <h2>Racontez-moi votre projet, je vous dis ce qui est faisable.</h2>
    <p>Une demi-heure au téléphone ou en visio, sans engagement. Mes honoraires ne sont dus qu'une fois votre prêt obtenu.</p>
    <a class="bouton bouton-lavande" href="contact.html">Demander un rappel</a>
  </div>
</section>
'''

PRETS = f'''
<section class="tete-page">
  <div class="conteneur">
    <div class="revele"><p class="surtitre">Les prêts</p><h1>Chaque projet a son montage.</h1></div>
    <p class="chapo revele">Résidence principale, investissement, rachat ou assurance : voici comment je présente chaque dossier aux banques pour obtenir les meilleures conditions.</p>
  </div>
</section>
<div class="conteneur">
  <section class="bloc-pret" id="residence">
    <div class="bloc-pret-photo rideau"><img src="photos/cartons.webp" alt="Un couple porte des cartons dans son nouveau logement" loading="lazy"></div>
    <div class="revele">
      <p class="surtitre">Résidence principale</p>
      <h2>Acheter son logement, premier achat ou non.</h2>
      <p>J'établis votre budget réel, frais de notaire et de garantie compris, puis le plan de financement le plus solide possible.</p>
      <ul class="points"><li>Prêt à taux zéro et prêts aidés si vous y avez droit</li><li>Apport, épargne et reste à vivre présentés en votre faveur</li><li>Achat dans l'ancien, le neuf, la construction ou avec travaux</li></ul>
    </div>
  </section>
  <section class="bloc-pret" id="investissement">
    <div class="bloc-pret-photo rideau"><img src="photos/maison-ocre.webp" alt="Une façade ocre aux volets anciens" loading="lazy"></div>
    <div class="revele">
      <p class="surtitre">Investissement locatif</p>
      <h2>Investir sans vous asphyxier chaque mois.</h2>
      <p>Les banques regardent votre taux d'endettement et les loyers attendus. Je prépare un dossier qui montre un projet rentable et maîtrisé.</p>
      <ul class="points"><li>Prise en compte des loyers selon les règles de chaque banque</li><li>Durée et différé choisis selon votre effort d'épargne</li><li>Location nue, meublée ou petit immeuble de rapport</li></ul>
    </div>
  </section>
  <section class="bloc-pret" id="renegociation">
    <div class="bloc-pret-photo rideau"><img src="photos/maquette.webp" alt="Une maquette de maison posée près d'une calculatrice" loading="lazy"></div>
    <div class="revele">
      <p class="surtitre">Renégociation et rachat</p>
      <h2>Votre prêt actuel peut peut-être coûter moins cher.</h2>
      <p>Je compare votre prêt en cours avec ce que les banques proposent aujourd'hui, pénalités et frais compris. Si l'opération ne vous fait rien gagner, je vous le dis.</p>
      <ul class="points"><li>Renégociation avec votre banque ou rachat par une autre</li><li>Regroupement de crédits quand la situation le justifie</li><li>Calcul du gain net, frais déduits</li></ul>
    </div>
  </section>
  <section class="bloc-pret" id="assurance">
    <div class="bloc-pret-photo rideau"><img src="photos/remise-cles.webp" alt="Une remise de clés autour d'une table" loading="lazy"></div>
    <div class="revele">
      <p class="surtitre">Assurance emprunteur</p>
      <h2>Changer d'assurance, à tout moment.</h2>
      <p>Depuis la loi Lemoine, vous pouvez changer d'assurance de prêt quand vous le souhaitez. À garanties équivalentes, l'économie peut être importante.</p>
      <ul class="points"><li>Comparaison à garanties équivalentes, exigées par votre banque</li><li>Démarches de résiliation et de substitution prises en charge</li><li>Pour un nouveau prêt comme pour un prêt en cours</li></ul>
    </div>
  </section>
</div>
<section class="section section-blanche">
  <div class="conteneur capacite">
    <div class="revele">
      <p class="surtitre">Capacité d'emprunt</p>
      <h2>Combien pouvez-vous emprunter ?</h2>
      <p class="chapo">Les banques limitent la mensualité à 35 % de vos revenus, assurance comprise. Ce calcul donne un ordre de grandeur. Le vrai chiffre dépend de votre dossier complet, et c'est mon travail de le défendre.</p>
    </div>
    <form class="calcul revele" data-calcul="capacite" onsubmit="return false" aria-label="Calcul de capacité d'emprunt">
      {curseur('revenus', 'Revenus nets du foyer par mois', 1500, 12000, 100, 4200)}
      {curseur('charges', 'Crédits en cours par mois', 0, 2000, 50, 0)}
      {curseur('duree', 'Durée', 10, 25, 1, 25)}
      <div class="resultat" aria-live="polite">
        <span class="resultat-libelle">Vous pourriez emprunter environ</span>
        <span class="resultat-chiffre"><span data-o="capacite"></span> <small>€</small></span>
        <span class="resultat-cout">Mensualité maximale<b><span data-o="mens"></span> €</b></span>
      </div>
      <p class="avertissement">Estimation au taux indicatif de 3,40 %, assurance comprise dans la limite des 35 %. {AVERT}</p>
    </form>
  </div>
</section>
'''

ACCOMP = f'''
<section class="tete-page">
  <div class="conteneur">
    <div class="revele"><p class="surtitre">L'accompagnement</p><h1>Du premier appel à la signature chez le notaire.</h1></div>
    <p class="chapo revele">Six étapes, toujours dans le même ordre. À chacune, vous savez ce que j'attends de vous et ce que je fais de mon côté.</p>
  </div>
</section>
<section class="section" style="padding-top:56px">
  <div class="conteneur">
    <ol class="etapes">
      <li class="etape revele"><h3>Premier échange<span class="duree">30 minutes, offert</span></h3><p>Vous me racontez votre projet et votre situation. Je vous dis tout de suite ce qui est faisable, et à quelles conditions.</p></li>
      <li class="etape revele"><h3>Étude du dossier<span class="duree">2 à 5 jours</span></h3><p>Vous m'envoyez vos pièces. J'analyse vos revenus, votre épargne et vos charges, puis je construis le plan de financement.</p></li>
      <li class="etape revele"><h3>Mise en concurrence<span class="duree">1 à 2 semaines</span></h3><p>Je présente votre dossier aux banques choisies pour votre profil, et je négocie taux, assurance, frais et garantie.</p></li>
      <li class="etape revele"><h3>Accord de principe<span class="duree">Selon les banques</span></h3><p>Je compare les propositions sur leur coût total et je vous explique laquelle je recommande, et pourquoi.</p></li>
      <li class="etape revele"><h3>Offre de prêt<span class="duree">10 jours de réflexion</span></h3><p>La banque émet l'offre. La loi vous laisse dix jours de réflexion avant de l'accepter : je relis chaque ligne avec vous.</p></li>
      <li class="etape revele"><h3>Signature chez le notaire<span class="duree">Le jour des clés</span></h3><p>Je m'assure que les fonds sont débloqués à temps. Vous signez, vous récupérez les clés.</p></li>
    </ol>
  </div>
</section>
<section class="section section-sombre">
  <div class="conteneur">
    <div class="tete-section revele">
      <div><p class="surtitre">Pour gagner du temps</p><h2>Les pièces à préparer</h2></div>
      <p>Un dossier complet dès le départ, c'est une réponse plus rapide des banques. Je vous envoie la liste exacte selon votre situation.</p>
    </div>
    <div class="pieces">
      <div class="piece revele"><h3>Votre identité</h3><ul><li>Pièce d'identité</li><li>Livret de famille ou PACS</li><li>Justificatif de domicile</li></ul></div>
      <div class="piece revele"><h3>Vos revenus</h3><ul><li>3 derniers bulletins de salaire</li><li>2 derniers avis d'imposition</li><li>Contrat de travail</li></ul></div>
      <div class="piece revele"><h3>Vos comptes et le projet</h3><ul><li>3 derniers relevés de comptes</li><li>Justificatifs d'épargne</li><li>Compromis de vente ou devis</li></ul></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="conteneur">
    <div class="encart revele">
      <div class="encart-mot">0 €</div>
      <div><h3>Rien à payer avant d'avoir votre prêt.</h3><p>Mes honoraires sont fixés dans un mandat signé dès le départ et ne sont dus qu'une fois votre prêt obtenu. C'est la loi, et c'est aussi ma façon de travailler.</p></div>
    </div>
  </div>
</section>
'''

QUI = '''
<section class="tete-page">
  <div class="conteneur">
    <div class="revele"><p class="surtitre">Qui suis-je</p><h1>Daniel B., courtier à Valence.</h1></div>
    <p class="chapo revele">Mon métier : défendre votre dossier devant les banques, pour que votre projet passe aux meilleures conditions.</p>
  </div>
</section>
<section class="section">
  <div class="conteneur presentation">
    <div class="cadre-portrait rideau">
      <img src="photos/falaise.webp" alt="" loading="lazy">
      <div><strong>Votre portrait</strong><small>Une photo de vous, dans votre bureau ou dans Valence.</small></div>
    </div>
    <div class="presentation-texte revele">
      <p>Acheter un logement, c'est souvent la plus grosse décision financière d'une vie. Pourtant, beaucoup d'emprunteurs signent la première offre de leur banque, faute de temps ou de points de comparaison.</p>
      <p>Mon rôle est de faire ce travail à votre place : comprendre votre situation, monter un dossier clair, le présenter aux banques qui correspondent à votre profil, puis négocier chaque ligne de l'offre.</p>
      <p class="citation">« Je préfère vous dire non tout de suite que vous faire perdre trois mois. »</p>
      <p><span class="a-completer">À compléter avec Daniel</span> : son parcours, depuis quand il exerce, ce qui l'a amené au courtage.</p>
    </div>
  </div>
</section>
<section class="section section-blanche">
  <div class="conteneur">
    <div class="tete-section revele"><div><p class="surtitre">Ma façon de travailler</p><h2>Trois engagements</h2></div><p>Ce que vous pouvez attendre de moi, à chaque étape du dossier.</p></div>
    <div class="valeurs">
      <div class="revele"><h3>Je vous dis la vérité</h3><p>Si votre projet ne passe pas en l'état, je vous l'explique, et je vous dis ce qu'il faut changer pour qu'il passe.</p></div>
      <div class="revele"><h3>Je reste joignable</h3><p>Un numéro, une personne. Vous savez toujours où en est votre dossier.</p></div>
      <div class="revele"><h3>Je compare le coût total</h3><p>Taux, assurance, frais et garantie : je recommande l'offre la moins chère sur toute la durée, pas seulement le plus beau taux.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="conteneur media-perso">
    <div class="revele"><p class="surtitre">En vidéo</p><h2>Mes conseils avant d'acheter</h2><p class="chapo">Des vidéos courtes pour préparer votre projet : l'apport, l'assurance, la renégociation. Elles se placent ici dès que vous les avez tournées.</p></div>
    <div class="cadre-video rideau"><img src="photos/maison-pierre.webp" alt="" loading="lazy"><div><span class="lecture" aria-hidden="true"></span><strong>Vos vidéos conseils</strong><small>Tournées au téléphone, cela suffit largement.</small></div></div>
  </div>
</section>
'''

CONTACT = '''
<section class="tete-page">
  <div class="conteneur">
    <div class="revele"><p class="surtitre">Contact</p><h1>Parlons de votre projet.</h1></div>
    <p class="chapo revele">Laissez-moi quelques informations : je vous rappelle sous 24 h ouvrées pour un premier échange offert.</p>
  </div>
</section>
<div class="conteneur contact">
  <form class="formulaire revele">
    <fieldset class="choix-projet champ">
      <legend>Votre projet</legend>
      <label><input type="radio" name="projet" value="achat" checked><span>Acheter ma résidence</span></label>
      <label><input type="radio" name="projet" value="investir"><span>Investir</span></label>
      <label><input type="radio" name="projet" value="renegocier"><span>Renégocier mon prêt</span></label>
      <label><input type="radio" name="projet" value="assurance"><span>Changer d'assurance</span></label>
    </fieldset>
    <div class="champ"><label for="f-nom">Nom et prénom</label><input id="f-nom" name="nom" autocomplete="name" required></div>
    <div class="champ"><label for="f-tel">Téléphone</label><input id="f-tel" name="tel" type="tel" autocomplete="tel" required></div>
    <div class="champ"><label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email"></div>
    <div class="champ"><label for="f-montant">Montant envisagé</label><select id="f-montant" name="montant"><option>Je ne sais pas encore</option><option>Moins de 150 000 €</option><option>150 000 à 300 000 €</option><option>Plus de 300 000 €</option></select></div>
    <div class="champ champ-large"><label for="f-msg">Votre projet en quelques mots</label><textarea id="f-msg" name="message" rows="5" placeholder="Ville, type de bien, apport, date souhaitée…"></textarea></div>
    <label class="consentement"><input type="checkbox" required> J'accepte que Daniel B. utilise ces informations pour me recontacter au sujet de mon projet. Elles ne sont transmises à aucun tiers sans mon accord.</label>
    <button class="bouton bouton-lavande" type="submit">Envoyer ma demande</button>
  </form>
  <aside class="coordonnees revele">
    <div><h3>Par téléphone</h3><p><span class="a-completer">Numéro à ajouter</span><br>Du lundi au samedi</p></div>
    <div><h3>Rendez-vous</h3><p>À Valence, chez vous ou en visio. Partout dans la Drôme et l'Ardèche.</p></div>
    <div><h3>Honoraires</h3><p>Premier échange offert. Rien à payer avant l'obtention de votre prêt.</p></div>
    <div class="bloc-pret-photo rideau" style="aspect-ratio:4/3"><img src="photos/maison-rose.webp" alt="Une maison aux volets pastel" loading="lazy"></div>
  </aside>
</div>
'''

PAGES = [
    ('index.html', 'Daniel B. | Courtier en prêt immobilier à Valence', 'Courtier en prêt immobilier à Valence : je mets les banques en concurrence et je négocie taux, assurance et frais pour votre projet.', ACCUEIL),
    ('prets.html', 'Prêts immobiliers | Daniel B., courtier à Valence', 'Résidence principale, investissement locatif, renégociation, assurance emprunteur : le montage adapté à chaque projet.', PRETS),
    ('accompagnement.html', 'Accompagnement | Daniel B., courtier à Valence', "Les six étapes d'un prêt immobilier avec Daniel B., du premier échange à la signature chez le notaire.", ACCOMP),
    ('qui-suis-je.html', 'Qui suis-je | Daniel B., courtier à Valence', 'Daniel B., courtier en prêt immobilier à Valence : ma façon de travailler.', QUI),
    ('contact.html', 'Contact | Daniel B., courtier à Valence', 'Demandez un rappel : premier échange offert, rien à payer avant l\'obtention de votre prêt.', CONTACT),
]
for f, t, d, c in PAGES:
    open(os.path.join(ICI, f), 'w', encoding='utf-8', newline='\n').write(page(f, t, d, c))
open(os.path.join(ICI, 'robots.txt'), 'w', newline='\n').write('User-agent: *\nDisallow: /\n')
print('ok', len(PAGES))
