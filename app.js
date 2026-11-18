(function () {
  var calme = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Menu mobile
  var entete = document.querySelector('.entete'), burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var o = entete.classList.toggle('ouvert');
    burger.setAttribute('aria-expanded', o);
  });

  // Apparitions au défilement
  var cibles = document.querySelectorAll('.revele, .rideau');
  if ('IntersectionObserver' in window && !calme) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('vu'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px' });
    cibles.forEach(function (c) { io.observe(c); });
  } else cibles.forEach(function (c) { c.classList.add('vu'); });

  // Vidéos d'ambiance : en pause hors écran, absentes si l'utilisateur limite les animations
  document.querySelectorAll('video[data-ambiance]').forEach(function (v) {
    if (calme) { v.removeAttribute('autoplay'); v.pause(); return; }
    if (!('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause(); });
    }).observe(v);
  });

  var euro = new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 0 });
  function remplir(r) { r.style.setProperty('--p', ((r.value - r.min) / (r.max - r.min) * 100) + '%'); }

  // Le chiffre glisse vers sa nouvelle valeur au lieu de sauter
  function animer(el, cible) {
    var depart = +el.dataset.v || 0; el.dataset.v = cible;
    if (calme || !depart) { el.textContent = euro.format(cible); return; }
    var t0 = performance.now(), d = 420;
    cancelAnimationFrame(el._raf);
    (function pas(t) {
      var k = Math.min(1, (t - t0) / d), e = 1 - Math.pow(1 - k, 3);
      el.textContent = euro.format(depart + (cible - depart) * e);
      if (k < 1) el._raf = requestAnimationFrame(pas);
    })(t0);
  }
  function mensualite(capital, ans, taux) {
    var i = taux / 100 / 12, n = ans * 12;
    return i ? capital * i / (1 - Math.pow(1 + i, -n)) : capital / n;
  }

  // Calcul de mensualité (accueil)
  var cm = document.querySelector('[data-calcul="mensualite"]');
  if (cm) {
    var m = cm.querySelector('[name=montant]'), d = cm.querySelector('[name=duree]'), t = cm.querySelector('[name=taux]');
    var maj = function () {
      [m, d, t].forEach(remplir);
      var c = +m.value, n = +d.value, tx = +t.value;
      cm.querySelector('[data-o=montant]').textContent = euro.format(c) + ' €';
      cm.querySelector('[data-o=duree]').textContent = n + ' ans';
      cm.querySelector('[data-o=taux]').textContent = tx.toFixed(2).replace('.', ',') + ' %';
      var mens = mensualite(c, n, tx), cout = mens * n * 12 - c;
      var mieux = mensualite(c, n, Math.max(0, tx - 0.3)), gain = (mens - mieux) * n * 12;
      animer(cm.querySelector('[data-o=mens]'), Math.round(mens));
      animer(cm.querySelector('[data-o=cout]'), Math.round(cout));
      animer(cm.querySelector('[data-o=gain]'), Math.round(gain / 10) * 10);
    };
    [m, d, t].forEach(function (x) { x.addEventListener('input', maj); });
    maj();
  }

  // Capacité d'emprunt (page Prêts) : 35 % des revenus, assurance comprise
  var cc = document.querySelector('[data-calcul="capacite"]');
  if (cc) {
    var rv = cc.querySelector('[name=revenus]'), ch = cc.querySelector('[name=charges]'), du = cc.querySelector('[name=duree]');
    var maj2 = function () {
      [rv, ch, du].forEach(remplir);
      cc.querySelector('[data-o=revenus]').textContent = euro.format(+rv.value) + ' €';
      cc.querySelector('[data-o=charges]').textContent = euro.format(+ch.value) + ' €';
      cc.querySelector('[data-o=duree]').textContent = du.value + ' ans';
      var mens = Math.max(0, rv.value * 0.35 - ch.value);
      var i = 3.4 / 100 / 12, n = du.value * 12;
      var cap = mens * (1 - Math.pow(1 + i, -n)) / i;
      animer(cc.querySelector('[data-o=mens]'), Math.round(mens));
      animer(cc.querySelector('[data-o=capacite]'), Math.round(cap / 1000) * 1000);
    };
    [rv, ch, du].forEach(function (x) { x.addEventListener('input', maj2); });
    maj2();
  }

  // Formulaire : aperçu, rien n'est envoyé
  var f = document.querySelector('.formulaire');
  if (f) f.addEventListener('submit', function (e) {
    e.preventDefault();
    var old = f.querySelector('.merci'); if (old) old.remove();
    var p = document.createElement('p');
    p.className = 'merci'; p.setAttribute('role', 'status');
    p.textContent = 'Aperçu : sur le vrai site, votre demande arrive directement chez Daniel, qui vous rappelle sous 24 h ouvrées.';
    f.appendChild(p);
  });
})();
