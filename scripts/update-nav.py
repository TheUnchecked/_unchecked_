import os
import re

ARTICLES = [
    {"file": "la-matematica-degli-agent.html", "num": "10", "title": "La matematica degli agent non mente, ma siamo sicuri che basti questo?", "tags": ["AI", "Lavoro"]},
    {"file": "exchange-split-permissions.html", "num": "09", "title": "Exchange on-prem: il rischio che dorme nella tua configurazione di default", "tags": ["Exchange", "Security"]},
    {"file": "ho-fallito-la-certificazione.html", "num": "08", "title": "27 anni di IT. Bocciato per 20 centesimi.", "tags": ["IT Career"]},
    {"file": "zero-trust.html", "num": "07", "title": "Zero Trust non è un prodotto. È una mentalità.", "tags": ["Security"]},
    {"file": "domain-join-risks.html", "num": "06", "title": "La falla silenziosa: i rischi dell'account Domain Join.", "tags": ["Active Directory", "Security"]},
    {"file": "adminsdholder.html", "num": "05", "title": "AdminSDHolder: perché i tuoi permessi spariscono ogni 60 minuti.", "tags": ["Active Directory"]},
    {"file": "rc4-kerberos-2026.html", "num": "04", "title": "RC4 e Kerberos: hai tempo fino a luglio 2026.", "tags": ["Kerberos", "Security"]},
    {"file": "azure-storage.html", "num": "03", "title": "Azure Storage: scegli la ridondanza sbagliata e lo scopri nel momento peggiore.", "tags": ["Azure", "Cloud"]},
    {"file": "la-vita-và-così.html", "num": "02", "title": "Ovidio Marras: l'eroe che nessuno di noi sarebbe.", "tags": ["Società"]},
    {"file": "IA-Lavoro.html", "num": "01", "title": "L'IA ci ruberà il lavoro? Solo se lo meriti.", "tags": ["AI", "Lavoro"]},
]

# L'ultimo articolo è quello con il numero più alto
LATEST = max(ARTICLES, key=lambda a: int(a["num"]))

HTML_NAV = """
<nav class="article-nav" id="article-nav"></nav>
<div style="text-align:center;">
  <a href="../index.html" class="nav-back-home" id="back-home-link">← Tutti gli articoli</a>
</div>"""

JS_NAV = """
const ARTICLES = """ + str(ARTICLES).replace("'", '"') + """;

(function() {
  const currentFile = window.location.pathname.split('/').pop();
  const idx = ARTICLES.findIndex(a => a.file === currentFile);
  if (idx === -1) return;

  const prev = idx > 0 ? ARTICLES[idx - 1] : null;
  const next = idx < ARTICLES.length - 1 ? ARTICLES[idx + 1] : null;

  function buildLink(article, direction) {
    if (!article) {
      return `<div class="article-nav-link nav-${direction} nav-placeholder">
        <span class="nav-direction">${direction === 'prev' ? '← Precedente' : 'Successivo →'}</span>
      </div>`;
    }
    const tags = article.tags.map(t => `<span class="nav-tag">${t}</span>`).join('');
    const l
